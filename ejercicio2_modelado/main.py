class Book:
    def __init__(self, title, genre, price):
        self.title = title
        self.genre = genre
        self.price = price

    def __str__(self):
        return f"{self.title} - {self.genre} - ${self.price}"

class Shelf:
    def __init__(self, capacity):
        self.capacity = capacity
        self.books = []

    def add_book(self, book):
        if len(self.books) < self.capacity:
            self.books.append(book)
        else:
            print("Estante lleno.")

    def count_books(self):
        return len(self.books)

    def percent_full(self):
        return (len(self.books) / self.capacity) * 100

    def total_value(self):
        return sum(book.price for book in self.books)

    def most_expensive_book(self):
        if not self.books:
            return None
        return max(self.books, key=lambda b: b.price)

    def books_alphabetical(self):
        return sorted(self.books, key=lambda b: b.title)

    def books_by_genre(self, genre):
        return [book for book in self.books if book.genre.lower() == genre.lower()]

# Ejemplo de uso
if __name__ == "__main__":
    libro1 = Book("El Principito", "Fábula", 1500)
    libro2 = Book("Cien Años de Soledad", "Realismo Mágico", 3500)
    libro3 = Book("Harry Potter", "Fantasía", 2800)
    libro4 = Book("El Señor de los Anillos", "Fantasía", 4000)

    estante = Shelf(capacity=5)
    estante.add_book(libro1)
    estante.add_book(libro2)
    estante.add_book(libro3)
    estante.add_book(libro4)

    print("Cantidad de libros:", estante.count_books())
    print("Porcentaje de llenado:", estante.percent_full(), "%")
    print("Valor total:", estante.total_value())
    print("Libro más caro:", estante.most_expensive_book())
    print("Libros ordenados alfabéticamente:")
    for libro in estante.books_alphabetical():
        print("-", libro)
    print("Libros de género 'Fantasía':")
    for libro in estante.books_by_genre("Fantasía"):
        print("-", libro)
