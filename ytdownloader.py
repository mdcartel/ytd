from pytube import Youtube
link = input('enter video URL')
yt = Youtube(link)
downloader = yt.streams.get_highest_resolution()
print('download in progress...')
downloader.download(filename='video_download.mp4')
print('download done')