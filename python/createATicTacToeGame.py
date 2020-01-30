## encapslate game state in a class
class T3Game():
    def __init__(self):
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.curr_player = 0 # X for even 0 for odd
    
    def determine_player_symbol(self):
        if self.curr_player % 2 == 0:  # even
            player_symbol = "X"
        else:
            player_symbol = "O"
        return player_symbol

    def determine_status(self):
        player_symbol = self.determine_player_symbol()
        if player_symbol == "O":
            player = "FIRST"
        else:
            player = "SECOND"
        
        if self.board[0][0] == player_symbol and self.board[1][1] == player_symbol and self.board[2][2] == player_symbol:
            return "{} PLAYER WON".format(player)
        else:
            return "ONGOING"


    ## expose a method to place tokens
    def add_token(self, user_play):
        
        print("User_play:", user_play)
        space = user_play.split()
        for index,pos in enumerate(space):
            try:
                space[index] = int(pos)
            except ValueError:
                return "Invalid space please try again"
        player_symbol = self.determine_player_symbol()
        self.board[space[0]][space[1]] = player_symbol
        return

    ## expose a method to retrieve game status
    def print_board(self):
        print("    0    1    2")
        print("0 [[{}]  [{}]  [{}]]".format(
            self.board[0][0], self.board[0][1], self.board[0][2]))
        print("1 [[{}]  [{}]  [{}]]".format(
            self.board[1][0], self.board[1][1], self.board[1][2]))
        print("2 [[{}]  [{}]  [{}]]".format(
            self.board[2][0], self.board[2][1], self.board[2][2]))
        

    def print_board_start(self):
        print("    0    1    2")
        print("0 [[ ]  [ ]  [ ]]")
        print("1 [[ ]  [ ]  [ ]]")
        print("2 [[ ]  [ ]  [ ]]")

def main():
    print("Welcome to Tic Tac Toe")
    g = T3Game()
    plays = 0
    g.print_board_start()
    while plays < 9:
        g.curr_player += 1
        user_play = input("The game board is provided above, choose a row and and column (ex: 0 1): ")
        added_token = g.add_token(user_play)
        if added_token != None:
            print(added_token)
            g.curr_player -= 1
            continue
        g.print_board()
        game_status = g.determine_status()
        print(game_status)
        if 'WON' in game_status:
            break
        plays += 1
    

main()



