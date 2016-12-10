Youtube2mp3
===========
A slim API which allows to convert Youtube videos to mp3.


Requirements
============
- [youtube-dl](https://github.com/rg3/youtube-dl)
- [virtualenv](https://github.com/pypa/virtualenv)


Quick Start
==========

First steps
-----------
    $ make init         # Initialize virtualenv and install requirements
    $ make test         # Run unit tests
    $ make run-in-dev   # Run the application (default port: 5000)
    
    # Request to extract an audio as mp3 from Youtube video
    $ curl -XGET http://127.0.0.1:5000/api/youtube2mp3?url=https://youtu.be/2XEgvGh4QoE
    
    # Download the extracted audio track
    $ curl -XGET http://127.0.0.1:5000/downloads/2XEgvGh4QoE.mp3

Running in production
-----------
    $ make init
    $ make run-in-prod

REST API Outline
================

Extract audio track from Youtube video
----
**Path:** /api/youtube2mp3?url={youtube-video-url}

**Method:** GET 

**Query Params:**

    url: (Mandatory, String) A valid Youtube video URL.
    
**Success Response:**

  * **Code:** 200 <br />
    **Content:** `{ video_id : "2XEgvGh4QoE", download_url : "http://domain.com/downloads/2XEgvGh4QoE.mp3" }`
    
__Example:__

    GET http://127.0.0.1:5000/api/youtube2mp3?url=https://www.youtube.com/watch?v=2XEgvGh4QoE
    
    
Download the extracted audio track
----

**Path:** /downloads/{:audio-filename}

**Method:** GET 

**URL Params:**

    audio-id: (String) An audio file's name to be served (e.g. 2XEgvGh4QoE.mp3)
    

Author: Yuri Kroz
