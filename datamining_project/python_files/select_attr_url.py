from nltk.tokenize import TweetTokenizer
tknzr = TweetTokenizer()
tweetfile=open('H:\\Tweets.txt')
file_write=open('H:\\attribute_url.csv', 'w')
file_write.write('@_attr,#_attr,url_attr\n')

for lines in tweetfile:
    wordlist = tknzr.tokenize(lines)
    hsf=[0,0,0]
    for wrds in wordlist:
        if '@' in wrds:
            hsf[0] += 1
        if '#' in wrds:
            hsf[1] += 1
        if 'http' in wrds:
            hsf[2] += 1
    file_write.write(str(hsf[0])+','+str(hsf[1])+ ','+ str(hsf[2])+'\n')

file_write.close()
