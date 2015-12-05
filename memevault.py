import facebook 
import requests # Used for paging
import urllib

# Refer to the included file 'config.py'
from config import *

if __name__ == '__main__':
	
	# Graph API instance.
	graph = facebook.GraphAPI(access_token = access_token)
	
	# We generate an object that stores the contents of our group's feed. 
	# groupId is set in the config
	groupFeed = graph.get_connections(id=groupId, connection_name='feed')
	
	while(True):
		
		try:
			# Attempt to iterate over posts in our group's feed.
			for post in groupFeed['data']:
				try:
					# Concatenate our desired directory (set in config) with the time the post was created (in a string)
					# 	and our desired file type (jpg)
					path = directory + "/" + str(post['created_time']) + ".jpg"
					
					# We use the urlretrieve method to download our image from a given url
					# post['picture'] is the url to a thumbnail of any picture generated 
					# 	for a post (could be a keyframe to an embedded video)
					urllib.urlretrieve(post['picture'], path)

				except:
					print "The content is either not a picture or cannot be downloaded"

			# This grabs us the following paging for the group. Allowing us to parse all of the group's feed
			# and not just the recent most posts.
			groupFeed = requests.get(groupFeed['paging']['next']).json()

		except:
			print "There are no additional posts in the feed."