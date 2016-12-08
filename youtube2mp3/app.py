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
    pass


@app.route("/downloads/<string:filename>")
def serve_file(filename):
    return send_from_directory("../static/scraped", filename)

if __name__ == '__main__':
    app.run()
