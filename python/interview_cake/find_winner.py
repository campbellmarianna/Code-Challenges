'''
Prompt:
Tic-tac-toe is played by two players A and B on a 3 x 3 grid.

Here are the rules of Tic-Tac-Toe:

Players take turns placing characters into empty squares (" ").
The first player A always places "X" characters, while the second player B always places "O" characters.
"X" and "O" characters are always placed into empty squares, never on filled ones.
The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.
Given an array moves where each element is another array of size 2 corresponding to the row and column of the grid where they mark their respective character in the order in which A and B play.

Return the winner of the game if it exists (A or B), in case the game ends in a draw return "Draw", if there are still movements to play return "Pending".

You can assume that moves is valid (It follows the rules of Tic-Tac-Toe), the grid is initially empty and A will play first.
'''
# Return the Winner, Draw, Pending based on the rules of the board

# valid input - follows the rules
# Input: array moves 

# Input: [[X, O, X], # (0, 0), (0,1), (0,2)
#         [X, O, X], # (1, 0), (1,1), (1,2)
#         [X, O, X]] # (2, 0), (2,1), (2,2)
# Output: X

# Input: [[X, O, X], 
#         [X, X, O], 
#         [X, O, X]]
# Output: X

# add a move to the board
# check if the game should end 
    # letter found three times and properly positioned
    # no more empty (" ") spots

# if there are no more moves return Pending

# def tictactoe_1(moves: List[List[int]]) -> str:
    # fill in the board with the moves
    # check moves for empty spot and return pending otherwise continue
    # for inner_list in moves:
    #     for move in inner_list:
    #         if move == '':
    #             return "Pending"
    # A_wins = 0
    # a_win = 0
    # B_wins = 0
    # # check for 3 spaces filed with As or Bs in a particular order
    # # check straight down
    # for inner_list in moves:
    #     for move in inner_list:
    #         if move[0] == 'A':

                
        # check horizontal
        # check diagonally 

# add a move to the board
# check if the game should end
# letter found three times and properly positioned
# no more empty (" ") spots

# if there are no more moves return Pending

def tictactoe(moves) -> str:
    board = [["", "", ""], ["", "", ""], ["", "", ""]]
    player = True
    winners = {('A', 'A', 'A'): 'A', ('B', 'B', 'B'): 'B'}
    # Fill in the board with the moves
    for inner_list in moves:
        row, column = inner_list
        if player:  # True is Player A
            board[row][column] = 'A'
            player = False
        else:  # False is Player B
            board[row][column] = 'B'
            player = True
        # Check if the game should end
        empty_space = 0
        # Check for 3 of the same (non-empty) character
        for inner_list_index in range(len(board)):
            # Row
            row = tuple(board[inner_list_index])
            if row in winners:
                return winners[row]
            # Column
            column = tuple([board[0][inner_list_index],
                            board[0+1][inner_list_index], board[0+2][inner_list_index]])
            if column in winners:
                return winners[column]
            if board[inner_list_index][0] == '':
                empty_space += 1
            if board[inner_list_index][1] == '':
                empty_space += 1
            if board[inner_list_index][2] == '':
                empty_space += 1
        # Diagonal
        diagonal = (board[0][0], board[1][1], board[2][2])
        if diagonal in winners:
                return winners[diagonal]
        diagonal = (board[0][2], board[1][1], board[2][0])
        if diagonal in winners:
                return winners[diagonal]
        # No more empty ("") spots
        if empty_space == 0:
            return "Draw"

    # If there are no more moves
    return "Pending"
        
if __name__ == '__main__':
    # moves = [[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]] # [['A','', ''], ['', 'A', ''], ['B', 'B', 'A']]
    moves = [[0, 0], [1, 1], [2, 0], [1, 0], [
        1, 2], [2, 1], [0, 1], [0, 2], [2, 2]]  # [['A','A', 'B'], ['B', 'B', 'A'], ['B', 'B', 'A']]
    moves = [[0, 2], [1, 0], [2, 2], [1, 2], [
        2, 0], [0, 0], [0, 1], [2, 1], [1, 1]]
    print(tictactoe(moves))  # [['B','A', 'A'], ['B', 'A', 'B'] ,['A', 'B', 'A']]
