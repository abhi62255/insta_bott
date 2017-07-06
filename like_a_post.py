import requests
from constants import BASE_URL,APP_ACCESS_TOKEN
from get_users_post import  get_users_post


def like_a_post(insta_username) :
    media_id =get_users_post(insta_username)
    request_url = ('%smedia/%s/likes') % (BASE_URL,media_id)
    payload = {"access_token": APP_ACCESS_TOKEN}
    print 'POST request url : %s' % (request_url)
    post_a_like = requests.post(request_url, payload).json()

    if post_a_like['meta']['code'] == 200:
        print 'Like was successful!'
    else:
        print 'Your like was unsuccessful. (Try again)'
