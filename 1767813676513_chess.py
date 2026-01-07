import numpy as np  #imports




class Base_Piece:


   def __init__(self, color, position, symbol):
      self.color = color    # represents the piece color no matter the type/symbol it must have either W for white or B for black
      self.position = position  # Represents the 8x8 coordinates On The Chess language Converted to position On the array eg pawn e8 is converted To where e8 is On the array
      self.symbol = symbol  # represents the piece type eg rook is r, bishop is b


   def move(self, position, new_position, board):
       raise NotImplementedError


   def legal(self, position, board):
       raise NotImplementedError






class Piece_Pawn(Base_Piece):


    def __init__(self, color, position):
       super().__init__(color, position, symbol='p')




    def move_pawn(self, position, new_position, board):


        orig_row, orig_col = position
        dest_row, dest_col = new_position


        # Move the pawn
        board[dest_row][dest_col] = board[orig_row][orig_col]  # copy pawn to new position
        board[orig_row][orig_col] = '_'  # empty the original square


    def pawn_legal(self, color, position, new_position, board):


       orig_row, orig_col = position
       dest_row, dest_col = new_position
       dest_cell = board[dest_row][dest_col]
       orig_cell = board[orig_row][orig_col]
       color = orig_cell[0]  # 'W' or 'B'


    # Destination bounds check
       if not (0 <= dest_row < 8 and 0 <= dest_col < 8):
           return False


    # White pawn logic
       if color == "W":
        # Single forward
           if dest_col == orig_col and dest_cell == '_' and dest_row == orig_row - 1:
               return True


        # Double forward from starting row
           elif dest_col == orig_col and dest_cell == '_' and dest_row == orig_row - 2 and orig_row == 6:
               if board[orig_row - 1][orig_col] == '_':  # square in between must be empty
                   return True


        # Diagonal capture
           elif abs(dest_col - orig_col) == 1 and dest_row == orig_row - 1 and dest_cell != '_' and dest_cell[0] == 'B':
               return True


           else:
               return False


    # Black pawn logic
       elif color == "B":
        # Single forward
           if dest_col == orig_col and dest_cell == '_' and dest_row == orig_row + 1:
               return True


        # Double forward from starting row
           elif dest_col == orig_col and dest_cell == '_' and dest_row == orig_row + 2 and orig_row == 1:
               if board[orig_row + 1][orig_col] == '_':  # square in between must be empty
                   return True


        # Diagonal capture
           elif abs(dest_col - orig_col) == 1 and dest_row == orig_row + 1 and dest_cell != '_' and dest_cell[0] == 'W':
               return True


           else:
               return False






class Piece_Rook(Base_Piece):
    def __init__(self, color, position):
       super().__init__(color, position, symbol='r')


    def move_rook(self, position, new_position, board):


        orig_row, orig_col = position
        dest_row, dest_col = new_position


        # Move the rook
        board[dest_row][dest_col] = board[orig_row][orig_col]  # copy rook to new position
        board[orig_row][orig_col] = '_'  # empty the original square


    def rook_legal(self, position, new_position, board):


        orig_row, orig_col = position
        dest_row, dest_col = new_position
        dest_cell = board[dest_row][dest_col]
        color = board[orig_row][orig_col][0]


    # bounds check
        if not (0 <= dest_row < 8 and 0 <= dest_col < 8):
            return False


    # straight line check
        if not (orig_row == dest_row or orig_col == dest_col):
            return False


    # path clear
        if orig_row == dest_row:  # horizontal
            step = 1 if dest_col > orig_col else -1
            for col in range(orig_col + step, dest_col, step):
                if board[orig_row][col] != '_':
                    return False
        elif orig_col == dest_col:  # vertical
            step = 1 if dest_row > orig_row else -1
            for row in range(orig_row + step, dest_row, step):
                if board[row][orig_col] != '_':
                    return False


    # cannot capture own piece
        if dest_cell != '_' and color == dest_cell[0]:
            return False


        return True


class Piece_Bishop(Base_Piece):
    def __init__(self, color, position):
       super().__init__(color, position, symbol='b')


    def move_bishop(self, position, new_position, board):


        orig_row, orig_col = position
        dest_row, dest_col = new_position


        # Move the bishop
        board[dest_row][dest_col] = board[orig_row][orig_col]  # copy bishop to new position
        board[orig_row][orig_col] = '_'  # empty the original square


    def bishop_legal(self, position, new_position, board):


        orig_row, orig_col = position
        dest_row, dest_col = new_position
        dest_cell = board[dest_row][dest_col]
        color = board[orig_row][orig_col][0]


        # bounds check
        if not (0 <= dest_row < 8 and 0 <= dest_col < 8):
            return False


        # Diagonal check
        if abs(dest_row - orig_row) != abs(dest_col - orig_col):
            return False


        # Path clear check
        row_step = 1 if dest_row > orig_row else -1
        col_step = 1 if dest_col > orig_col else -1
        row, col = orig_row + row_step, orig_col + col_step
        while row != dest_row and col != dest_col:
            if board[row][col] != '_':
                return False
            row += row_step
            col += col_step


        # cannot capture own piece
            if dest_cell != '_' and color == dest_cell[0]:
                return False


        return True






