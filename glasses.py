from threading import Thread
import math
import numpy as np
import random
import tkinter as tk
import time


from PIL import Image

root = tk.Tk()

root.geometry("300x300+2000-1000")
root.state('zoomed')

width = 2500
height = 1080
win = tk.Canvas(root,width=width ,height=height,borderwidth=0)
win['bg'] = '#000000'

win.pack()

angle = 30

class VerticleBox:
    def __init__(self, topLeft, topRight = None):
        self.angle = -7 * math.pi / 180
        self.topLeft = topLeft
        self.w = random.randint(50,75)
        self.h = random.randint(50,90)
        self.topRight = [topLeft[0] + (math.cos(self.angle) * (self.w)), topLeft[1] + (math.sin(self.angle) * (self.w )) ] if topRight is None else topRight
        self.bottomLeft = [self.topLeft[0] + (self.h * math.sin(self.angle)), self.topLeft[1] + (self.h * math.cos(self.angle))]
        self.bottomRight = [self.topRight[0] + (self.h * math.sin(self.angle)), self.topRight[1] + (self.h * math.cos(self.angle))]

class HorizontalBox:
    def __init__(self, topLeft, topRight = None, angle = None):
        self.angle = 30 * math.pi / 180 if angle is None else angle * math.pi / 180
        self.topLeft = topLeft
        self.w = random.randint(50,75)
        self.h = random.randint(50,120)
        self.topRight = [topLeft[0] + (math.cos(-self.angle) * (self.w)), topLeft[1] + (math.sin(-self.angle) * (self.w )) ] if topRight is None else topRight
        self.bottomLeft = [self.topLeft[0] + (self.h * math.cos(self.angle)), self.topLeft[1] + (self.h * math.sin(self.angle))]
        self.bottomRight = [self.topRight[0] + (self.h * math.cos(self.angle)), self.topRight[1] + (self.h * math.sin(self.angle))]

def draw(block, color):
    a = win.create_line(block.topLeft[0],block.topLeft[1],block.topRight[0], block.topRight[1], fill=color)
    b = win.create_line(block.topLeft[0],block.topLeft[1],block.bottomLeft[0], block.bottomLeft[1], fill=color)
    c = win.create_line(block.topRight[0],block.topRight[1],block.bottomRight[0], block.bottomRight[1], fill=color)
    d = win.create_line(block.bottomLeft[0],block.bottomLeft[1],block.bottomRight[0], block.bottomRight[1], fill=color)
    win.update()
    time.sleep(0.1)

startX = 20
startY = 20
numRows = 50
first = 20
reset = True
col = ["green", "blue", "red", "yellow", "white", "cyan", "purple", "pink", ]
i = 0
for r in range(numRows):
    x,y = startX, random.randint(10,50) + startY
    start = x
    blocks = random.randint(3,12)

    vert = random.choice([True,False])
    topLeft = [x,y]
    topRight = None

    for b in range(blocks):
        if vert:
            block = VerticleBox(topLeft=topLeft, topRight=topRight)
       
        else:
            block = HorizontalBox(topLeft=topLeft, topRight=topRight)

        draw(block, col[i])

        if reset:
            first = block.topLeft[0]
            reset = False

        startX, startY = block.bottomRight[0], block.bottomRight[1]

        topLeft = block.bottomLeft
        topRight = block.bottomRight

        vert = not vert
    
    if startY > height:
        startX = first + random.randint(200,220)
        startY = random.randint(20,100)
        reset = True
        i = (i + 1) % len(col)
    

root.mainloop()