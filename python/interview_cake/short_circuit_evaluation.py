# Short-Circuit Evaultion
# to avoid unneccessary work
# if first condition is false Python 3.6 doesn't check other condition
if it_is_friday and it_is_raining:
    print("board games at my place!")

if friends['Becky'].is_free_this_friday():
    invite_to_board_game_night(friends['Becky'])

if 'Becky' in friends and friends['Becky'].is_free_this_friday():
    invite_to_board_game_night(friends['Becky'])

