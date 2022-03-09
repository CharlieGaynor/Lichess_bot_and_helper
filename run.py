# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 19:39:28 2022

@author: Charl
"""

import cv2
import pyautogui
import numpy as np 
import torch
import torch.nn as nn

def si(img):
    '''function to show image. Press 0 to close'''
    
    cv2.imshow('image',img)
    import time
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return

capture = pyautogui.screenshot(region=(1920-1333, 1080-907, 720, 720))
board = cv2.cvtColor(np.array(capture), cv2.COLOR_RGB2BGR)
#si(board)
board.shape


new_board = cv2.resize(board, (77*8, 77*8))
#si(new_board)

class network(nn.Module):
    def __init__(self):
        
        super().__init__()
        self.l1 = nn.Linear(in_features=77*77*3, out_features=14)
#         self.l2 = nn.ReLU()
#         self.l3 = nn.Linear(in_features=10**2, out_features=14)
        
    def forward(self, x):
        return self.l1(x)
        # return self.l3(self.l2(self.l1(x)))
        
model = network()
model.load_state_dict(torch.load('models/basicbitch.pth'))
model.eval()

board = []
for x in range(8):
    for y in range(8):
        piece = new_board[(x) * 77: (x+1) * 77, (y) * 77: (y+1) * 77, :]
        piece2 = torch.tensor(piece, dtype=torch.float32)
        # piece2 = torch.flatten(piece2)
        # pred = model(piece2)
        # _, label = pred.max(-1)
        
        