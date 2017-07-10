import requests
from constants import BASE_URL,APP_ACCESS_TOKEN




def sub_trends():
    tag = raw_input("Enter the Event : ")
    name = []
    media_count = []
    request_url='%stags/search?q=%s&access_token=%s' % (BASE_URL,tag,APP_ACCESS_TOKEN)
    print "Get request URL is : %s" % (request_url)
    media = requests.get(request_url).json()
    print media['data']




    count = 1
    while len(media['data']) > count:
        name.append(media['data'][count]['name'].encode("utf-8"))
        media_count.append(media['data'][count]['media_count'])
        count = count + 1

    count = 0
    while len(media['data'])-1 > count:
        print str(name[count])+" "+str(media_count[count])
        count = count + 1


sub_trends()
