from instagrapi import Client
import time


user,passwd=" "," " #input required here


############ GLOBAL VARIABLES #############
client=Client()
client.login(user,passwd)
my_id=client.user_id

followings={}
followers={}

unfriendly=[]
############ GLOBAL VARIABLES #############

def followings_info():
    """
    Fetches the user's following information and prints out the name,username and userID of accounts followed
    """
    following=client.user_following_gql(my_id, amount=0)
    j=0
    for i in enumerate(following):
        name,username,IDnum=following[j].full_name,following[j].username,following[j].pk
        print(f"Name:",name," Username:",username," ID:",IDnum,"\n")
        followings[username]=(name,IDnum)
        j+=1
    return followings

def followers_info():
    """
    Fetches the user's followers info and prints out the name,username and userID of followers
    """
    follower=client.user_followers_v1(my_id, amount=0)
    k=0
    for i in enumerate(follower):
        name,username,IDnum=follower[k].full_name,follower[k].username,follower[k].pk
        print(f"Name:",name," Username:",username,IDnum,"\n")
        followers[username]=(name,IDnum)
        k+=1
    return followers


def not_followbk():
    """
    Prints followed accounts which the user do not follow the user back
    """
    followings_info()
    followers_info()
    for i in followings:
        if i not in followers:
            unfriendly.append([i,followings[i]])
            print(followings[i][0]," ",followings[i][1])
    print(unfriendly)
            
def remove_from_following(acct_id):
    """
    Requires manual input. Unfollows specified user_id when called
    """
    client.user_unfollow(acct_id)

if __name__ == "__main__":
    not_followbk()

