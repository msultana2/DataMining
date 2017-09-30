from nltk.tokenize import TweetTokenizer
tknzr = TweetTokenizer()
f = open('H:\\tweets.txt')
text_file = open('H:\\token_strings.txt', 'w')
tweetarray = []
for lines in f:
    try:
        k = tknzr.tokenize(lines)
        tweetarray.append(k)
    except:
        pass
text_file.write(str(tweetarray))
text_file.close()
    