class Piece_Knight(Base_Piece):
    def __init__(self, color, position):
       super().__init__(color, position, symbol='n')


    def move_knight(self, position, new_position, board):


       orig_row, orig_col = position
       dest_row, dest_col = new_position


       # Move the knight
       board[dest_row][dest_col] = board[orig_row][orig_col]  # copy knight to new position
       board[orig_row][orig_col] = '_'  # empty the original square




    def knight_legal(self, position, new_position, board):




       orig_row, orig_col = position
       dest_row, dest_col = new_position
       dest_cell = board[dest_row][dest_col]
       orig_cell = board[orig_row][orig_col]
       color = orig_cell[0]  # 'W' or 'B'


    # Destination bounds check
       if not (0 <= dest_row < 8 and 0 <= dest_col < 8):
           return False




    # L-shape check
       dr = abs(dest_row - orig_row)
       dc = abs(dest_col - orig_col)


       if not ((dr == 2 and dc == 1) or (dr == 1 and dc == 2)):
           return False




    # cannot capture own piece
       if dest_cell != '_' and color == dest_cell[0]:
           return False


       return True






class Piece_King(Base_Piece):
    def __init__(self, color, position):
       super().__init__(color, position, symbol='k')


    def move_king(self, position, new_position, board):


       orig_row, orig_col = position
       dest_row, dest_col = new_position


       # Move the king
       board[dest_row][dest_col] = board[orig_row][orig_col]  # copy king to new position
       board[orig_row][orig_col] = '_'  # empty the original square






    def king_legal(self, position, new_position, board):  # verify all check and checkmate rules Separately from king_legal


       orig_row, orig_col = position
       dest_row, dest_col = new_position
       dest_cell = board[dest_row][dest_col]
       orig_cell = board[orig_row][orig_col]
       color = orig_cell[0]  # 'W' or 'B'


    # Destination bounds check
       if not (0 <= dest_row < 8 and 0 <= dest_col < 8):
           return False




    #movement check
       dr = abs(dest_row - orig_row)
       dc = abs(dest_col - orig_col)


       if dr == 0 and dc == 0:
          return False  # didn't move


       if dr > 1 or dc > 1:
          return False # too far


    # cannot capture own piece
       if dest_cell != '_' and color == dest_cell[0]:
           return False


       return True






class Piece_Queen(Base_Piece):
    def __init__(self, color, position):
       super().__init__(color, position, symbol='q')


    def move_queen(self, position, new_position, board):


        orig_row, orig_col = position
        dest_row, dest_col = new_position


        # Move the queen
        board[dest_row][dest_col] = board[orig_row][orig_col]  # copy queen to new position
        board[orig_row][orig_col] = '_'  # empty the original square


    def queen_legal(self, position, new_position, board):




        orig_row, orig_col = position
        dest_row, dest_col = new_position
        dest_cell = board[dest_row][dest_col]
        color = board[orig_row][orig_col][0]




        # shape check: must be diagonal OR straight
        if not (
           abs(dest_row - orig_row) == abs(dest_col - orig_col) or
           orig_row == dest_row or
           orig_col == dest_col
        ):
           return False




        #path clear checks
        if abs(dest_row - orig_row) == abs(dest_col - orig_col):


            row_step = 1 if dest_row > orig_row else -1
            col_step = 1 if dest_col > orig_col else -1
            row, col = orig_row + row_step, orig_col + col_step
            while row != dest_row and col != dest_col:
                if board[row][col] != '_':
                    return False
                row += row_step
                col += col_step


        elif (orig_row == dest_row or orig_col == dest_col):


            if orig_row == dest_row:  # horizontal
                step = 1 if dest_col > orig_col else -1
                for col in range(orig_col + step, dest_col, step):
                    if board[orig_row][col] != '_':
                        return False
            elif orig_col == dest_col:  # vertical
                step = 1 if dest_row > orig_row else -1
                for row in range(orig_row + step, dest_row, step):
                    if board[row][orig_col] != '_':
                        return False




        #color check
        if dest_cell != '_' and color == dest_cell[0]:
            return False


        return True










