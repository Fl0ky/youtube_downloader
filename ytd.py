from pytube import YouTube

def download_video(url, path):
    yt = YouTube(url)
    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(path)

if __name__ == '__main__':
    url = input("Enter the url of the video to be downloaded: ")
    path = input("Enter the path to save the video: ")
    download_video(url, path)