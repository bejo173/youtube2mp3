from abc import abstractmethod
import subprocess
from model import ScrapedYoutubeVideo


class ScraperException(Exception):
    pass


class BaseYoutubeScraper:
    @abstractmethod
    def scrape(self, video_id: str, dest: str):
        """Scrapes a video from Youtube with a given ID.

        :param video_id: ID of a Youtube video
        :param dest: Where to save the scraped stuff

        :returns Saved filename

        :rtype: str
        """
        raise NotImplemented


class YoutubeDlScraper(BaseYoutubeScraper):
    """A scraper which scrapes a Youtube video using 'youtube-dl'.
    It downloads the video and extracts an audio from it in mp3 format.

    :returns Saved filename

    :rtype: str
    """
    def scrape(self, video_id: str, dest: str):

        exit_with_error = subprocess.call(
            ['youtube-dl', '--extract-audio', '--audio-format=mp3',
             '--output=' + dest + '/%(id)s.%(ext)s', video_id]
        )

        if exit_with_error:
            raise ScraperException("Error! Failed to scrape video (Video ID: %s)".format(video_id))

        return video_id + ".mp3"
