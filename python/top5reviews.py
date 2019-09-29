# Given reviews return the top 5 (id and num of reviews)
# log of reviews
# output: id and count
# Brainstorm 
# loop input
# get id
# if its already there increment

# Progress
# rebuild in sets or tuples
reviewLog = [
    {'id':1234, 'user_name':'Amy',
        'review_comment': "It was such a spectacular meal, I couldn't stop thinking about it"},
    {'id': 2345, 'user_name': 'Toby'},
    {'id':1234, 'user_name':'Amy',
        'review_comment': "It was such a spectacular meal, I couldn't stop thinking about it"},
    {'id':5678, 'user_name':'Adam',
        'review_comment': "SO GOOD! I will be back with a friend."},
    {'id':5678, 'user_name':'Adam',
        'review_comment': "SO GOOD! I will be back with a friend."},
    {'id':5678, 'user_name':'Adam',
        'review_comment': "SO GOOD! I will be back with a friend."},
    {'id':1121, 'user_name':'Raven',
        'review_comment': "Super Delicious!!"},
    {'id':1121, 'user_name':'Raven',
        'review_comment': "Super Delicious!!"},
    {'id':1121, 'user_name':'Raven',
        'review_comment': "Super Delicious!!"},
    {'id':1121, 'user_name':'Raven',
        'review_comment': "Super Delicious!!"}
]

reviewLog2 = [
    {'id': 1234, 'user_name': 'Darcey',
        'review_comment': "The food and the atomsphere was pleasant"},
    {'id': 1234, 'user_name': 'Darcey',
        'review_comment': "The food and the atomsphere was pleasant"},
    {'id': 1234, 'user_name': 'Darcey',
        'review_comment': "The food and the atomsphere was pleasant"},
    {'id': 1234, 'user_name': 'Darcey',
        'review_comment': "The food and the atomsphere was pleasant"},
    {'id': 1234, 'user_name': 'Darcey',
        'review_comment': "The food and the atomsphere was pleasant"},
    {'id': 2345, 'user_name': 'Toby',
        'review_comment': "So, so"},
    {'id': 2345, 'user_name': 'Toby',
        'review_comment': "So, so"},
    {'id': 2345, 'user_name': 'Toby',
     'review_comment': "So, so"},
    {'id': 9101112, 'user_name': 'Amy',
        'review_comment': "It was such a spectacular meal, I couldn't stop thinking about it"},
    {'id': 5678, 'user_name': 'Adam',
        'review_comment': "SO GOOD! I will be back with a friend."},
    {'id': 5678, 'user_name': 'Adam',
        'review_comment': "SO GOOD! I will be back with a friend."},
    {'id': 5678, 'user_name': 'Adam',
        'review_comment': "SO GOOD! I will be back with a friend."},
    {'id': 131415, 'user_name': 'Evan',
        'review_comment': "Discusting Food. Never going back."},
    {'id': 2345, 'user_name': 'Toby',
        'review_comment': "So, so"},
    {'id': 131415, 'user_name': 'Evan',
        'review_comment': "Discusting Food. Never going back."},
    {'id': 1121, 'user_name': 'Evan',
        'review_comment': "Discusting Food. Never going back."},
    {'id': 1121, 'user_name': 'Namon',
        'review_comment': "Terrible"},
    {'id': 161718, 'user_name': 'Namon',
        'review_comment': "Terrible"}
]

def top5Reviews(listReviews):
    """ Return 5 id and counts that occure the most"""
    hist = {}
    for i in range(0, len(listReviews)):
        review_id = listReviews[i]['id']
        if review_id in hist.keys():
            hist[review_id] += 1
        else:
            hist[review_id] = 1
    #
    ordered_ids = sorted(hist, key=hist.__getitem__, reverse=True)
    # print first 5 ids in the list of sorted ids by valiue
    for i in range(0, 5):
        print("ID: {}, COUNT: {}".format(ordered_ids[i], hist[ordered_ids[i]]))
    

# print(top5Reviews(reviewLog2))
# Notes
# O(logn)

# Create histogram of occurances of a number in a list = 
[2, 4, 5, 3, 2, 1]
# create a dictionary
# loop list
  # check if elem is in dict
    increment value
  # otherwise
    add num to dictionary
  
# you can write to stdout for debugging purposes, e.g.
print("This is a debug message")
# Input: users
# Output: greatest to least
# Return the most reviewed (user) from greatest to least


def top_5_reviews(review_comment_data):
    review_comments = []
    for review_comment in review_comment_data:

        if review_comment['user'] in review_comments:
            review_comment['user'] += 1
        else:
            review_comment['user'] = 1
    occurences = review_comments.vaues()
    sorted_occ = sorted(occurences)
    # get the key with the largest values

    #new_largest_value = 0
    #k number of times = 5
    #loop through dict
    #if dict[i].value > new_largest_value
    #new_largest_value = dict[i].user
    #pop user and add it to users

   # for key, value in my_dict.items():

    # loop dictionary find new largest value
    # pop
    # insert into users
    # ['nivedita', 'amy', 'mari',...]
    return users
