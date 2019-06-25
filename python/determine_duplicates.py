"""
Class Code Problem: Given a list of n numbers, determine if it contains any duplicate numbers.
"""

def check_duplicate(input_list):
    """
    Returns True or False by finding if there are any repeated elements in the inputlist.
    """
    contains_no_dups = set()
    for item in input_list:
        print("Contains_no_dups set: {}".format(contains_no_dups))
        if item in contains_no_dups:
            return True # found deplicate
        else: # not found add to set
            contains_no_dups.add(item)
    return False # didn't find duplicates

if __name__ == '__main__':
    print(check_duplicate([5,10,15,14]))
    print(check_duplicate([8,2,4,8,9,1]))
