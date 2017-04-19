#/usr/bin/python
 # -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function

from PIL import Image
import tweepy
import random
from random import randint
import datetime
import pollster

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


with open('cred.txt') as f:
	cred = f.read().splitlines()

consumer_key = cred[0]
consumer_secret = cred[1]
access_token = cred[2]
access_token_secret = cred[3]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

tw_api = tweepy.API(auth)

# STREAMING STUFF





# # for testing
status = tw_api.get_status(854402046367326210)
# rate = 20.0


# keep_length = int(len(status.text) * (rate / 100.0))
# total_length = len(status.text)
# redact_length = total_length - keep_length

# # █ ⓐ
 
# start = randint(0,redact_length)
# end = start + keep_length


# keep_string = status.text[start:keep_length]
# text = status.text.encode('utf-8')
# keep_string = text[start:end]
# print(keep_string)

# padleft = start
# padright = total_length - end
# new_status = 'ⓐ🅿🅾🆃🆄🆂:' + ('█' * padleft) + str(keep_string) + ('█' * padright)

# new_status.replace("@","ⓐ")

# print(new_status)

# pollstuff



def get_polls():
	p_api = pollster.Api()
	chart = p_api.charts_slug_get('donald-trump-favorable-rating')

	approve = chart.pollster_estimates[0].values['hash']['Favorable']
	disapprove = chart.pollster_estimates[0].values['hash']['Unfavorable']
	undecided = chart.pollster_estimates[0].values['hash']['Undecided']

	polls = [approve,disapprove,undecided]

	return polls

polls = get_polls()

print(polls)
# Streaming Stuff:

# class StdOutListener(StreamListener):
#     ''' Handles data received from the stream. '''
 
#     def on_status(self, status):
#         # Prints the text of the tweet
#         # print('Tweet text: ' + status.text)
 
#         # There are many options in the status object,
#         # hashtags can be very easily accessed.
#         for hashtag in status.entities['hashtags']:
#             print(hashtag['text'])
 
#         return True
 
#     def on_error(self, status_code):
#         print('Got an error with status code: ' + str(status_code))
#         return True # To continue listening
 
#     def on_timeout(self):
#         print('Timeout...')
#         return True # To continue listening
 
# if __name__ == '__main__':
#     listener = StdOutListener()
#     auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#     auth.set_access_token(access_token, access_token_secret)
 
#     stream = Stream(auth, listener)
#     stream.filter(follow=['822215679726100480,25073877'])




def partimage(image):
	# the rate at which to blank out the image
	rate = 60;
	grid = 25;
	# open the image
	im = Image.open(image)

	# how wide should the blank spots be? Default is 10%
	gridX = int(round(im.size[0] / grid))
	gridY = int(round(im.size[1] / grid))

	# make the white rectangle
	stamp = Image.new("RGB",(gridX,gridY), "white")

	# work through the grid
	for x in range(0,grid):
		for y in range (0,grid):	

			# blank out 'rate'% of spots
			if (randint(0,100) < rate):
				im.paste(stamp,(x * gridX,y * gridY))


	# note: this will overrite anything else here already
	im.save("new-potus.jpg")


