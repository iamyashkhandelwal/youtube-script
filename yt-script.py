from pytube import YouTube  
from pytube import Playlist

DOWNLOAD_PATH = "D:/Yash/youtube-downloads";
# PlaylistURL = 'https://youtube.com/playlist?list=PLC3y8-rFHvwiNfZK3QmKLnrPcSAX32INO';


def downloadPlaylistVideos(playlistUrl, downloadPath = DOWNLOAD_PATH):
    playlist = Playlist(playlistUrl)
    print('Number of videos in playlist: %s' % len(playlist.video_urls))
    # Loop through all videos in the playlist and download them
    for video in playlist.videos:
        video.streams.filter(res="720p").first().download(downloadPath)
    print('Videos downloaded!')  


# downloadPlaylistVideos("https://www.youtube.com/watch?v=hGuwdn9mHnc&list=PLJUTYXGp-CH4zDSPpDgOvDHf2Q4XD-Zqu")

def downloadVideo(videoURL, downloadPath = DOWNLOAD_PATH):
    youtubeObject = YouTube(videoURL)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download(downloadPath)
    except:
        print("An error has occurred")
    print("Video downloaded!")

# downloadVideo("https://youtu.be/k9j5yPuQ2TA")