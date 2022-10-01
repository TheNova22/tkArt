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
win.pack()

angle = 30

class VerticleBox:
    def __init__(self, topLeft, topRight = None):
        self.angle = -7 * math.pi / 180
        self.topLeft = topLeft
        self.w = random.randint(50,75)
        self.h = random.randint(50,120)
        self.topRight = [topLeft[0] + (math.cos(self.angle) * (self.w)), topLeft[1] + (math.sin(self.angle) * (self.w )) ] if topRight is None else topRight
        self.bottomLeft = [self.topLeft[0] + (self.h * math.sin(self.angle)), self.topLeft[1] + (self.h * math.cos(self.angle))]
        self.bottomRight = [self.topRight[0] + (self.h * math.sin(self.angle)), self.topRight[1] + (self.h * math.cos(self.angle))]

class HorizontalBox:
    def __init__(self, topLeft, topRight = None, angle = None):
        self.angle = 30 * math.pi / 180 if angle is None else angle * math.pi / 180
        self.topLeft = topLeft
        self.w = random.randint(50,120)
        self.h = random.randint(50,75)
        self.topRight = [topLeft[0] + (math.cos(-self.angle) * (self.w)), topLeft[1] + (math.sin(-self.angle) * (self.w )) ] if topRight is None else topRight
        self.bottomLeft = [self.topLeft[0] + (self.h * math.cos(self.angle)), self.topLeft[1] + (self.h * math.sin(self.angle))]
        self.bottomRight = [self.topRight[0] + (self.h * math.cos(self.angle)), self.topRight[1] + (self.h * math.sin(self.angle))]

def draw(block):
    a = win.create_line(block.topLeft[0],block.topLeft[1],block.topRight[0], block.topRight[1])
    b = win.create_line(block.topLeft[0],block.topLeft[1],block.bottomLeft[0], block.bottomLeft[1])
    c = win.create_line(block.topRight[0],block.topRight[1],block.bottomRight[0], block.bottomRight[1])
    d = win.create_line(block.bottomLeft[0],block.bottomLeft[1],block.bottomRight[0], block.bottomRight[1])
    win.update()
    time.sleep(0.1)

startX = 20
startY = 20
numRows = 25
first = 20
reset = True
for r in range(numRows):
    x,y = random.randint(10,20) + startX, random.randint(10,50) + startY
    start = x
    blocks = random.randint(3,6)

    vert = random.choice([True,False])
    topLeft = [x,y]
    topRight = None

    for b in range(blocks):
        if vert:
            block = VerticleBox(topLeft=topLeft, topRight=topRight)
       
        else:
            block = HorizontalBox(topLeft=topLeft, topRight=topRight)

        draw(block)

        if reset:
            first = block.topLeft[0]
            reset = False

        startX, startY = block.bottomRight[0], block.bottomRight[1]

        topLeft = block.bottomLeft
        topRight = block.bottomRight

        vert = not vert
    
    if startY > height:
        startX = first + random.randint(200,250)
        startY = random.randint(20,100)
        reset = True
    

root.mainloop()