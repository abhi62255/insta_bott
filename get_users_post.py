from get_user_id import get_user_id
import requests
import urllib
from constants import BASE_URL,APP_ACCESS_TOKEN


def get_users_post(insta_username) :
    user_id=get_user_id(insta_username)
    if user_id == None :
        print "User does not exist \n"
        exit()
    request_url='%susers/%s/media/recent/?access_token=%s' % (BASE_URL,user_id,APP_ACCESS_TOKEN)
    print "GET request URL is %s" % (request_url)
    user_media=requests.get(request_url).json()

    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            image_name = user_media['data'][0]['id'] + '.jpeg'
            image_url = user_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            return user_media['data'][0]['id']
        else:
            print "User does not exists \n"
    else:
        print "Status code other than 200 recived \n"
        return None