import os
from scraper import YoutubeDlScraper

basedir = os.path.dirname(os.path.dirname(__file__))


class AppConfig:
    """Application configuration.
    Encapsulates run-time resources and settings utilized throughout API resources.
    """
    _STATIC_DIR = 'static'
    STATIC_PATH = '/%s'.format(_STATIC_DIR)

    # A port on which the application will be running.
    # In production it is recommended to leave it as is and redirect to it
    # from a production web server (e.g. nginx or apache).
    PORT = 5000

    # HOST is used to build the URL from which a scraped MP3 file can be downloaded
    HOST = 'http://127.0.0.1:' + PORT.__str__()

    # Where scraped stuff should be saved
    SCRAPING_OUTPUT = os.path.join(basedir, _STATIC_DIR, 'scraped')

    def __init__(self):
        self.scraper = YoutubeDlScraper()


class ProductionConfig(AppConfig):
    DEBUG = False
    HOST = 'https://yyk.herokuapp.com'

    def __init__(self):
        super().__init__()


class DevelopmentConfig(AppConfig):
    DEVELOPMENT = True
    DEBUG = True

    def __init__(self):
        super().__init__()
