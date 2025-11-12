class Book:
    """
    A class representing a book with title, author, and publication year.
    Demonstrates Python magic methods: __init__, __del__, __str__, and __repr__.
    """

    def __init__(self, title, author, year):
        """
        Constructor that initializes the book's attributes.
        """
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """
        Destructor that prints a message when the object is deleted.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        User-friendly string representation of the Book object.
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Official string representation that can recreate the object.
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"
