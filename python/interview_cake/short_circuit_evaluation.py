# Short-Circuit Evaultion
# To avoid unneccessary work

# If first condition is false Python 3.6 doesn't check other condition
if it_is_friday and it_is_raining:
    print("board games at my place!")

# Potentially get a Key Error on the first check
if friends['Becky'].is_free_this_friday():
    invite_to_board_game_night(friends['Becky'])
# If 'Becky' isn't in friends, Python will ignore the rest of the conditional and aviod throwing the KeyError
if 'Becky' in friends and friends['Becky'].is_free_this_friday():
    invite_to_board_game_night(friends['Becky'])

# Summary
# Short circuit evaulation enables a programmer to do related conditionals on one line instead of multiple nested conditionals. This is primary useful making code more concise and readiable.