class Article:
    all = []
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        if not isinstance(title, str):
            raise Exception("Title must be a string")
        if len(title) < 5 or len(title) > 50:            raise Exception("Title must be between 5 and 50 characters")
        self._title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        self._title = title
        
class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Title must be a string")
        if len(name) == 0:
            raise Exception("Name must not be empty")
        self._name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

    def articles(self):
        all_articles = Article.all
        return [article for article in all_articles if article.author == self]

    def magazines(self):
        all_articles = Article.all
        return list(set([article.magazine for article in all_articles if article.author == self]))

    def add_article(self, magazine, title):
        new_article = Article(self, magazine, title)
        return new_article
    def topic_areas(self):
        author_articles = self.articles()

        if not author_articles: 
            return None
        return list(set([article.magazine.category for article in author_articles]))


class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str):
            raise Exception("Title must be a string")
        if len(name) < 2 or len(name) > 16:            
            raise Exception("Title must be between 5 and 50 characters")
        self._name = name


        if not isinstance(category, str):
            raise Exception("Category must be a string")
        if len(category) == 0:
            raise Exception("Category must not be empty")
        self._category = category


    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Title must be a string")
        if len(value) < 2 or len(value) > 16:            
            raise Exception("Title must be between 5 and 50 characters")
        self._name = value


    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise Exception("Category must be a string")
        if len(value) == 0:
            raise Exception("Category must not be empty")
        self._category = value
    def articles(self):    
        all_articles = Article.all
        return [article for article in all_articles if article.magazine == self]

    def contributors(self):
        all_articles = Article.all
        return list(set([article.author for article in all_articles if article.magazine == self]))

    def article_titles(self):
       magazine_articles = [article.title for article in Article.all if article.magazine == self]

       if not magazine_articles: 
           return None
       
       return magazine_articles

    def contributing_authors(self):
        magazine_articles = [article for article in Article.all if article.magazine == self]
        if not magazine_articles:
            return None
        
        author_counts = {}
        for article in magazine_articles:
            if article.author in author_counts:
                author_counts[article.author] += 1
            else:
                author_counts[article.author] = 1
                
        authors_list = [author for author, count in author_counts.items() if count > 2]
        
        # Return None if no authors have written more than 2 articles
        if not authors_list:
            return None
                
        return authors_list