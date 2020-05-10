#ydl2.py
from __future__ import unicode_literals
import youtube_dl
import logging
import time
from tqdm import tqdm
import config

logging.basicConfig(level=logging.INFO,format='%(asctime)s:%(levelname)s:%(message)s')

def my_hook(d):

    if d['status'] == 'downloading':
        #print(d['speed'])
        #print(d['elapsed'])
        logging.info("ETA : {}".format(d['eta']))

    if d['status'] == 'finished':
        logging.info('Done downloading, now converting ...')
        total_size_of_file = int(d['total_bytes'])
        total_size_of_file_in_MB = total_size_of_file/(1024**2)
        logging.info("Size on disk {} MB".format(total_size_of_file_in_MB))

ydl_opts = {
    'forcetitle': True,
    'quiet' : True,
    'forceduration': True,
    'forcedescription' : False,
    'socket_timeout' : 15,
    'format': 'bestaudio/best',
    'outtmpl': '{}\\%(title)s.%(ext)s'.format(config.AUDIO_OUTPUT),
    'noplaylist' : True,
    'geo_bypass' : True,
    'progress_hooks': [my_hook],
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',

    }]
}

logging.info("Getting the list of urls to download")
URLS_FILE = open("data/urls_audio.txt", "r")
urls_in_file = URLS_FILE.read()
list_of_urls = urls_in_file.split("\n")
list_of_urls_to_download = list_of_urls[config.START_COUNTER:]
URLS_FILE.close()

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    for each_url in tqdm(list_of_urls_to_download):
        try:
            print(each_url)
            logging.info("Downloading {}".format(each_url))
            ydl.download([each_url])
        except:
            logging.info("Could not download {}".format(each_url))
            continue



