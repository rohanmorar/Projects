#!/usr/bin/env python
# coding: utf-8

# In[3]:


from IPython.display import clear_output

def display_board(board):
    clear_output()
    print(board[1]+"|"+board[2]+"|"+board[3])
    print("=====")
    print(board[4]+"|"+board[5]+"|"+board[6])
    print("=====")
    print(board[7]+"|"+board[8]+"|"+board[9])


# In[4]:


test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)


# In[5]:


def player_input():
    
    marker = ""
    
    #KEEP ASKING PLAYER 1 TO CHOOSE X OR O 
    
    while marker != "X" and marker != "O": 
        marker = input("Player 1, choose X or O: ")
    
    #ASSIGN Player 2 the opposite marker
    player1 = marker
    
    if player1 == "X":
        player2 = "O"
    else:
        player2 = "X"
        
    return (player1,player2)


# In[ ]:


player_input()


# In[ ]:


def place_marker(board, marker, position):
    board[position] = marker


# In[ ]:


place_marker(test_board,'$',8)
display_board(test_board)


# In[ ]:


def win_check(board, mark):
    
    #Win tic tac toe?
    
    #All rows, check to see if they all share the same marker
    return((board[1] == mark and board[2] == mark and board[3] == mark) or 
    (board[4] == mark and board[5] == mark and board[6] == mark) or 
    (board[7] == mark and board[8] == mark and board[9] == mark) or 
    #All collums, check match
    (board[1] == mark and board[4] == mark and board[7] == mark) or 
    (board[2] == mark and board[5] == mark and board[8] == mark) or 
    (board[3] == mark and board[6] == mark and board[9] == mark) or 
    
    #All diagonals, check match
    (board[1] == mark and board[5] == mark and board[9] == mark) or 
    (board[3] == mark and board[5] == mark and board[7] == mark))


# In[ ]:


win_check(test_board,'X')


# In[ ]:


import random

def choose_first():
    coin_flip = random.randint(0,1)
    if coin_flip == 0:
        return "Player 1"
    else:
        return "Player 2"
        


# In[ ]:


choose_first()


# In[ ]:


def space_check(board, position):
    return board[position] == " "


# In[ ]:


def full_board_check(board):
    
    for i in range(1,10):
        if space_check(board,i):
            return False
        else:
            return True


# In[ ]:


def player_choice(board):
    
    position = 0
    
    while position not in range(1,10) or not space_check(board,position):
        position = int(input("Choose a position (1-9) "))
    
    return position


# In[ ]:


def replay():
    choice = input("Do you want to play again? Type Yes or No")
    
    return choice == "Yes"


# In[ ]:


print('Welcome to Tic Tac Toe!')

while True:
    # Set the game up here: Board > Whos First > Choose markers.
    the_board = [" "]*10
    player1_marker,player2_marker = player_input()
    
    turn = choose_first()
    print(turn + " will go first. ")
    
    play_game = input("Ready to play? Enter: y or n?")
    
    if play_game == "y":
        game_on = True
    else:
        game_on = False

    while game_on:
        
        if turn == "Player 1":
            
            #show the board
            display_board(the_board)
            #Choose position
            position = player_choice(the_board)
            #Place marker on position
            place_marker(the_board,player1_marker,position)
            
            
            #Why do we put board,player1_marker
            #Check if they won
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print("Player 1 has WON!")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("It's a tie!")
                    game_on = False
                else:
                    turn = "Player 2"
        
        else:
            #show the board
            display_board(the_board)
            #Choose position
            position = player_choice(the_board)
            #Place marker on position
            place_marker(the_board,player2_marker,position)
            
            
            #Why do we put board,player1_marker
            #Check if they won
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print("Player 2 has WON!")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("It's a tie!")
                    game_on = False
                else:
                    turn = "Player 1"
                    
             #Why do we put board,player1_marker
            #pass

    if not replay():
        break


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




