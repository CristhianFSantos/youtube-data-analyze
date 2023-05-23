import pandas as pd
import numpy as np
import re
from tqdm.notebook import tqdm
from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification
from scipy.special import softmax
import torch
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer,PorterStemmer
from nltk.corpus import stopwords 
from nltk.stem import RSLPStemmer


class ProcessData:
    model_route = 'cardiffnlp/xlm-v-base-tweet-sentiment-pt'
    tokenizer = AutoTokenizer.from_pretrained(model_route)
    model = AutoModelForSequenceClassification.from_pretrained(model_route)

    def polarity_scores_roberta(self, text):
        device = "cuda:0" if torch.cuda.is_available() else "cpu"
        encoded_text = self.tokenizer(text, return_tensors='pt').to(device)
        model_psr = self.model.to(device)
        output = model_psr(**encoded_text)
        scores = output[0][0].detach().cpu().numpy()
        scores = softmax(scores)
        scores_dict = {
            'roberta_neg' : scores[0],
            'roberta_neu' : scores[1],
            'roberta_pos' : scores[2]
        }
        return scores_dict
    
    
    def preprocess(self, sentence):
        lemmatizer = WordNetLemmatizer()
        stemmerPT = RSLPStemmer()

        language = "portuguese"
        stop_words = set(stopwords.words(language)) 

        remove_stop_words = False
        remove_stem_words = False
        remove_lemma_wrods = False
        
        
        sentence=str(sentence)
        sentence = sentence.lower()
        sentence=sentence.replace('{html}',"") 
        cleanr = re.compile('<.*?>')
        cleantext = re.sub(cleanr, '', sentence)
        rem_url=re.sub(r'http\S+', '',cleantext)
        rem_num = re.sub('[0-9]+', '', rem_url)
        tokenizer = RegexpTokenizer(r'\w+')
        tokens = tokenizer.tokenize(rem_num)  
        if(remove_stop_words):
          filtered_words = [w for w in tokens if len(w) > 2 if not w in stop_words]
        else:
          filtered_words = [w for w in tokens]
        if(remove_stem_words):
          filtered_words = [stemmerPT.stem(w) for w in filtered_words]
        if(remove_lemma_wrods):
          filtered_words = [lemmatizer.lemmatize(w) for w in filtered_words] 
        return " ".join(filtered_words)

    def process_data_frame(self, df_pandas):
        df_preprocessed = df_pandas.copy()
        df_preprocessed['textOriginal'] = np.array(df_preprocessed['textOriginal'].map(lambda s:self.preprocess(s)))       

        res = {}
        ids_com_erro = []
        for i, row in tqdm(df_preprocessed.iterrows(), total=len(df_preprocessed)):
            try:
                text = row['textOriginal']
                myid = row['commentId']

                roberta_result = self.polarity_scores_roberta(text)
                print(len(df_preprocessed) - i)

                res[myid] = roberta_result
            except Exception as e:
                print(str(e))
                print(f'Erro em commentId: {myid}')
                ids_com_erro.append(myid)
        
        
        results_df = pd.DataFrame(res).T
        results_df = results_df.reset_index().rename(columns={'index': 'commentId'})
        results_df = results_df.merge(df_preprocessed, how='right')        


        results_df_categorizado = results_df
        results_df_categorizado['Sentimento'] = ""


        for index, row in results_df_categorizado.iterrows():
          valor_max = max(float(row['roberta_neg']), 
                         float(row['roberta_neu']),
                         float(row['roberta_pos']))
          texto_sentimento = ""
          if(valor_max == float(row['roberta_neg'])):
            texto_sentimento = "Negativo"
          elif(valor_max == float(row['roberta_neu'])):
            texto_sentimento = "Neutro"
          elif(valor_max == float(row['roberta_pos'])):
            texto_sentimento = "Positivo"
          else:
            texto_sentimento = "Sem resultado"
          results_df_categorizado.at[index, 'Sentimento'] = texto_sentimento
  
  
        df_total = results_df_categorizado.copy()
        df_total['N_total']=1
        df_count = df_total.groupby(['videoId'] ,  as_index=False)['N_total'].sum()
        
        df_positivo = results_df_categorizado.copy()
        df_positivo['N_positivo']=1
        df_positivo = df_positivo.groupby(['videoId','Sentimento'] ,  as_index=False)['N_positivo'].sum()
        df_positivo=df_positivo[df_positivo['Sentimento']=='Positivo'].copy()
        
        df_count=pd.merge(df_count,df_positivo,on='videoId')
        df_count['Perc_positivo']=((df_count['N_positivo']/df_count['N_total'])*100)
      
        return {
            'resultados_categorizados': results_df_categorizado,
            'resultados_agrupados': df_count,
        }