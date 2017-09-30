import json
tweetfile=open('H:\\twitter.txt')
tweetfiles=open('H:\\tweets.txt','w')
for lines in tweetfile:
    if lines.isspace():
        continue
    try:
        tweetjson=json.loads(lines)
        if tweetjson['lang'] == 'en':
            tweettext=str(tweetjson['text'].encode('utf-8')).replace('\n','')
            tweetfiles.write(tweettext+'\n')
    except:
        pass
tweetfiles.close()
