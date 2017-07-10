import requests
from constants import BASE_URL,APP_ACCESS_TOKEN
import matplotlib.pyplot as plt
plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt





def sub_trends():
    name = []
    media_count = []
    tag = raw_input("Enter the Event : ")
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

    plt.rcdefaults()
    fig, ax = plt.subplots()

    # Example data

    y_pos = np.arange(len(name))
    error = np.random.rand(len(name))

    ax.barh(y_pos, media_count, xerr=error, align='center',
            color='blue', ecolor='black')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(name)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Media Counts   Unit : Crore')
    ax.set_title('Sub-trends for an Event : ' + tag)

    plt.show()



