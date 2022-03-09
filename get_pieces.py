# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

'''
Connect 4:
    
    Observation space: 6x7 grid of -1 / 0 / 1
    action space
'''

import numpy as np 
import cv2
import os
# print(os.listdir('images\\png\\'))
import pyautogui

# for im in os.listdir('images\\png\\'):
#     img = cv2.imread('images\\png\\' + im)
#     # cv2.imshow('image',img)
#     # cv2.waitKey(0)
#     # cv2.destroyAllWindows()
#     print(img.shape)

def si(img):
    '''function to show image. Press 0 to close'''
    
    cv2.imshow('image',img)
    import time
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return

# bs = cv2.imread('images\\png\\board_sample.png')
# bs.shape
# # Unique white color of board
# bs[2, 0 , :]
# # Unique brown color of board
# bs[2, -1, :]

# # (944, 907, 616, 616))

#capture = pyautogui.screenshot(region=(1920 - 963, 1080 - 940, 656, 656))

board_size = 616
# capture = pyautogui.screenshot(region=(1920 - 963, 1080 - 843, board_size, board_size))
capture = pyautogui.screenshot(region=(1920-1329, 1080-853, board_size, board_size))

board = cv2.cvtColor(np.array(capture), cv2.COLOR_RGB2BGR)
si(board)
board = cv2.resize(board, (616, 616))
si(board)

sq = int(board_size/8)
# Kings
wkw = board[: sq, : sq, :]
wkb = board[: sq, sq: sq*2, :]
bkw = board[: sq, sq*2: sq*3, :]
bkb =board[: sq, sq*3: sq*4, :]

# Queens
wqb = board[sq: sq*2, : sq, :]
wqw = board[sq: sq*2, sq: sq*2, :]
bqb = board[sq: sq*2, sq*2: sq*3, :]
bqw = board[sq: sq*2, sq*3: sq*4, :]
  
# Rooks
wrw = board[sq*2: sq*3, : sq, :]
wrb = board[sq*2: sq*3, sq: sq*2, :]
brw = board[sq*2: sq*3, sq*2: sq*3, :]
brb = board[sq*2: sq*3, sq*3: sq*4, :]

# Bishops
wbb = board[sq*3: sq*4, : sq, :]
wbw = board[sq*3: sq*4, sq: sq*2, :]
bbb = board[sq*3: sq*4, sq*2: sq*3, :]
bbw = board[sq*3: sq*4, sq*3: sq*4, :]

# (k)Nights
wnw = board[sq*4: sq*5, : sq, :]
wnb = board[sq*4: sq*5, sq: sq*2, :]
bnw = board[sq*4: sq*5, sq*2: sq*3, :]
bnb = board[sq*4: sq*5, sq*3: sq*4, :]

# Pawns
wpb = board[sq*5: sq*6, : sq, :]
wpw = board[sq*5: sq*6, sq: sq*2, :]
bpb = board[sq*5: sq*6, sq*2: sq*3, :]
bpw = board[sq*5: sq*6, sq*3: sq*4, :]

#si(wpb)

# Saving black pieces
# ws_pieces = [wkw, bkw, wqw, bqw, wrw, brw, wbw, bbw, wnw, bnw, wpw, bpw]
# ws_names = ['wkw', 'bkw', 'wqw', 'bqw', 'wrw', 'brw',
#             'wbw', 'bbw', 'wnw', 'bnw', 'wpw', 'bpw']


# type(wkw)
# for piece, name in zip(ws_pieces, ws_names):       
#     # print(piece, name)
#     cv2.imwrite(f'images//processed/white_square//{name}.png', piece) 

# # Saving white pieces
# bs_pieces = [wkb, bkb, wqb, bqb, wrb, brb, wbb, bbb, wnb, bnb, wpb, bpb]
# bs_names = ['wkb', 'bkb', 'wqb', 'bqb', 'wrb', 'brb',
#             'wbb', 'bbb', 'wnb', 'bnb', 'wpb', 'bpb']
# type(wkw)
# for piece, name in zip(bs_pieces, bs_names):       
#     # print(piece, name)
#     cv2.imwrite(f'images//processed/black_square//{name}.png', piece)


# white_square = board[sq*6: sq*7, sq*4: sq*5, :]
# black_square = board[sq*6: sq*7, sq*5: sq*6, :]

# cv2.imwrite(f'images//processed/white_square//z_wsquare.png', white_square)
# cv2.imwrite(f'images//processed/black_square//z_bsquare.png', black_square)



