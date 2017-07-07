from constants import APP_ACCESS_TOKEN,BASE_URL
import requests


def recent_media_like():
    request_url='%susers/self/media/liked?access_token=%s' % (BASE_URL,APP_ACCESS_TOKEN)
    print "request url is %s" % (request_url)
    media_like = requests.get(request_url).json()
    print media_like['data'][0]['id']

    media_id = []  # List to store comment id
    a = 0
    while len(media_like['data']) > a:
        media_id.append(media_like['data'][a]['id'])
        a = a + 1
    print "Media ID Are \n"
    for temp in media_id:
        print temp

