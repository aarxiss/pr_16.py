class Book:
    def __init__(self, title, author, content):
        self.title = title
        self.author = author
        self.content = content

    def update_content(self, new_content):
        self.content = new_content


class BookViewer:
    def display(self, book: Book):
        print(f"{book.title} — {book.author}")
        print(book.content)


class BookSaver:
    def save_to_file(self, book: Book):
        with open(f"{book.title}.txt", "w", encoding='utf-8') as f:
            f.write(f"{book.title} — {book.author}\n{book.content}")



book = Book("Кайдашева сім’я", "Іван Нечуй-Левицький", "Це повість про село...")
viewer = BookViewer()
saver = BookSaver()

viewer.display(book)
book.update_content("Оновлений зміст книги")
saver.save_to_file(book)
