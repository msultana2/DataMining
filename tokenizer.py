from nltk.tokenize import TweetTokenizer
tknzr = TweetTokenizer()

file = open('H:\\Fight_Zika_class.txt')
text_file = open('H:\\token_Fight_Zika_class.txt', 'w')
freq_file = open('H:\\freq_Fight_Zika_class.txt', 'w')
tweetarray = []
wordfreq = {}
for lines in file:
    try:
        k = tknzr.tokenize(lines)
        tweetarray.append(k)
    except:
        pass
for line in tweetarray:
    for word in line:
        word=word.lower()
        if word in wordfreq:
            wordfreq[word] = wordfreq[word]+1
        else:
            wordfreq[word] = 1

#print("List\n" + str(tweetarray) + "\n")
#print("Frequencies : \n" + str(wordfreq) + "\n")

text_file.write(str(tweetarray))
freq_file.write(str(wordfreq))
text_file.close()
freq_file.close()









