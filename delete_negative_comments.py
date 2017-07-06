from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
import requests
from get_users_post import get_users_post
from constants import APP_ACCESS_TOKEN,BASE_URL



def delete_negative_comment(insta_username):
  media_id = get_users_post(insta_username)
  request_url = (BASE_URL + 'media/%s/comments/?access_token=%s') % (media_id, APP_ACCESS_TOKEN)
  print 'GET request url : %s' % (request_url)
  comment_info = requests.get(request_url).json()

  if comment_info['meta']['code'] == 200:
    if len(comment_info['data']):
      print('1')
      # logic to del comment
    else:
      print 'There are no existing comments on the post!'
  else:
    print 'Status code other than 200 received!'