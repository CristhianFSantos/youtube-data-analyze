from termcolor import colored
import datetime


class LogTools: 
    def log_success(self, message):
        print(colored(message, 'green'))
    
    
    def log_error(self, message):
        print(colored(message, 'red'))


    def log_warning(self, message):
        print(colored(message, 'yellow'))


    def log_with_time_now(self, message):
        print(colored(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S") + ' - ' + message, 'blue'))