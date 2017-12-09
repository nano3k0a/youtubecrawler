from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser

DEVELOPER_KEY = "AIzaSyDbdq8npbqef2Iw2Bz51bRMgIKoy2e5nxU"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
VIDEO_ITEM = "youtube#video"
CHANNEL_ITEM = "youtube#channel"
PLAYLIST_ITEM = "youtube#playlist"

def getYouTube():
    return build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

def buildOptions():
    argparser.add_argument("--q", help="Search term", default="Google")
    argparser.add_argument("--max-results", help="Max results", default=25)
    args = argparser.parse_args()
    return args

def search(options, youtube):
    search_response = youtube.search().list(
        q=options.q,
        part="id,snippet",
        maxResults=options.max_results).execute()
    videos = []
    channels = []
    playlist = []

    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == VIDEO_ITEM:
            """
            videos.append("%s(%s)" %(search_result["snippet"]["title"],
                                     search_result["id"]["videoId"]))
            """
            videos.append(search_result)
    return videos

def main():
    youtube = getYouTube()
    videos = search(buildOptions(), youtube)
    for video in videos:
        print(video)

if __name__ == "__main__":
    main()
