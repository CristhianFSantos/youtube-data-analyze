from search import Search
from utils import Utils
from mail import Mail

class Start:
    search = Search()
    utils = Utils()
    mail = Mail()
        
    
    def run_initial_search(self, data):
        response = self.search.get_lists_data_youtube(data)
        email = data['email']
        
        for comment in response['comments']:
            comment['textOriginal'] = self.utils.clear_text(comment['textOriginal'])
       
        
        self.mail.send_mail(email, 'Pesquisa Avançada no Youtube', 'api-youtube-data-analyze/src/templates/email_result.html')
        print('email enviado com sucesso!')
        