from urllib.parse import urlparse, parse_qs


class VideoIDExtractorError(Exception):
    pass


class VideoIDExtractor:
    @staticmethod
    def extract(video_url: str) -> str:
        """
        Gets a URL and extracts Youtube video ID from it.
        In case the URL is invalid or video ID can't be found - raises exception.
        """
        parsed_url = urlparse(video_url)
        if parsed_url.hostname == 'youtu.be':
            return parsed_url.path[1:]
        if parsed_url.hostname in ('www.youtube.com', 'youtube.com'):
            if parsed_url.path == '/watch':
                p = parse_qs(parsed_url.query)
                return p['v'][0]
            if parsed_url.path[:7] == '/embed/':
                return parsed_url.path.split('/')[2]
            if parsed_url.path[:3] == '/v/':
                return parsed_url.path.split('/')[2]

        raise VideoIDExtractorError("Failed to extract video ID from the provided URL")