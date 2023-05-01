from json_tools import JsonTools
from googleapiclient.discovery import build


class YouTube:
    
    ## Create api_key.json file in the root directory of the project and get api key in https://console.developers.google.com/apis/credentials
    def get_developer_key(self) -> str :
        json_tools = JsonTools()
        data_json = json_tools.read_json('api_key.json') ## This file is not in the repository because it contains sensitive data
        developer_key = data_json['developerKey']
        return developer_key
    
    
    def build_youtube_service(self):
        DEVELOPER_KEY = self.get_developer_key()
        YOUTUBE_API_SERVICE_NAME = "youtube"
        YOUTUBE_API_VERSION = "v3"
        
        youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
        return youtube
    
    
    # As requisições possuem quotas de uso, que são limitadas, mas informações em: 
    # https://developers.google.com/youtube/v3/getting-started?hl=pt-br#quota
    # https://developers.google.com/youtube/v3/determine_quota_cost?hl=pt-br
    # https://i.stack.imgur.com/fAEkl.png
    def get_videos(self, query, region_code):
        search_response = self.build_youtube_service().search().list(
            q = query,
            part = "id,snippet",
            regionCode = region_code,
            maxResults = 50
        ).execute()
        return search_response
    
    def get_video_statistics(self, video_id):
        statistics_response = self.build_youtube_service().videos().list(
            part = "statistics",
            id = video_id
        ).execute()
        return statistics_response
    
    def get_video_comments(self, video_id):
        comments_response = self.build_youtube_service().commentThreads().list(
            part = "snippet",
            videoId = video_id,
            maxResults = 100
        ).execute()
        return comments_response