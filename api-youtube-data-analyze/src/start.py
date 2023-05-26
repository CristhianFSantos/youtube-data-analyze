from tabulate import tabulate
from search import Search
from utils import Utils
from mail import Mail
from csv_tools import CsvTools
from process_data import ProcessData
from log_tools import LogTools
import pandas as pd

class Start:
    search = Search()
    utils = Utils()
    mail = Mail()
    csv_tools = CsvTools()
    log_tools = LogTools()
    process_data = ProcessData()
        
    
    def run_initial_search(self, data):
        email = data['email']
        ############# Processo de busca inicial na API do Youtube
        self.log_tools.log_with_time_now('query data in youtube api')
        
        response_json = self.search.get_lists_data_youtube(data)
        
        self.log_tools.log_success('query data in youtube api finished')        
        
        ############# Processo de limpeza, processamento e categorização dos dados
        self.log_tools.log_with_time_now('comment processing step started')
        
        for comment in response_json['comments']:
            comment['textOriginal'] = self.utils.clear_text(comment['textOriginal'])
        df_comments = pd.DataFrame(response_json['comments'])
        processed_comments = self.process_data.process_data_frame(df_comments)
        
        self.log_tools.log_success('completed comment processing step')        
        
        
        ############# Processo de limpeza, processamento e categorização dos dados
        self.log_tools.log_with_time_now('grouping the processing results')
        
        df_videos = pd.DataFrame(response_json['videos'])
        df_statistics = pd.DataFrame(response_json['statistics'])     
        resultados_agrupados = processed_comments['resultados_agrupados']
        df_total_result = pd.merge(df_videos, df_statistics, on='videoId')
        df_total_result = pd.merge(df_total_result, resultados_agrupados, on='videoId')
        df_total_result['link'] = 'https://www.youtube.com/watch?v=' + df_total_result['videoId']
        
        self.log_tools.log_success('completed grouping the processing results')
        
        ############# Transformando o resultado em uma tabela de texto para ser enviado por email
        self.log_tools.log_with_time_now('transforming the result into a text table to be sent by email')
        df_last_result = df_total_result[['videoId', 'title', 'channelTitle', 'viewCount', 'likeCount', 'commentCount', 'N_positivo', 'Perc_positivo', 'link']]
        df_last_result = df_last_result.sort_values(['Perc_positivo', 'viewCount', 'likeCount', 'commentCount'], ascending=[False, False, False, False])
        df_last_result_top_10 = df_last_result.head(10)
        df_last_result_top_10 = df_last_result_top_10[['title', 'channelTitle', 'link']]
        df_last_result_top_10.columns = ['Titulo do video', 'Canal do video', 'Link do video']
        text_result = tabulate(df_last_result_top_10, headers='keys', tablefmt='psql')
        print(text_result)               
        
        
        ############# Processo de envio de email com os resultados
        