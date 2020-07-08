import tweepy 
import time
from keys import *

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

mentions=api.mentions_timeline()
print("=====================================================================\n=====================================================================")

FILE_NAME='last_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply():
	import time
	print("current tweets:")
	try:
		last_seen_id=retrieve_last_seen_id(FILE_NAME)
		mentions=api.mentions_timeline(last_seen_id,tweet_mode='extended')
	except:
		mentions=api.mentions_timeline(tweet_mode='extended')
	intro=""
	tweetTime=""
	for mention in reversed(mentions):
	 	print(str(mention.id)+'--'+mention.full_text)
	 	store_last_seen_id(mention.id,FILE_NAME)
	 	if "hello" in mention.full_text.lower() or "hi" in mention.full_text.lower() or "hey" in mention.full_text.lower():
	 		intro=" Greetings!" 
	 		print("found hello!")
	 	if "the time" in mention.full_text.lower():
	 		print("found time!")
	 		tweetTime= "The current time and date is: "+time.ctime()+" EST"
	 	if  tweetTime or intro:
	 		print("replying...")
	 		api.update_status(intro+" "+tweetTime, mention.id)
	 		hello=""
	 		tweetTime=""

            
while True:
    reply()
    time.sleep(15)

	
