from get_user_id  import get_user_id
from constants import BASE_URL,APP_ACCESS_TOKEN
import requests

def get_user_info(insta_username):
    user_id=get_user_id(insta_username)
    if user_id == None :
        print("User does not exist \n")
        exit()

    request_url='%s/users/%s/?access_token=%s' % (BASE_URL,user_id,APP_ACCESS_TOKEN)
    print "Request URL is %s" %(request_url)
    user_info=requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if user_info['data']:
            print "Username is : %s" % (user_info['data']['username'])
            print "Number of Posts : %s" % (user_info['data']['counts']['media'])
            print "Followed by : %s" % (user_info['data']['counts']['followed_by'])
            print "Follows : %s" % (user_info['data']['counts']['follows'])
        else:
            print "user  does not exist \n"
    else:
        print "Status code other than 200 recived \n"


