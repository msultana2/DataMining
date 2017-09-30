from nltk.tokenize import TweetTokenizer
tknzr = TweetTokenizer()

file = open('H:\\Health_Concern_class.txt')
#text_file = open('H:\\token_Spread_threat_class.txt', 'w')
freq_file = open('H:\\freq_Health_Concern_class.txt', 'w')
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

#popular_words = sorted(wordfreq, key = wordfreq.get, reverse = True)
#for i in range(min(30, len(popular_words))):
    #print(str(popular_words[i]))

valueDict = {}
for key in wordfreq.keys():
    if wordfreq[key] in valueDict:
        valueDict[wordfreq[key]].append(key)
    else:
        valueDict[wordfreq[key]] = [key]

sortedKeys = sorted(valueDict.keys(), reverse=True)

printed = 0 #counter variable
for key in sortedKeys:
    for token in valueDict[key]:
        print (token, key)
        printed+=1
        
        if printed>=50:
            break    
    if printed >= 50:
        break

#print("List\n" + str(tweetarray) + "\n")
#print("Frequencies : \n" + str(wordfreq) + "\n")

#text_file.write(str(tweetarray))
freq_file.write(str(wordfreq))
#text_file.close()
freq_file.close()









