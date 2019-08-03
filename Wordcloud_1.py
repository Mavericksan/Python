# This program generates a wordcloud out of a textfile

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

filename = input('Bitte Filenamen der Textdatei zum Generieren der Wordcloud eingeben: ')
#print('Eingegebener Filename: ', filename)

with open(filename) as f:
    text = f.read()

wordcloud = WordCloud(width = 1920, height = 1280)

STOPWORDS.add('said')
STOPWORDS.add('Illustration')

wordcloud.generate(text)
plt.imshow(wordcloud, interpolation= 'bilinear')
plt.axis('off')
plt.show()
