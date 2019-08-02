# This program generates a wordcloud out of a textfile

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

with open('alice_wonderland.txt') as f:
    text = f.read()

wordcloud = WordCloud(width = 1920, height = 1280)

STOPWORDS.add('said')
STOPWORDS.add('Illustration')

wordcloud.generate(text)
plt.imshow(wordcloud, interpolation= 'bilinear')
plt.axis('off')
plt.show()
