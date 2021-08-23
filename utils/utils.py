import feedparser
import requests
from dateutil.parser import parse
from tqdm import tqdm

# import threading


def get_episodes(feed):  # sourcery skip: merge-dict-assign
    d = feedparser.parse(feed)

    TITLE = d["feed"]["title"]
    AUTHOR = d["feed"]["author"].replace("/", "-")
    FOLDER_NAME = f"{AUTHOR} - {TITLE}"

    episodes = []
    for i in d["entries"]:
        e = {}
        e["title"] = i["title"]
        e["timestamp"] = str(parse(i["published"]).date()).replace("-", "")

        ### extract link
        for link in i["links"]:
            if link["type"] == "audio/mpeg":
                e["url"] = link["href"]

        ### create download path
        file_extension = e["url"].split("?")[0].split(".")[-1]
        filename = e["title"].replace(":", "-")

        e["filename"] = e["timestamp"] + "-" + filename + "." + file_extension

        episodes.append(e)

    ### sort chronologically
    episodes = episodes[::-1]

    return FOLDER_NAME, episodes


# # from https://stackoverflow.com/a/33543751
# def download(link, filelocation):
#     r = requests.get(link, stream=True)
#     with open(filelocation, 'wb') as f:
#         for chunk in r.iter_content(1024):
#             if chunk:
#                 f.write(chunk)

# def createNewDownloadThread(link, filelocation):
#     download_thread = threading.Thread(target=download, args=(link,filelocation))
#     download_thread.start()
#     download_thread.join() # exit only after finishing all threads

# https://gist.github.com/yanqd0/c13ed29e29432e3cf3e7c38467f42f51
def download(url, filelocation):
    resp = requests.get(url, stream=True)
    total = int(resp.headers.get("content-length", 0))
    with open(filelocation, "wb") as file, tqdm(
        total=total,
        unit="iB",
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for data in resp.iter_content(chunk_size=1024):
            size = file.write(data)
            bar.update(size)
