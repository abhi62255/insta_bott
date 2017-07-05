# to get id of user
from constants import BASE_URL,APP_ACCESS_TOKEN
import requests


def get_user_id(insta_username) :
    request_url="%s/users/search?q=%s&access_token=%s" % (BASE_URL,insta_username,APP_ACCESS_TOKEN)
    print "request url is %s" % (request_url)
    user_info=requests.get(request_url).json()

    if user_info['meta']['code'] == 200 :
        if  len(user_info['data']):
            return user_info['data'][0]['id']
        else:
            return None
    else:
        print("Return code is other than 200 recived \n")
        exit()

