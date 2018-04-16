import os
import urllib.request


class Downloader:

    def __init__(self, destination, links):
        self.destination = destination
        self.links = links
        self.downloadable = False

    def start(self):
        self.downloadable = True
        for link in self.links:
            if self.downloadable:
                self.download(link)
            else:
                return
        print("completed.")

    def pause(self):
        self.downloadable = False

    def download(self, link):
        filename = os.path.basename(os.path.normpath(link))
        file_path = str(self.destination) + filename
        if not os.path.exists(file_path):
            print(link, end=' ', flush=True)
            urllib.request.urlretrieve(link, file_path)
            print('✅')
