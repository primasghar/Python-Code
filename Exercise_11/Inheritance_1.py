# Implement the following class hierarchy using Python: A publication can be either a book or a magazine.
# Each publication has a name. Each book also has an author and a page count, whereas each magazine has a chief editor.
# Also write the required initializers to both classes. Create a print_information method to both subclasses
# for printing out all information of the publication in question. In the main program, create publications Donald Duck
# (chief editor Aki Hyyppä) and Compartment No. 6 (author Rosa Liksom, 192 pages). Print out all information of both
# publications using the methods you implemented.


class Publication:
    def __init__(self,publication_name):
        self.publication_name = publication_name

    def print_information(self):
        print(f"The publication is {self.publication_name}.")


class Magazine(Publication):

    def __init__(self, publication_name, chief_editor):
        self.chief_editor = chief_editor
        super().__init__(publication_name)

    def print_information(self):
        super().print_information()
        print(f"It's Chief Editor is {self.chief_editor}")

class Book(Publication):

    def __init__(self, publication_name, author, page_count):
        self.author = author
        self.page_count = page_count
        super().__init__(publication_name)

    def print_information(self):
        super().print_information()
        print(f"This book is written by {self.author} and it has {self.page_count} pages.")


publication_1 = Magazine("Donald Duck",  "Aki Hyyppä" )
publication_2 = Book("Compartment No. 6",  "Rosa Liksom", 192 )

publication_1.print_information()
publication_2.print_information()