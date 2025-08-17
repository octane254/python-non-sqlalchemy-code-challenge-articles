# lib/magazine.py
class Magazine():
    def __init__(self, name, category):
        self.name = name
        self.category = category

    # name property
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if not (2 <= len(value) <= 16):
            raise ValueError("Name must be between 2 and 16 characters")
        self._name = value

    # category property
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise TypeError("Category must be a string")
        if len(value.strip()) == 0:
            raise ValueError("Category must be longer than 0 characters")
        self._category = value

    # Relationships
    def articles(self):
        from .article import Article
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    # Aggregates
    def article_titles(self):
        if not self.articles():
            return None
        return [article.title for article in self.articles()]

    def contributing_authors(self):
        authors = []
        for author in self.contributors():
            count = len([a for a in self.articles() if a.author == author])
            if count > 2:
                authors.append(author)
        return authors if authors else None