class board_array:


    board = np.array([
 ['Br', 'Bn', 'Bb', 'Bq', 'Bk', 'Bb', 'Bn', 'Br'],
 ['Bp', 'Bp', 'Bp', 'Bp', 'Bp', 'Bp', 'Bp', 'Bp'],
 [ '_',  '_',  '_',  '_',  '_',  '_',  '_',  '_' ],
 [ '_',  '_',  '_',  '_',  '_',  '_',  '_',  '_' ],
 [ '_',  '_',  '_',  '_',  '_',  '_',  '_',  '_' ],
 [ '_',  '_',  '_',  '_',  '_',  '_',  '_',  '_' ],
 ['Wp', 'Wp', 'Wp', 'Wp', 'Wp', 'Wp', 'Wp', 'Wp'],
 ['Wr', 'Wn', 'Wb', 'Wq', 'Wk', 'Wb', 'Wn', 'Wr']
])


# cell command allows me to spread space out with out messing with the board attrube mannually.














def func_input_translation(current_player):
    """
    Translates user chess input into array coordinates.


    Expected input format:
        <piece> <origin> <destination>
        Example: p e2 e4


    Returns:
        piece_symbol (str): lowercase piece symbol (e.g. 'p')
        origin_coord (tuple): (row, col) index for origin
        dest_coord (tuple): (row, col) index for destination
    """


    # Prompt player for input
    move_input = input(f"Choose your move ({current_player}): ")


    # Split input into components
    parts = move_input.split()
    piece_symbol = parts[0].lower()
    origin = parts[1]
    destination = parts[2]


    # Maps chess file letters to array columns
    col_map = {
        'a': 0, 'b': 1, 'c': 2, 'd': 3,
        'e': 4, 'f': 5, 'g': 6, 'h': 7
    }


    # Maps chess ranks to array rows (flipped for array indexing)
    row_map = {
        '1': 7, '2': 6, '3': 5, '4': 4,
        '5': 3, '6': 2, '7': 1, '8': 0
    }


    # Convert chess notation to array coordinates
    origin_coord = (row_map[origin[1]], col_map[origin[0]])
    dest_coord = (row_map[destination[1]], col_map[destination[0]])




    return piece_symbol, origin_coord, dest_coord








# bounds check: qeustion is Is it in bounds?


def bounds_verify(origin):
    row, col = origin
    return 0 <= row < 8 and 0 <= col < 8




# space filled check: what holds the origin if nothing invalid if piece types are the same vaild qeustion is Is there a piece there?


def space_verify(origin, piece):
    row, col = origin
    cell = board_array.board[row][col]
    if cell == '_':
        return False
    elif cell[1] != piece:
        return False
    return True




# color verifaction:  qeustion is Does it belong to the current player?


def color_verify(origin, piece, current_player):
    row, col = origin
    cell = board_array.board[row][col]
    if current_player == "white" and cell[0] != 'W':
        return False
    if current_player == "black" and cell[0] != 'B':
        return False
    return True




# check and checkmate detection functions
def pawn_attacks_square(origin, target, board):
    r, c = origin
    tr, tc = target
    piece = board[r][c]
    color = piece[0]


    direction = -1 if color == 'W' else 1


    return tr == r + direction and abs(tc - c) == 1




def find_king(board, current_player):
    king = ('Wk' if current_player == "white" else 'Bk')
    for r in range(8):
        for c in range(8):
            if board[r][c] == king:
                return (r, c)
    return None




def piece_attacks_square(piece, origin, target, board):
    p = piece[1]


    if p == 'p':
        return pawn_attacks_square(origin, target, board)
    elif p == 'r':
        return Piece_Rook(None, None).rook_legal(origin, target, board)
    elif p == 'n':
        return Piece_Knight(None, None).knight_legal(origin, target, board)
    elif p == 'b':
        return Piece_Bishop(None, None).bishop_legal(origin, target, board)
    elif p == 'q':
        return Piece_Queen(None, None).queen_legal(origin, target, board)
    elif p == 'k':
        return Piece_King(None, None).king_legal(origin, target, board)


    return False




def check_detection(board, current_player):
    king_pos = find_king(board, current_player)
    enemy = 'B' if current_player == "white" else 'W'


    for r in range(8):
        for c in range(8):
            piece = board[r][c]
            if piece == '_' or piece[0] != enemy:
                continue


            if piece_attacks_square(piece, (r, c), king_pos, board):
                return True


    return False




