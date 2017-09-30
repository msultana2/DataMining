from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import time

access_token="781183608543477760-0MAsyQ1sIgB3bAcuHJFmRNDTyY6cgVB"
access_token_secret="oWOGS6GrWwmRAO5qpdsxmCP1D1RC6V8vzyf8jFg1dzOZZ"
consumer_key="35ZxHgE7vJniQZtL77GS3KINJ"
consumer_secret="VJikDUnQs4ku67vKt12CMjYBL4TbWwSq6RlDgOCWqxV8nCGCm1"

class StdoutListener(StreamListener):
    def on_data(self,data):
        try:
            savefile=open("h:\\twitter.txt","a")
            savefile.write(data)
            savefile.write('\n')
            savefile.close()
            return True
        except BaseException as e:
            print ('Failed reading on data',str(e))
            time.sleep(5)

    def on_error(self,status):
        print(status)

I=StdoutListener()
auth=OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
stream=Stream(auth,I)
stream.filter(track=['zika'])
