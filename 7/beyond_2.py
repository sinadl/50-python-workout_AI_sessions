import re

article = "Alice Johnson wrote this paper with Bob Smith. Later, Carol Lee reviewed the final draft."
authors = ["Alice Johnson", "Bob Smith", "Carol Lee"]

def remove_article_words(article,authors):
    result = []
    tmp_article = article.split()
    for letter_index,article_word in enumerate(tmp_article):
        for author_word in authors:
            article_word = article_word = re.sub(r'[^\w\s]', '', article_word)
            if article_word.lower() in author_word.lower():
                mask = "_" * len(article_word)
                article = article.replace(article_word,mask)
                
    return article
print(remove_article_words(article,authors))