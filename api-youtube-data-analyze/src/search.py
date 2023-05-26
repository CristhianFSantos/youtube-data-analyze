from youtube_tools import YouTube
from map_youtube_data import MapYoutubeData
from log_tools import LogTools
from utils import Utils
class Search:
    
    map_youtube_data = MapYoutubeData()
    youtube_tools = YouTube()
    log_tools = LogTools()
    utils = Utils()
    
    def get_lists_data_youtube(self, response):
        search = response['search']
        
        self.log_tools.log_with_time_now('get videos')        
        full_videos = self.map_youtube_data.map_videos(self.youtube_tools.get_videos(search))
        
        videos_key = 'videoId'  
        videos = self.utils.remove_duplicates(full_videos, videos_key)
        videos_id = list(map(lambda video: video[videos_key], videos))
        
        statistics = []
        comments = []
        self.log_tools.log_with_time_now('get statistics and comments')        
        for video_id in videos_id:
            statistics += self.map_youtube_data.map_statistics(self.youtube_tools.get_video_statistics(video_id))
            comments += self.map_youtube_data.map_comments(self.youtube_tools.get_video_comments(video_id))
            
        return {
            'videos': videos,
            'statistics': statistics,
            'comments': comments,
        }