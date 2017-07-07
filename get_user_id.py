# to get id of user
from constants import BASE_URL,APP_ACCESS_TOKEN,insta_username
import requests




def get_user_id(insta_username) :
    insta_username = raw_input("Enter Name of your friend \n")
    request_url="%susers/search?q=%s&access_token=%s" % (BASE_URL,insta_username,APP_ACCESS_TOKEN)
    print "request url is %s" % (request_url)
    user_info=requests.get(request_url).json()

    if user_info['meta']['code'] == 200 :
        if  len(user_info['data']):
            return user_info['data'][0]['id']
        else:
            print "User does not exist \n"
            return None
    else:
        print("Return code is other than 200 recived \n")
        exit()

