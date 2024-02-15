import yt_dlp

url = input("Enter the Youtube Link")

ydl_opts = {}

with yt_dlp.YoutubeDL(ydl_opts) as file:
  file.download([url])

print("Your Video Downloaded Successfully")
