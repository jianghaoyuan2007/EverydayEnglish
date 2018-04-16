from parser import *
import os
import urllib.request


class Installer:

    def __init__(self, book, path, name):
        self.book = book
        self.path = path
        self.name = name
        self.current_path = path

    def install(self):
        self.make_dir(self.name)
        self.enter_dir(self.name)
        self.dfs()

    def download(self, url, filename):
        file_path = str(os.path.join(self.current_path, filename))
        if not os.path.exists(file_path):
            print(url, end=' ', flush=True)
            urllib.request.urlretrieve(url, file_path)
            print('✅')

    def make_dir(self, name):
        dir_path = str(os.path.join(self.current_path, name))
        print(dir_path)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

    def enter_dir(self, name):
        self.current_path = str(os.path.join(self.current_path, name))

    def back_to_previous_dir(self):
        self.current_path = os.path.abspath(os.path.join(self.current_path, os.pardir))

    def dfs_visit(self, g, u):
        if u.is_dir:
            self.make_dir(u.name)
            self.enter_dir(u.name)
        else:
            self.download(u.value, u.name)
        for v in list(u.items):
            if not v.visited:
                self.dfs_visit(g, v)
        u.visited = True
        if u.is_dir:
            self.back_to_previous_dir()

    def dfs(self):
        for chapter in list(self.book.items):
            chapter.visited = False
        for chapter in list(book.items):
            if not chapter.visited:
                self.dfs_visit(self.book, chapter)


parser = Parser('contents.xml')

book = parser.parse()

path = str(os.getcwd())

installer = Installer(book, path, book.name)

installer.install()