# lib/article.py
class Article():
    all = []  # single source of truth

    def __init__(self, author, magazine, title):
        # validate title
        if not isinstance(title, str):
            raise TypeError("Title must be a string")
        if not (5 <= len(title) <= 50):
            raise ValueError("Title must be between 5 and 50 characters")

        # validate author
        from .author import Author
        if not isinstance(author, Author):
            raise TypeError("Author must be an instance of Author")

        # validate magazine
        from .magazine import Magazine
        if not isinstance(magazine, Magazine):
            raise TypeError("Magazine must be an instance of Magazine")

        self._title = title
        self.author = author
        self.magazine = magazine
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    # author property
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        from .author import Author
        if not isinstance(value, Author):
            raise TypeError("Author must be an instance of Author")
        self._author = value

    # magazine property
    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        from .magazine import Magazine
        if not isinstance(value, Magazine):
            raise TypeError("Magazine must be an instance of Magazine")
        self._magazine = value
