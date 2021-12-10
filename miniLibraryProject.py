class Library:
    dic = {}
    def __init__(self, books, name):
        self.books = books
        self.lib_name = name

    def display(self):
        print(self.lib_name)

    def retu(self):
        pass

    def add(self):
        pass

    def lend(self):
        pass



if __name__ == '__main__':
    aakash = Library(["Python", "Java"], "Aakash")
    inpu = input("Welcome To The Aakash Library")
