# Class Code Problem
'''Given a list of n numbers, determine if it contains any duplicate numbers.'''

def check_duplicate(input_list):
    contains_no_dups = Set()
    for element in input_list:
        if element in contains_no_dups:
            return True # found deplicate
        else: # not found add to set
            contains_no_dups.append(element)
        return False # didn't find duplicates

if __name__ == '__main__':
    check_duplicate([5,10,15,14])
    check_duplicate([8,2,4,8,9,1])
