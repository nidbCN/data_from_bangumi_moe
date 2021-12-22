from json import dumps
import json
import requests
import time

API_BASE = "https://bangumi.moe/api/torrent/"
URL_BASE = "https://bangumi.moe/torrent/"

first_endpoint = "latest"
resp = requests.get(API_BASE + first_endpoint)
page_count = resp.json()["page_count"]
torrents = []

for i in range(1, page_count + 1):
    page_resp = requests.get(API_BASE + f"page/{i}")
    torrent_info_list  = page_resp.json()["torrents"]
    
    bangumi_info_list = []
    
    for item in torrent_info_list:
        bangumi_info_item = {
            "id" : item["_id"],
            "title": item["title"],
            "seeders": item["seeders"],
            "magnet": item["magnet"],
            "size": item["size"],
            "filelist": item["content"],
            "introduction": item["introduction"],
            "url": URL_BASE + item["_id"]
        }
        print(f"{bangumi_info_item['seeders']} UP\t{bangumi_info_item['title']}:\t{bangumi_info_item['url']}\t")
        bangumi_info_list.append(bangumi_info_item)
    
    torrents.append({
        "page": i,
        "bangumi_list": bangumi_info_list 
    })
    
    time.sleep(1)
    
with open("data.json","w", encoding="utf-8") as f:
    json.dump(torrents,f ,ensure_ascii=False)