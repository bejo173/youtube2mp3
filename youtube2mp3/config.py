import os
from scraper import YoutubeDlScraper

basedir = os.path.dirname(os.path.dirname(__file__))


class AppConfig:
    """Application configuration.
    Encapsulates run-time resources and settings utilized throughout API resources.
    """
    """Initialize application's configs"""
    _STATIC_DIR = 'static'
    STATIC_PATH = '/%s'.format(_STATIC_DIR)
    HOST = 'http://127.0.0.1:5000'

    # Where scraped stuff should be saved
    SCRAPING_OUTPUT = os.path.join(basedir, _STATIC_DIR, 'scraped')

    def __init__(self):
        self.scraper = YoutubeDlScraper()


class ProductionConfig(AppConfig):
    DEBUG = False
    HOST = 'http://54.159.247.16'

    def __init__(self):
        super().__init__()


class DevelopmentConfig(AppConfig):
    DEVELOPMENT = True
    DEBUG = True

    def __init__(self):
        super().__init__()
