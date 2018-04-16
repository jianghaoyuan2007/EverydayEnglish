from parser import *
from downloader import *
import os


parser = Parser('contents.xml')

book = parser.parse()

destination = str(os.getcwd()) + '/mp3/'

downloader = Downloader(destination, parser.download_links)

downloader.start()
