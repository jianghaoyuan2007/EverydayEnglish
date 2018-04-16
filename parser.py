import xml.etree.ElementTree as ET


class Item:

    def __init__(self, name, value, items, is_dir=False):
        self.name = name
        self.value = value
        self.items = items
        self.is_dir = is_dir
        self.visited = False


class Parser:

    picture_dictionary_index = 1

    def __init__(self, xml):
        self.xml = xml
        self.book = ET.parse(xml).getroot()
        self.url = self.book.attrib['url']
        self.download_links = []

    def parse(self):

        book_name = self.book.attrib['name']
        book_item = Item(book_name, '', [], is_dir=True)

        chapters = list(self.book)
        for c_index, chapter in enumerate(chapters):

            chapter_index = c_index + 1
            chapter_name = 'Chapter {0:0=2d} {1}'.format(chapter_index, chapter.attrib['name'])
            chapter_item = Item(chapter_name, '', [], is_dir=True)
            book_item.items.append(chapter_item)

            picture_dictionary_link = self.picture_dictionary_link(chapter_index)
            picture_dictionary_item = Item('Picture Dictionary.mp3', picture_dictionary_link, [])
            chapter_item.items.append(picture_dictionary_item)

            self.download_links.append(picture_dictionary_link)

            units = list(chapter)
            for u_index, unit in enumerate(units):

                unit_index = u_index + 1
                unit_name = 'Unit {0:0=2d} {1}'.format(unit_index, unit.text)
                unit_item = Item(unit_name, '', [], is_dir=True)
                chapter_item.items.append(unit_item)

                dialogue_name = 'Dialogue.mp3'
                dialogue_link = self.dialogue_link(chapter_index, unit_index)
                dialogue_item = Item(dialogue_name, dialogue_link, [])
                unit_item.items.append(dialogue_item)
                self.download_links.append(dialogue_link)

                useful_expressions_name = 'Useful Expressions.mp3'
                useful_expressions_link = self.useful_expressions_link(chapter_index, unit_index)
                useful_expressions_item = Item(useful_expressions_name, useful_expressions_link, [])
                unit_item.items.append(useful_expressions_item)
                self.download_links.append(useful_expressions_link)
        return book_item

    def download_link(self, chapter, index):
        filename = '{0:0=2d}-{1:0=2d}.mp3'.format(chapter, index)
        return self.url + filename

    def picture_dictionary_link(self, chapter):
        return self.download_link(chapter, Parser.picture_dictionary_index)

    def dialogue_link(self, chapter, unit):
        index = Parser.picture_dictionary_index + (unit - 1) * 2 + 1
        return self.download_link(chapter, index)

    def useful_expressions_link(self, chapter, unit):
        index = Parser.picture_dictionary_index + unit * 2
        return self.download_link(chapter, index)


