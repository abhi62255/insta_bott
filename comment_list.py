from get_users_post import get_users_post
from constants import insta_username,BASE_URL,APP_ACCESS_TOKEN
import requests


def comment_list() :
    media_id=get_users_post(insta_username)
    request_url = (BASE_URL + 'media/%s/comments/?access_token=%s') % (media_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    comment_info = requests.get(request_url).json()

    comment = []  # List to store comment
    a = 0
    while len(comment_info['data']) > a:
        comment.append(comment_info['data'][a]['text'])
        a = a + 1

    print "Comments  Are \n"
    for temp in comment:
        print temp

    print '\n'
