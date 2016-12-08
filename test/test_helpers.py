from unittest import TestCase
from nose.tools import assert_true
from youtube2mp3.helpers import VideoIDExtractor, VideoIDExtractorError


class TestVideoIDExtractor(TestCase):

    VIDEO_ID = '30AM8K06FJU'
    VALID_YOUTUBE_URLS = [
        'http://youtu.be/30AM8K06FJU',
        'http://www.youtube.com/watch?v=30AM8K06FJU&feature=feedu',
        'http://www.youtube.com/embed/30AM8K06FJU',
        'http://www.youtube.com/v/30AM8K06FJU?version=3&amp;hl=en_US',
        'https://www.youtube.com/watch?v=30AM8K06FJU&list=PL33D3186459758157&index=4']

    def test_when_valid_url_provided_then_return_video_id(self):
        failed_urls = []
        for valid_youtube_url in TestVideoIDExtractor.VALID_YOUTUBE_URLS:
            try:
                extracted_video_id = VideoIDExtractor.extract(valid_youtube_url)
                if extracted_video_id != self.VIDEO_ID:
                    self.fail()
            except VideoIDExtractorError:
                failed_urls.append(valid_youtube_url)

        if failed_urls:
            self.fail("Failed URLs: %s".format(failed_urls))

        assert_true(True)

