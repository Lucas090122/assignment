class Publication:
    def __init__(self, name):
        self.name = name


class Book(Publication):
    def __init__(self, name, author, page_count):
        self.author =  author
        self.page = page_count
        super().__init__(name)

    def print_information(self):
        print(f'Book name: {self.name}, author: {self.author}, '
              f'page count: {self.page} pzges.')
        return


class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        print(f'Magazine name: {self.name}, chief editor: {self.chief_editor}.')
        return


#main program
magazine_1 = Magazine('Donald Duck', 'Aki Hyyppä')
book_1 = Book('Compartment No. 6', 'Rosa Liksom', 192)
magazine_1.print_information()
book_1.print_information()