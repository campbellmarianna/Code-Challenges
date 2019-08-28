# Given reviews return the top 5 (id and num of reviews)
# log of reviews
# output: id and count
# Brainstorm f
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
    {'id':1234, 'user_name':'Amy',
        'review_comment': "It was such a spectacular meal, I couldn't stop thinking about it"},
    {'id':3000, 'user_name':'Amy',
        'review_comment': "It was such a spectacular meal, I couldn't stop thinking about it"},
    {'id':2146, 'user_name':'Amy',
        'review_comment': "It was such a spectacular meal, I couldn't stop thinking about it"},
    {'id':1121, 'user_name':'Amy',
        'review_comment': "It was such a spectacular meal, I couldn't stop thinking about it"},
    {'id':1121, 'user_name':'Amy',
        'review_comment': "It was such a spectacular meal, I couldn't stop thinking about it"},
    {'id':2516, 'user_name':'Amy',
        'review_comment': "It was such a spectacular meal, I couldn't stop thinking about it"},
    {'id':2, 'user_name':'Amy',
        'review_comment': "It was such a spectacular meal, I couldn't stop thinking about it"}
]
# from operator import itemgetter
def top5Reviews(listReviews):
    """ Return 5 id and counts that occure the most"""
    # dictListReviews = []
    hist = {}
    # dictListReviews.append(hist)
    for i in range(0, len(listReviews)):
        review_id = listReviews[i]['id']
        # print("Review: {}".format(review_id))
        if review_id in hist.keys():
            hist[review_id] += 1
        else:
            hist[review_id] = 1
    # get values from histogram
    reviewAmounts = []
    for occurance in hist.values():
        reviewAmounts.append(occurance)
    reviewAmounts.sort(reverse=True)
    return reviewAmounts[:5]
    print(reviewAmounts)
    # dictListReviews.sort(key=lambda item: item.get("id"), reverse=True)

    # newlist = sorted(dictListReviews, key=itemgetter('id'), reverse=True)
    # newlist = sorted(hist, key=lambda k: k['id'])
    # sort list of ids
    # retrieve the 5
    # dictListReviews.sort(key=itemgetter('id'), reverse=True)
    # return dictListReviews

print(top5Reviews(reviewLog))