def make_move(board, origin, dest):
    r1, c1 = origin
    r2, c2 = dest
    captured = board[r2][c2]
    board[r2][c2] = board[r1][c1]
    board[r1][c1] = '_'
    return captured




def undo_move(board, origin, dest, captured):
    r1, c1 = origin
    r2, c2 = dest
    board[r1][c1] = board[r2][c2]
    board[r2][c2] = captured


def movement_legal(piece, origin, dest, board):
    p = piece[1]


    if p == 'p':
        return Piece_Pawn(None, None).pawn_legal(None, origin, dest, board)
    elif p == 'r':
        return Piece_Rook(None, None).rook_legal(origin, dest, board)
    elif p == 'n':
        return Piece_Knight(None, None).knight_legal(origin, dest, board)
    elif p == 'b':
        return Piece_Bishop(None, None).bishop_legal(origin, dest, board)
    elif p == 'q':
        return Piece_Queen(None, None).queen_legal(origin, dest, board)
    elif p == 'k':
        return Piece_King(None, None).king_legal(origin, dest, board)


    return False




def is_legal_move(piece, origin, dest, board):
    # 1. movement rules
    if not movement_legal(piece, origin, dest, board):
        return False


    # 2. simulate move
    captured = make_move(board, origin, dest)


    current_player = "white" if piece[0] == 'W' else "black"
    still_in_check = check_detection(board, current_player)


    # 3. undo
    undo_move(board, origin, dest, captured)


    return not still_in_check




def checkmate_detection(board, current_player):
    if not check_detection(board, current_player):
        return False


    color = 'W' if current_player == "white" else 'B'


    for r in range(8):
        for c in range(8):
            piece = board[r][c]
            if piece == '_' or piece[0] != color:
                continue


            origin = (r, c)


            for dr in range(8):
                for dc in range(8):
                    dest = (dr, dc)


                    if is_legal_move(piece, origin, dest, board):
                        return False  # escape exists


    return True










# main loop


current_player = "white"


letters = 'a, b, c, d, e, f, g, h'.split()


def print_board():
    print("  " + " ".join(letters))
    for i, row in enumerate(board_array.board, start=1):
        print(f"{8-i+1} " + " ".join(f"{cell:2}" for cell in row))




def get_piece_object(piece_str, position):
    color = piece_str[0]
    symbol = piece_str[1]
    if symbol == 'p':
        return Piece_Pawn(color, position)
    elif symbol == 'r':
        return Piece_Rook(color, position)
    elif symbol == 'n':
        return Piece_Knight(color, position)
    elif symbol == 'b':
        return Piece_Bishop(color, position)
    elif symbol == 'q':
        return Piece_Queen(color, position)
    elif symbol == 'k':
        return Piece_King(color, position)
    return None


while True:
    print_board()


    # Step 1: get user input
    piece_symbol, origin, destination = func_input_translation(current_player)


    # Step 2: validate origin square
    if not bounds_verify(origin):
        print("Invalid origin: out of bounds")
        continue


    if not space_verify(origin, piece_symbol):
        print("Invalid origin: no piece or wrong type")
        continue


    if not color_verify(origin, piece_symbol, current_player):
        print("Invalid origin: wrong color")
        continue


    # Step 3: validate move legality
    piece_str = board_array.board[origin[0]][origin[1]]
    piece_obj = get_piece_object(piece_str, origin)


    # Call the correct legal function
    legal = False
    if piece_symbol == 'p':
        legal = piece_obj.pawn_legal(piece_obj.color, origin, destination, board_array.board)
    elif piece_symbol == 'r':
        legal = piece_obj.rook_legal(origin, destination, board_array.board)
    elif piece_symbol == 'n':
        legal = piece_obj.knight_legal(origin, destination, board_array.board)
    elif piece_symbol == 'b':
        legal = piece_obj.bishop_legal(origin, destination, board_array.board)
    elif piece_symbol == 'q':
        legal = piece_obj.queen_legal(origin, destination, board_array.board)
    elif piece_symbol == 'k':
        legal = piece_obj.king_legal(origin, destination, board_array.board)


    if not legal:
        print("Illegal move! Try again.")
        continue


    # Step 4: make the move
    make_move(board_array.board, origin, destination)


    # Step 5: check for check or checkmate
    opponent = "black" if current_player == "white" else "white"
    if check_detection(board_array.board, opponent):
        if checkmate_detection(board_array.board, opponent):
            print_board()
            print(f"Checkmate! {current_player.capitalize()} wins!")
            break
        else:
            print(f"{opponent.capitalize()} is in check!")


    # Step 6: switch player
    current_player = opponent