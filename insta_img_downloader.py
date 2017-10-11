import urllib
from urllib.request import urlopen, urlretrieve
import argparse
from json import load
import os
import re

def make_folder():
    if not os.path.isdir(args.username):
        os.makedirs(args.username)

def download_images():
    request_url = "https://www.instagram.com/"+args.username+"/media/"

    try:
        json_obj = urlopen(request_url)
    except:
        print("Invalid username!")

    data = load(json_obj)
    make_folder()
    for content in data["items"]:
        file_url = content["images"]["standard_resolution"]["url"]
        
        file_name = file_url.replace("https://scontent-arn2-1.cdninstagram.com/","")
        file_name = file_name.replace("https://instagram.fsvg1-1.fna.fbcdn.net/","")
        
        path = 's2onlyone1'+"/"+re.split('/', file_name)[-1]
        urlretrieve(file_url,path)
        print("Downloaded: "+path)

def make_folder():
    if not os.path.isdir(args.username):
        os.makedirs(args.username)
        
        
if __name__ == "__main__" :
    parser = argparse.ArgumentParser(description='Instagram Image Downloader')
    parser.add_argument('-u', '--username', type=str, metavar='', required=True, help='The username of the the instagram account')
    args = parser.parse_args()
    download_images()
    
    
    
    
    
    
    
    
    
    