from nltk.util import ngrams
n=1
sentance='vinay is og'
unigram=ngrams(sentance.split(),n)
for grams in unigram:
    print(grams)