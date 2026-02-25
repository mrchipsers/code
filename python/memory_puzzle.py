import random
import time


# 7. play_game
def play_game():
    rows, columns=choose_difficulty_level()
    board, revealed=get_board(rows, columns), get_revealed_cells(rows, columns)
    score=[0,0]
    player=0
    while not has_won(revealed, rows, columns):
        clear_screen()
        print(score)
        print(f"Player {player+1}'s turn")
        chosen1=get_player_choice(revealed, rows, columns)
        revealed[chosen1[0]][chosen1[1]]=True
        display_board(board, revealed, rows, columns)
        chosen2=get_player_choice(revealed, rows, columns)
        revealed[chosen2[0]][chosen2[1]]=True
        display_board(board, revealed, rows, columns)
        if board[chosen1[0]][chosen1[1]]==board[chosen2[0]][chosen2[1]]:
            print("Match!")
            score[player]+=1
        else:
            print("No Match")
            revealed[chosen1[0]][chosen1[1]], revealed[chosen2[0]][chosen2[1]]=False, False
            player^=1
    clear_screen()
    print(f"Player 1 score: {score[0]}")
    print(f"Player 2 score: {score[1]}")
    display_board(board, revealed, rows, columns)
    if score[0]>score[1]:
        print("🎉 Player 1 wins!")
    elif score[0]<score[1]:
        print("🎉 Player 2 wins!")
    else:
        print("🤝 It's a tie!")


# 6. get_player_choice
def get_player_choice(revealed: list[list], rows: int, columns: int):
    move=""
    valid=False
    while not valid:
        move=input("(row column): ")
        move=move.split()
        if not len(move)==2:
            print("Enter two numbers: row and column")
        elif not move[0].isdigit() or not move[1].isdigit():
            print("Enter valid numbers")
        elif not 0<=int(move[0])<=rows-1 or not 0<=int(move[1])<=columns-1:
            print(f"Numbers must be between 0 - {rows-1} for rows and 0 - {columns-1} for columns")
        elif revealed[int(move[0])][int(move[1])]:
            print("Cell already opened. Pick another one.")
        else:
            valid=True
    return (int(move[0]), int(move[1]))

# 5. has_won
def has_won(revealed: list[list], rows: int, columns: int):
    for i in range(rows):
        for j in range(columns):
            if not revealed[i][j]:
                return False
    return True


# clear_screan
# DON'T MODIFY THIS CODE
def clear_screen():
    '''
    pushes the previous board output off the screen by 
    printing 30 blank lines so that the board is hidden 
    between turns
    '''
    print('\n'*10)


# display_board
# DON'T MODIFY THIS CODE
def display_board(board, revealed_cells, rows, columns):
    '''
    display the board, no return    
    :param board: 2D list of symbols
    :param revealed_cells: 2D list of truth values
    :param rows: number rows in the board
    :param columns: number of columns in the board
    :return: None
    '''    
    # column numbers
    print('    ', end = '')
    for i in range(columns):
        print(f'   {i}  ', end = '')
    print()

    # top border
    print('   +' + '-----+' * columns)

    for j in range(rows):
        print(f'{j}  |', end='')
        for k in range(columns):
            if revealed_cells[j][k]:
                cell = board[j][k]    
                print(f' {cell}  |', end='') 
            else:
                cell = '*'
                print(f'  {cell}  |', end='')
         
        print()
        print('   +' + '-----+' * columns)


        

# 4. get_revealed_cells
def get_revealed_cells(rows: int, columns: int):
    board=[]
    for i in range(rows):
        column=[]
        for j in range(columns):
            column.append(False)
        board.append(column)
    return board

# 3. get_board
def get_board(rows: int, columns: int):
    icons=get_symbols((rows*columns)//2)
    board=[]
    icon=0
    for i in range(rows):
        column=[]
        for j in range(columns):
            column.append(icons[icon])
            icon+=1
        board.append(column)
    return board



# 2. get_symbols
def get_symbols(num_pairs: int):
    '''
    Generate and return a shuffled list of symbol pairs by randomly picking
    num_pairs symbols from the given list all_symbols. 
    :param num_pairs: the number of pairs needed
    :return: list of shuffled pairs
    '''
    all_symbols = ['😀', '😎', '🤠', '🥶', '🦁', '🐥', '🌻', '🍄', '🌞', '🐱', '🐶', '🐸', '🐵', '🐼', '🦊', '🐯', '🐨']
    symbolsCopy=all_symbols[:]
    icons=[]
    for i in range(num_pairs):
        if not symbolsCopy:
            symbolsCopy=all_symbols[:]
        icon=symbolsCopy[random.randint(0, len(symbolsCopy)-1)]
        symbolsCopy.remove(icon)
        icons.append(icon)
        icons.append(icon)
    random.shuffle(icons)
    return icons
        

        



# 1. choose_difficulty_level
def choose_difficulty_level():
    difficulty= input('''Choose difficulty:
1 - Easy (4 x 4)
2 - Medium (6 x 4)
3 - Hard (8 x 6)
> ''')
    while not difficulty in ["1","2","3"]:
        difficulty=input('''Invalid choice. Enter 1, 2, or 3.
Choose difficulty:
1 - Easy (4 x 4)
2 - Medium (6 x 4)
3 - Hard (8 x 6)
> ''')
    
    sizes=[(4,4),(6,4), (8,6)]
    return sizes[int(difficulty)-1]

    


#####################################################
################ MAIN PROGRAM HERE ##################
#####################################################
play_game()