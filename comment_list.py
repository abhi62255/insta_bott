from get_users_post import get_users_post
from constants import insta_username,BASE_URL,APP_ACCESS_TOKEN
import requests
                            # Importing functions and constants from other files


def comment_list() :        # Function defination
    media_id=get_users_post(insta_username)             # Calling of get_users_post90 function
    request_url = (BASE_URL + 'media/%s/comments/?access_token=%s') % (media_id, APP_ACCESS_TOKEN)      # Making URL to request
    print 'GET request url : %s' % (request_url)
    comment_info = requests.get(request_url).json()             # Making the request and storing input in jason object form

    comment = []  # List to store comment
    a = 0
    while len(comment_info['data']) > a:
        comment.append(comment_info['data'][a]['text'])         # Adding comments in list
        a = a + 1

    print "Comments  Are :"
    for temp in comment:
        counter = 1
        print str(counter) + ") "+str(temp)         # Geting output as comments of the post
        counter = counter+1

    print '\n'
