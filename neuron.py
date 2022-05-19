from threading import Thread
import math
import numpy as np
import random
import tkinter as tk
import time


from PIL import Image

root = tk.Tk()

root.geometry("300x300-1000-1000")
root.state('zoomed')

width = 1080
height = 1080
win = tk.Canvas(root,width=width ,height=height,borderwidth=0)
win.pack()

threadRunning = []

dirs = [[1,-1],[0.5,-1],[1,-0.5],[0.12,-0.5]]

colors = ['#fc973f','#b0feff', '#fff2b0', "#59995c"]


tot = 0


class Neuron:
    def __init__(self, startPoint, branchRate, totLines):

        self.startPoint = startPoint

        self.branchRate = branchRate

        self.totLines = totLines

        self.ct = totLines


    def brancher(self, window : tk.Canvas, direction, color : str):
        global tot

        x = self.startPoint[0]
        y = self.startPoint[1]

        while self.ct > 0:
            


            p3_x = x + int(direction[0] * self.branchRate *(random.randint(20,40)))
            p3_y = y + int(direction[1] * self.branchRate *(random.randint(20,40)))

            p2_x = (random.randint(x // 1,p3_x // 1) if p3_x > x else random.randint(p3_x // 1,x // 1)) + (random.randint((-10 * self.branchRate) // 1,(10 * self.branchRate) // 1)) 
            p2_y= (random.randint(p3_y // 1,y // 1) if p3_y < y else random.randint(y // 1,p3_y // 1)) + (random.randint((-30 * self.branchRate) // 1,(30 * self.branchRate) // 1))

            
                # if p2_x > p3_x:
                    
                #     Thread(target = newNode.brancher,args=[window, [1,1]]).start()
                
                # else: Thread(target = newNode.brancher,args=[window, [-1,1]]).start()


            window.create_line(x, y,p2_x,p2_y, p3_x, p3_y, smooth=True, fill = color)
            choice = random.randint(1,16)
            if choice == 1:
                print("in",choice,tot)
                if self.totLines > 5:
                    newNode = Neuron([p3_x // 1,p3_y // 1],self.branchRate * 0.6, int(self.totLines * 0.5))

                    if choice == 1:
                        threadRunning.append(Thread(target = newNode.brancher,args=[window, random.choice(dirs + [[1,1]]), color]))

                        threadRunning[-1].setDaemon(True)


                        threadRunning[-1].start()

                        tot += 1
                        print(tot)
                    # else: Thread(target = newNode.brancher,args=[window, [1,-1]]).start()
                # newNode.brancher(window,[1,-1])

            x = p3_x
            y = p3_y


            window.update()

            self.ct -= 1









k = 0

while k < len(dirs):

    n = Neuron([30,width - 30],0.9,80)


    threadRunning.append(Thread(target = n.brancher,args=[win, dirs[k],colors[k]]))

    threadRunning[-1].setDaemon(True)


    threadRunning[-1].start()

    tot += 1
     
    k += 1


root.mainloop()

# while True: pass