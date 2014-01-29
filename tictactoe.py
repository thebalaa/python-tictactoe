# TicTacToe Mohamad Balaa
# 2014 Shoraibit.com

import sys
import copy

class WinningPlayerException(Exception):
    pass

class InvalidMoveException(Exception):
    pass

class TicTacToe(object):
    '''
        row, col
    '''

    # '-' represents an empty space on the board
    board = [ ['-','-','-'] for row in range(3) ]

    # player x goes first
    current_player = 'x'
    
    def __init__(self,):
        self.configure_game()
        self.start_game_loop()

    def configure_game(self,):

        def _generate_winning_boards():
            winning_rows = []
            winning_cols = []
            for i,x in enumerate(range(3)):
                winning_row = []
                winning_col = []
                for j,y in enumerate(range(3)):
                    winning_row.append((x,y))
                    winning_col.append((y,x))
                winning_cols.append(winning_col[:])
                winning_rows.append(winning_row[:])
            return winning_cols, winning_rows, copy.deepcopy(winning_cols), copy.deepcopy(winning_rows)

        winning_cols_x, winning_rows_x, winning_cols_y, winning_rows_y = _generate_winning_boards()
        self.player_moves = { 'x': {'winning_cols':winning_cols_x,'winning_rows':winning_rows_x}, 'y': {'winning_cols':winning_cols_y,'winning_rows':winning_rows_y}}
        
                    
        #print '1) Play against the computer\n2) Play against another human'
        #self.num_players = raw_input('Please enter 1 or 2: ')

    def draw_board(self,):
        for row in self.board:
            print '%s %s %s' % (row[0], row[1], row[2])

    def do_player_turn(self, position):
        row,col = position
        # make sure the requested position is available
        if self.board[row][col] != '-':
            raise InvalidMoveException("This place is already taken")
        
        #update the board
        self.board[row][col] = self.current_player
        
        # check rows
        self.player_moves[self.current_player]['winning_rows'][row].remove((row,col))
        if not self.player_moves[self.current_player]['winning_rows'][row]:
            raise WinningPlayerException('%s has won' % (self.current_player,))
        
        # check columns 
        self.player_moves[self.current_player]['winning_cols'][col].remove((row,col))
        if not self.player_moves[self.current_player]['winning_cols'][col]:
            raise WinningPlayerException('%s has won' % (self.current_player,))
        
        # check left and right diagonal
        right = False
        left = False
        if (0,0) not in self.player_moves[self.current_player]['winning_rows'][0]:
            left = True
        if (0,2) not in self.player_moves[self.current_player]['winning_rows'][0]:
            right = True
        if right or left:
            if (1,1) not in self.player_moves[self.current_player]['winning_rows'][1]:
                if (2,0) not in self.player_moves[self.current_player]['winning_rows'][2]:
                    if right:
                        raise WinningPlayerException('%s has won' % (self.current_player,))
                if (2,2) not in self.player_moves[self.current_player]['winning_cols'][2]:
                    if left:
                        raise WinningPlayerException('%s has won' % (self.current_player,))

        # toggle self.current_player
        if self.current_player == 'x':
            self.current_player = 'y'
        else:
            self.current_player = 'x'

    def start_game_loop(self,):
        while True:
            print "Player %s it is your turn!" % ( self.current_player,)
            position = raw_input('Enter a position row, col ( for example 0,0 is the top left ) or press \'b\' to display the board: ')
            if position == 'b':
                self.draw_board()
                continue
            else:
                try:
                    row, col = position.split(',')
                    self.do_player_turn((int(row),int(col)))
                except WinningPlayerException, e:
                    print str(e)
                    break
                except InvalidMoveException, e:
                    print str(e)
                    continue
                except ValueError, e:
                    print str(e)
                    continue

if __name__ == '__main__':
    TicTacToe()
