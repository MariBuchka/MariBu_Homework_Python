from book import Book

# Создание экземпляров класса
library = [
        Book("War and Peace", "Leo Tolstoy"),
        Book("Гарри Поттер и Орден Феникса", "Джоан Кэтлин Роулинг"),
        Book("Гордость и предубеждение", "Джейн Остен")
]

# Цикл, печатающий библиотеку
for book in library:
    print(f"{book.title} - {book.author}")
