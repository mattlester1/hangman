#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 08:36:53 2021

@author: mattlester
"""
import random as rd


states = ["idaho", "utah", "california", "new york", "florida", "washington", "oregon", "ohio", "new jersey", "north dakota", "south dakota", "iowa", "kansas"]
holidays = ['christmas', 'thanksgiving', 'easter', 'forth of july', 'halloween', 'new years']
movies = ['top gun', 'mission impossible', 'jack reacher', 'days of thunder', 'red notice', 'titanic', 'avengers', 'support your local sheriff', 'saving private ryan']
marvel = ['iron man', 'hulk', 'captain america', 'thor', 'black widow', 'black panther', 'vision', 'spiderman', 'hawkeye', 'superman', 'wonder woman']

catagories = [states, holidays, movies, marvel]

def hangman():
    wrong = 0
    stages = ["",
              "__________       ",
              "          |      ",
              "          O      ",
              "         /|\     ",
              "         / \     ",
              "                 "]
    print("Welcome to hangman")
    print('\n')
    cat = catagories[(int(input("pick catagory by selection a number("
                                "states = 0 "
                                "holidays = 1 "
                                "movies = 2 " 
                                "marvel superheros = 3):")))]
    word = rd.choice(cat)
    rletters =list(word)
    board = ["__"] * len(word)
    win = False
    print('\n')
    
    print('\n')
    print(" ".join(board))
    
    while wrong < len(stages) - 2:
        msg = ("Guess a letter: ")
        char = input(msg)
        
        if char in rletters:
            rplace = rletters.index(char)
            board[rplace] = char
            rletters[rplace] = '$'
            print(' '.join(board))
        else:
            wrong += 1
            print(" ".join(board))
            e = wrong + 1
            print("\n". join(stages[0:e]))
        if "__" not in board:
            print("You Win!!")
            win = True
            break
        
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("You Lose! It was {}.".format(word))
            
                         
