from search import Search
from utils import Utils
from mail import Mail
from csv_tools import CsvTools

class Start:
    search = Search()
    utils = Utils()
    mail = Mail()
    csv_tools = CsvTools()
        
    
    def run_initial_search(self, data):
        response = self.search.get_lists_data_youtube(data)
        email = data['email']
        
        for comment in response['comments']:
            comment['textOriginal'] = self.utils.clear_text(comment['textOriginal'])
            
        for video in response['videos']:
            video['title'] = self.utils.clear_text(video['title'])        
    
        self.csv_tools.write_data_frame_to_csv(response['videos'], 'api-youtube-data-analyze/src/anexos/videos.csv')    
        self.csv_tools.write_data_frame_to_csv(response['comments'], 'api-youtube-data-analyze/src/anexos/comments.csv')    
        self.csv_tools.write_data_frame_to_csv(response['statistics'], 'api-youtube-data-analyze/src/anexos/statistics.csv')    
        
        self.mail.send_mail(email, 'Pesquisa Avançada no Youtube', 'api-youtube-data-analyze/src/templates/email_result.html')
        print('email enviado com sucesso!')
        