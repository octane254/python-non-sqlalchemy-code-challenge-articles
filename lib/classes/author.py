# lib/author.py
class Author():
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if len(name.strip()) == 0:
            raise ValueError("Name must be longer than 0 characters")
        self._name = name
        # single source of truth lives in Article class

    @property
    def name(self):
        return self._name

    # Relationships
    def articles(self):
        from .article import Article
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    # Aggregates
    def add_article(self, magazine, title):
        from .article import Article
        return Article(self, magazine, title)

    def topic_areas(self):
        if not self.articles():
            return None
        return list(set(mag.category for mag in self.magazines()))
