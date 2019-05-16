#!/usr/bin/env python
import sys
#from sklearn.feature_extraction import stop_words

# get all lines from stdin
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    
    # make text all lowercase
    line = line.strip().lower()

    # split the line into words; splits on any whitespace
    words = line.split()
    
    # remove punctuation from words
    #punc = set(string.punctuation)
    #words = ''.join(char for char in words not in punc)
    
    #remove the stopwords
   # stopwords = set(stop_words.ENGLISH_STOP_WORDS)
     
    # for word in words:
     #  if word not in stopwords:
      #     print word

    # output tuples (word, 1) in tab-delimited format
    for word in words:
        print '%s\t%s' % (word, "1")
