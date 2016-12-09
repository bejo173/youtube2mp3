#!/env/bin/python
# -*- coding: UTF8 -*-
"""
app.py
Application entry point.

The application expects APP_CONFIG environment variable to be set to a corresponding class
within 'config.py' module.

Example

Author: Yuri Kroz
Web site: https://github.com/splanger
"""
from __future__ import print_function
from flask import Flask, request, send_from_directory
import json
from scraper import ScraperException
from model import ScrapedYoutubeVideo
from helpers import VideoIDExtractor, VideoIDExtractorError
import logging
import config
import os

logger = logging.getLogger('Youtube2Mp3')

# Initialize the app's configurations
if 'APP_CONFIG' not in os.environ:
    logger.error("Expecting APP_CONFIG environment variable to be set. See README file.", "Error")
    exit(1)

app_config = eval(os.environ['APP_CONFIG'])()
app = Flask(__name__, app_config.STATIC_PATH)


# REST endpoints

@app.route('/api/youtube2mp3', methods=['GET'])
# @validate_query_params(['url'])
def convert_youtube_to_mp3():
    """Gets a URL to Youtube video, scrapes it,
    converts into scraped and returns a URL to download the scraped file.
    :return:
    """
    if 'url' not in request.args:
        return json.dumps({"error": "Missing 'url' query param"}), 400

    try:
        youtube_url = request.args['url']
        video_id = VideoIDExtractor.extract(youtube_url)
        scraped_filename = app_config.scraper.scrape(video_id, app_config.SCRAPING_OUTPUT)
        scraped_video = ScrapedYoutubeVideo(video_id, app_config.HOST + "/downloads/" + scraped_filename)
    except ScraperException:
        return json.dumps({"error": "Failed to scrape the video."}), 500
    except VideoIDExtractorError:
        return json.dumps({"error": "Can't fetch a video ID from the provided URL."}), 400

    return json.dumps(scraped_video.__dict__())


@app.route("/downloads/<string:filename>")
def serve_file(filename):
    return send_from_directory("../static/scraped", filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
