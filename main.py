from self_info import self_info
from get_own_post import get_own_post
from get_user_info import get_user_info
from like_a_post import like_a_post
from post_a_comment import post_a_comment
from delete_negative_comments import delete_negative_comment
from constants import insta_username
from get_user_id import get_user_id


def menu():
    while True:
        choice = raw_input(
            " 1) To get own info  \n 2) To get own post \n 3) To get friends info  \n 4) To Like post \n 5) To comment on post \n 6) To Delete negative comments \n 7) To exit application\n ENTER YOUR CHOICE  :- ")
        if choice.isdigit() == True:
            choice=int(choice)
        if choice == 1:
            self_info()         # Calling of self_info() function
        elif choice == 2:
            get_own_post()
        elif choice == 3:
            get_user_info(insta_username)
        elif choice == 4:
            like_a_post(insta_username)
        elif choice == 5:
            post_a_comment(insta_username)
        elif choice == 6:
            delete_negative_comment()
        elif choice == 7:
            break
        else:
            print "\n\n[[Select From Valid Options]]"


menu()