#!/usr/bin/env python
import sys
import string
from sklearn.feature_extraction import stop_words

# Define stopwords and punctuation
stopwords = set(stop_words.ENGLISH_STOP_WORDS)
#stopwords = set(['the','and','if'])
punc = set(string.punctuation)

# get all lines from stdin
for line in sys.stdin:
    # remove leading and trailing whitespace and make lowercase
    line = line.strip().lower()

    # split the line into words; splits on any whitespace
    words = line.split()
    
    # output tuples (word, 1) in tab-delimited format
    for word in words:
        # remove punctuation
        for char in word:
            if char in punc:
                word=word.replace(char,"")
        # remove stopwords
        if word not in stopwords:
            print '%s\t%s' % (word, "1")
