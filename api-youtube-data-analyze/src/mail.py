import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from json_tools import JsonTools
from email.mime.base import MIMEBase
from email import encoders

class Mail:
    json_tools = JsonTools()
    
    def get_mail_credentials(self):
        data_json = self.json_tools.read_json('api-youtube-data-analyze/mail_credentials.json')
        return {
            'smtp_server':  data_json['smtp_server'],
            'smtp_port':  data_json['smtp_port'],
            'smtp_username': data_json['smtp_username'],
            'smtp_password': data_json['smtp_password'],
        }
        
    def send_mail(self, recipient, subject, template_path):
        credentials = self.get_mail_credentials()
        
        message = MIMEMultipart()
        message['From'] = credentials['smtp_username']
        message['To'] = recipient
        message['Subject'] = subject

        with open(template_path, 'r', encoding='utf-8') as file:
            template = file.read()

        
        body = MIMEText(template, 'html', 'utf-8')
        body.add_header('Content-Type', 'text/html; charset=utf-8')
        message.attach(body)
        
        
        filename = 'anexo.csv'
        with open(filename, 'rb') as f:
            
            attachment = MIMEBase('application', 'octet-stream')
            attachment.set_payload(f.read())

            
            encoders.encode_base64(attachment)

            
            attachment.add_header('Content-Disposition', f'attachment; filename={filename}')
            message.attach(attachment)
    
        with smtplib.SMTP(credentials['smtp_server'], credentials['smtp_port']) as server:
            server.starttls()
            server.login(credentials['smtp_username'], credentials['smtp_password'])

            server.sendmail(credentials['smtp_username'], recipient, message.as_string())
            server.quit()