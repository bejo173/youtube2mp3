
class ScrapedYoutubeVideo:
    """Represents a scraped video"""

    def __init__(self, video_id, download_url):
        self.video_id = video_id
        self.download_url = download_url

    def __dict__(self):
        return {
            "video_id": self.video_id,
            "download_url": self.download_url
        }
