"""
Name: divisivecomments.py
Purpose: Given a reddit post url, returns a url to the most divise comment in that post 
         determined by the ratio of replies to upvotes.
Date: Dec 20 2019
Author: Zhang.G
"""

import praw

reddit = praw.Reddit(client_id='soD8M4NEXWa4Fw',
                     client_secret='TIOMIhNBRBx-t4X9KmqkHfbjPbE',
                     user_agent='controversial')

urlhere = input("Enter reddit url here: ")
post = reddit.submission(url=urlhere)

post.comments.replace_more(limit=None)
num_of_replies = 0
c_ratio = 0
current = False

for top_level_comment in post.comments:
    for second_level_comment in top_level_comment.replies:
        num_of_replies += 1

    if top_level_comment.score == 0:
        controversy_rating = num_of_replies
    else:
        controversy_rating = abs(num_of_replies / top_level_comment.score)

    if c_ratio < controversy_rating:
        c_ratio = controversy_rating
        current = top_level_comment

    counter = 0
    num_of_replies = 0

print(urlhere + current.id)
