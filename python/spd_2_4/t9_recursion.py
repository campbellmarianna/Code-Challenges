'''
Prompt:
Given a string of digits 2 to 9 a user has pressed on a T9 telephone keypad, return a list of all letter combinations they could have been trying to type on the keypad
'''
# create a dictionary (numbers to letters)
# create comb list
# find first number letters
# find second number letters
# loop first number letters
    # loop second number letter and characters and append to comp list
# return list


def t9_letters(digit_string):
    '''Note: Function solution only works for two digit inputs'''
    # create a dictionary (numbers to letters)
    t9_keyboard = {2: "abc", 3: "def", 4:"ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
    # create comb list
    comb_list = []
    # find first number letters
    letters_1 = t9_keyboard[int(digit_string[0])]
    print(letters_1) # "abc"
    # find second number letters
    letters_2 = t9_keyboard[int(digit_string[1])]
    # loop first number letters
    for char_1 in letters_1:
        # loop second number letter and characters and append to comp list
        for char_2 in letters_2:
            comb_list.append(char_1+char_2)
    # return list
    return comb_list

if __name__ == '__main__':
    digit_string = '23'
    print(t9_letters(digit_string))

    
