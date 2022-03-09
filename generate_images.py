# -*- coding: utf-8 -*-

import cv2
import numpy as np 
import os



# Loading images of white 7 black pieces into the arrays
wsqs = []
bsqs = []

for img in os.listdir('images//processed//white_square//'):
    wsqs.append(cv2.imread('images//processed//white_square//' + img))

for img in os.listdir('images//processed//black_square//'):
    bsqs.append(cv2.imread('images//processed//black_square//' + img))
    
def generate_board(blank_prob=0.7):
    '''
    Generates a chess board with random pieces on each square.
    
    args:
        blank_prob: probability the square is blank
        
    returns:
        chess board in form of a numpy array
    '''
    
    piece_prob = (1 - blank_prob) / 12
    parity = 1
    
    blank_board = np.zeros((77*8, 77*8, 3), dtype=np.uint8)
    for x in range(8):
        parity *= -1
        for y in range(8):
            parity *= -1  # Different color square now
            if parity == 1: # If white square
            # Select image from wsqs, bias probability for empty square
                square = np.random.choice(
                    range(13),
                    p = [piece_prob for i in range(12)] + [blank_prob])
                blank_board[
                    x*77 : (x+1)*77, (y*77): (y+1)*77, :
                ] = wsqs[square]
            else: # If black square
            # Select image from wsqs, bias probability for empty square 
                square = np.random.choice(
                    range(13),
                    p = [piece_prob for i in range(12)] + [blank_prob])
                blank_board[
                    x*77 : (x+1)*77, y*77: (y+1)*77, :
                ] = bsqs[square]
      
    return blank_board

def si(img):
    '''function to show image. Press 0 to close'''
    
    cv2.imshow('image',img)
    import time
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return


si(generate_board())

