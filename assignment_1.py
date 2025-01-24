# Parent Class: Book
class Book:
    def __init__(self, title, author, genre, pages):
        """
        Constructor to initialize a Book object.
        
        """
        self.title = title
        self.author = author
        self.genre = genre
        self.pages = pages
    
    def describe(self):
        """ a summary of the book."""
        return f"'{self.title}' by {self.author} is a {self.genre} book with {self.pages} pages."
    
    def read(self, pages_read):
        """
        Simulates reading the book.
        
        """
        if pages_read > self.pages:
            return f"You can't read more than {self.pages} pages!"
        return f"You have read {pages_read} pages of '{self.title}'. Keep going!"

# Child Class: EBook
class EBook(Book):
    def __init__(self, title, author, genre, pages, file_size):
        """
        Constructor to initialize an EBook object.

        """
        super().__init__(title, author, genre, pages)
        self.__file_size = file_size  # Encapsulation: Private attribute
    
    def get_file_size(self):
        """Returns the file size of the eBook."""
        return f"The file size of '{self.title}' is {self.__file_size} MB."
    
    def download(self):
        """ downloading the eBook."""
        return f"Downloading '{self.title}'... File size: {self.__file_size} MB."

# Test the Classes
if __name__ == "__main__":
    # Create a regular book
    book = Book("To Kill a Mockingbird", "Harper Lee", "Fiction", 281)
    print(book.describe())
    print(book.read(50))
    print(book.read(300))  # Trying to read more pages than available

    print("\n")

    # Create an eBook
    ebook = EBook("Atomic Habits", "James Clear", "Self-help", 320, 1.2)
    print(ebook.describe())
    print(ebook.get_file_size())
    print(ebook.download())
    print(ebook.read(100))
