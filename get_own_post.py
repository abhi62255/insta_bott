from constants import BASE_URL,APP_ACCESS_TOKEN
import requests
import urllib

def get_own_post():
    request_url = ('%susers/self/media/recent/?access_token=%s') % (BASE_URL,APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    own_media = requests.get(request_url).json()

    if own_media['meta']['code'] == 200:
        if len(own_media['data']):
            image_name=own_media['data'][0]['id']+'.jpeg'
            image_url = own_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url,image_name)
            return own_media['data'][0]['id']
        else:
            print "Post does not exist \n"
    else:
        print "status code is other than 200 recived \n"
        return None