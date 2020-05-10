from __future__ import unicode_literals
import youtube_dl
from tqdm import tqdm
import config
import logging

ydl_opts = {'outtmpl': '{}\\%(title)s.%(ext)s'.format(config.VIDEO_OUTPUT)}

logging.info("Getting the list of urls")
with open(config.URLS_FILE_VIDEO, "r") as url_list:
    file_contents = url_list.read()

# To start from a particular counter if neccessary
list_of_urls = file_contents.split("\n")[config.START_COUNTER:]


with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    for each_url in tqdm(list_of_urls):
        try:
            ydl.download([each_url])
        except:
            print("Could not download {}".format(each_url))
            continue
