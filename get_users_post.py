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
            choice = 1
            while True:
                choice = int(raw_input(" 1) To get recent Post id \n 2) To get Max liked post ID\n 3) To get Min liked photo \n 4) To exit \n ENTER YOUR CHOICE : "))
                if choice == 1:
                    image_name = user_media['data'][0]['id'] + '.jpeg'
                    image_url = user_media['data'][0]['images']['standard_resolution']['url']
                    urllib.urlretrieve(image_url, image_name)
                    return user_media['data'][0]['id']
                elif choice == 2:
                    count = 1
                    max_like_id = user_media['data'][0]['id']
                    while len(user_media['data']) > count:
                        if user_media['data'][count - 1]['likes']['count'] < user_media['data'][count]['likes']['count']:
                            max_like_id = user_media['data'][count]['id']

                        count = count + 1
                    image_name = user_media['data'][0]['id'] + '.jpeg'
                    image_url = user_media['data'][0]['images']['standard_resolution']['url']
                    urllib.urlretrieve(image_url, image_name)
                    return max_like_id
                elif choice == 3:
                    count = 1
                    max_like_id = user_media['data'][0]['id']
                    while len(user_media['data']) > count:
                        if user_media['data'][count - 1]['likes']['count'] > user_media['data'][count]['likes']['count']:
                            max_like_id = user_media['data'][count]['id']

                        count = count + 1
                    image_name = user_media['data'][0]['id'] + '.jpeg'
                    image_url = user_media['data'][0]['images']['standard_resolution']['url']
                    urllib.urlretrieve(image_url, image_name)
                    return max_like_id
                elif choice == 4:
                    break
                else:
                    print "\n\n[[Select From Valid Options]]"
        else:
            print "User does not exists \n"
    else:
        print "Status code other than 200 recived \n"
        return None
