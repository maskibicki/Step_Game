import nltk
from textblob import TextBlob
from newspaper import Article

nltk.download('punkt')
url = 'https://collider.com/worst-movies-of-all-time-according-to-rotten-tomatoes/#39-ballistic-ecks-vs-sever-39-2002' 
article = Article(url)
article.download()
article.parse()
article.nlp()
text = article.summary
print(text)
blob = TextBlob(text)
sentiment = blob.sentiment.polarity  # -1 to 1
print(sentiment)

'''
url the link thta the thing scans
'''