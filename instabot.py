from self_info import self_info
from get_own_post import get_own_post
from get_user_info import get_user_info
from recent_media_like import recent_media_like
from like_a_post import like_a_post
from post_a_comment import post_a_comment
from delete_negative_comments import delete_negative_comment
from constants import insta_username
from get_user_id import get_user_id
from get_users_post import get_users_post

def menu():
    while True:
        choice = raw_input(
            " 1) To get own info  \n 2) To get own post \n 3) To get friends id \n 4) To get friends info \n 5) To Get friend post id \n 6) To Like post \n 7) To comment on post \n "
            "8) To Delete negative comments from your post\n 9) To view recent Media id like by You\n 10) To exit application\n ENTER YOUR CHOICE  :- ")
        if choice.isdigit() == True:
            choice=int(choice)
        if choice == 1:
            self_info()         # Calling of self_info() function
        elif choice == 2:
            print "Post Id : %s \n"% get_own_post()
        elif choice == 3:
            print "User ID : %s \n" % get_user_id(insta_username)
        elif choice == 4:
            get_user_info(insta_username)
        elif choice == 5:
            print "Post ID : %s \n"% get_users_post(insta_username)
        elif choice == 6:
            like_a_post(insta_username)
        elif choice == 7:
            post_a_comment(insta_username)
        elif choice == 8:
            delete_negative_comment()
        elif choice == 9:
            recent_media_like()
        elif choice == 10:
            break
        else:
            print "\n\n[[Select From Valid Options]]"


menu()