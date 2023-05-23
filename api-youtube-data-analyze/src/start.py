from search import Search
from utils import Utils
from mail import Mail
from csv_tools import CsvTools
from process_data import ProcessData
import pandas as pd

class Start:
    search = Search()
    utils = Utils()
    mail = Mail()
    csv_tools = CsvTools()
        
    
    def run_initial_search(self, data):
        response_json = self.search.get_lists_data_youtube(data)
        email = data['email']
        
        for comment in response_json['comments']:
            comment['textOriginal'] = self.utils.clear_text(comment['textOriginal'])
            
        df_comments = pd.DataFrame(response_json['comments'])
        resultados = ProcessData().process_data_frame(df_comments)
        
        df_videos = pd.DataFrame(response_json['videos'])
        df_statistics = pd.DataFrame(response_json['statistics'])     
        df_resultados_categorizados = resultados['resultados_categorizados']
        df_resultados_agrupados = resultados['resultados_agrupados']

            
        self.mail.send_mail(email, 'Pesquisa Avançada no Youtube', 'api-youtube-data-analyze/src/templates/email_result.html')
        print('email enviado com sucesso!')
        