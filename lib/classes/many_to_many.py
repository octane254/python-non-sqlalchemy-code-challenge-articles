
class Author:
    def __init__(self, name):
        self._name = None
        self.name = name  # set once; later changes are ignored

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        # name is immutable after it's set once
        if hasattr(self, "_name") and self._name is not None:
            return
        if isinstance(value, str) and len(value) > 0:
            self._name = value

    # Relationships
    def articles(self):
        # all Article instances written by this author
        return [a for a in Article.all if a.author is self]

    def magazines(self):
        # unique magazines this author has written for
        mags = list({a.magazine for a in self.articles()})
        return mags if mags else []

    # Aggregate / association
    def add_article(self, magazine, title):
        # create and return an Article linked to this author
        return Article(self, magazine, title)

    def topic_areas(self):
        # unique categories from magazines the author contributed to
        if not self.articles():
            return None
        return list({m.category for m in self.magazines()})


class Magazine:
    def __init__(self, name, category):
        self._name = None
        self._category = None
        self.name = name
        self.category = category

    # name: mutable, str, length 2..16; ignore invalid assignments
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
        # else ignore

    # category: mutable, non-empty str; ignore invalid assignments
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value
        # else ignore

    # Relationships
    def articles(self):
        return [a for a in Article.all if a.magazine is self]

    def contributors(self):
        # unique authors who have written for this magazine
        authors = list({a.author for a in self.articles()})
        return authors if authors else []

    # Aggregates
    def article_titles(self):
        titles = [a.title for a in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        # authors with > 2 articles in this magazine
        counts = {}
        for a in self.articles():
            counts[a.author] = counts.get(a.author, 0) + 1
        heavy = [author for author, n in counts.items() if n > 2]
        return heavy if heavy else None


class Article:
    # single source of truth for relationships
    all = []

    def __init__(self, author, magazine, title):
        # title: immutable after set; must be str, length 5..50
        self._title = None
        self.title = title  # uses setter that only allows first valid set

        # author and magazine must be correct types; they are mutable later
        self._author = None
        self._magazine = None
        self.author = author
        self.magazine = magazine

        # track every article
        Article.all.append(self)

    # title: read-only after first valid assignment
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        # do nothing if already set (immutable)
        if hasattr(self, "_title") and self._title is not None:
            return
        if isinstance(value, str) and 5 <= len(value) <= 50:
            self._title = value
        # else ignore

    # author: must be Author; mutable
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if isinstance(value, Author):
            self._author = value
        # else ignore

    # magazine: must be Magazine; mutable
    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if isinstance(value, Magazine):
            self._magazine = value
        # else ignore
