from nltk.tokenize import TweetTokenizer
tknzr = TweetTokenizer()
tweetfile=open('H:\\Tweets.txt')
file_write=open('H:\\attribute.csv', 'w')
file_write.write('health_attr,spread_attr,fight_attr\n')
health = ['brain', 'admits', 'deformities', 'america', 'cause']
spread = ['health','officials','virus','disease','authorities','public','stay']
fight = ['zika','fight','brazil','mosquitoes','colombia','army','bacteria','mosquito_borne','scientists']


for lines in tweetfile:
    wordlist = tknzr.tokenize(lines)
    hsf=[0,0,0]
    for wrds in wordlist:
        if wrds.lower() in health:
            hsf[0]=1
        if wrds.lower() in spread:
            hsf[1]=1
        if wrds.lower() in fight:
            hsf[2]=1
    file_write.write(str(hsf[0])+','+str(hsf[1])+ ','+ str(hsf[2])+'\n')

file_write.close()
