# to get info of our self
import requests
from constants import BASE_URL,APP_ACCESS_TOKEN

def self_info():
    request_url="%susers/self/?access_token=%s"% (BASE_URL,APP_ACCESS_TOKEN)
    print "request url is %s" % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200 :
        if len(user_info['data']):
            print "Username : %s" % (user_info['data']['username'])
            print "Number of posts : %s" % (user_info['data']['counts']['media'])
            print "Followed by : %s " % (user_info['data']['counts']['followed_by'])
            print "Follows : %s" % (user_info['data']['counts']['follows'])
        else:
            print("User does not exist \n")
    else:
        print "Status code other than 200 received \n"
