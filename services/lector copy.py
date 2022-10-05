import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import *
from nltk.stem.porter import PorterStemmer

text = ''

def chapter_to_str(chapter):
    global text
    soup = BeautifulSoup(chapter.get_body_content(), 'html.parser')
    text+=(' '.join([para.get_text() for para in soup.find_all('p')]))

book = epub.read_epub('El_laberinto_de_los_espiritus.epub')

for chapter in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
    chapter_to_str(chapter)

# Parseo
stop_words = set(stopwords.words('spanish'))
  
word_tokens = word_tokenize(text.lower())
word_tokens = [w for w in word_tokens if w.isalpha() or w.isnumeric()]
word_tokens = [w for w in word_tokens if not w.lower() in stop_words]
# word_tokens = [PorterStemmer().stem(w) for w in word_tokens]

fdist=FreqDist(word_tokens)
print(fdist.most_common(23))

bgs = bigrams(word_tokens)
fdist = FreqDist(bgs)
print(fdist.most_common(23))

tbgs = trigrams(word_tokens)
fdist = FreqDist(tbgs)
print(fdist.most_common(23))
