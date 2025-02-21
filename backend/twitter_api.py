import tweepy

# Twitter API credentials (replace with your keys)
API_KEY = "your_api_key"
API_SECRET = "your_api_secret"
ACCESS_TOKEN = "your_access_token"
ACCESS_SECRET = "your_access_secret"

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

def post_to_twitter(image_path, caption="Here is my resized image!"):
    api.update_status_with_media(status=caption, filename=image_path)
