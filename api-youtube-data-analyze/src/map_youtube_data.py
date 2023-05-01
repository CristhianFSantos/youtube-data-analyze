class MapYoutubeData:
    def map_videos(self, response_json):
        videos = []
        for search_result in response_json.get("items", []):
            if search_result["id"]["kind"] == "youtube#video":
                videos.append({
                    'videoId': search_result["id"]["videoId"],
                    'channelId': search_result["snippet"]["channelId"],
                    'publishedAt': search_result["snippet"]["publishedAt"],
                    'title': search_result["snippet"]["title"],
                    'channelTitle': search_result["snippet"]["channelTitle"],
                })
        return videos    
    
    def map_comments(self, response_json):
        comments = []
        for search_result in response_json.get("items", []):
            comments.append({
                'commentId': search_result["id"],
                'videoId': search_result["snippet"]["videoId"],
                'publishedAt': search_result["snippet"]["topLevelComment"]["snippet"]["publishedAt"],
                'updatedAt': search_result["snippet"]["topLevelComment"]["snippet"]["updatedAt"],
                'textOriginal': search_result["snippet"]["topLevelComment"]["snippet"]["textOriginal"],
                'authorDisplayName': search_result["snippet"]["topLevelComment"]["snippet"]["authorDisplayName"],
                'likeCount': search_result["snippet"]["topLevelComment"]["snippet"]["likeCount"],
            })
        return comments
    
    def map_statistics(self, response_json):
        statistics = []
        for search_result in response_json.get("items", []):
            statistics.append({
                'videoId': search_result["id"],
                'viewCount': search_result["statistics"]["viewCount"],
                'likeCount': search_result["statistics"]["likeCount"],
                'favoriteCount': search_result["statistics"]["favoriteCount"],
                'commentCount': search_result["statistics"]["commentCount"],
            })
        return statistics