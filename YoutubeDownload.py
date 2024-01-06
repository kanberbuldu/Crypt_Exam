import pytube
import os


question = input("Ses Dosyası İçin 's' video Dosyası için 'v' Giriniz: ")

if question == "v" or question == "V":
    url = input("Video Url: ")
    path =""
    pytube.YouTube(url).streams.get_highest_resolution().download(path)

elif question == "s" or question == "S":
    urls = input("Ses url: ")
    path = ""

    pytube.YouTube(urls).streams.get_audio_only().download(path)
    base64,ext
else:
    print("Seçiminiz kontrol edip tekrar deneyiniz.")
