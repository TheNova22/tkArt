import math
import numpy as np
import random
import tkinter as tk
import time

from PIL import Image

root = tk.Tk()

# root.geometry("300x300-1000-1000")
# root.state('zoomed')


root.title("Kamui")

width = 500
height = 500
win = tk.Canvas(root, width=width, height=height, background="white")
win.pack()

nLines = 3
angle = (2 * math.pi) / float(nLines)
lineAngles = [x for x in range(nLines)]
allLines = []
points = []
C = []
inter = []
radius = (min(width, height) // 2) - 30

# B is at the center
B = [(width / 2), (height / 2)]

for i in range(len(lineAngles)):
    # This line shall be the hyptenuse
    C.append([(math.sin(lineAngles[i] * angle) * (radius)) + width / 2,
              (math.cos(lineAngles[i] * angle) * (radius)) + height / 2])

    j = (i - 1) % nLines
    A = [(math.sin(lineAngles[j] * angle) * (radius)) + width / 2,
         (math.cos(lineAngles[j] * angle) * (radius)) + height / 2]
    points.append([B[0] + (A[0]-B[0])/2, B[1] + (A[1]-B[1])/2])
    # print('{0} {1}'.format(math.sin(j), math.cos(j)))
    inter.append([points[i][0] + (C[i][0] - points[i][0])/2 + radius/3 * math.sin(lineAngles[j] * angle),
                 points[i][1] + (C[i][1] - points[i][1])/2 + radius/3 * math.cos(lineAngles[j] * angle)])

    # time.sleep(1)

win.create_oval(B[0]-radius, B[1]-radius, B[0] +
                radius, B[1]+radius, width=20, fill="#a6052d")
for i in range(len(lineAngles)):
    win.create_line(B[0], B[1], C[i][0], C[i]
                    [1], fill='black', smooth=True, width=20)

    cx = points[i][0] + (C[i][0] - points[i][0])/2 + \
        radius/3 * math.sin(lineAngles[(i - 1) % nLines] * angle)
    cy = points[i][1] + (C[i][1] - points[i][1])/2 + \
        radius/3 * math.cos(lineAngles[(i - 1) % nLines] * angle)
    win.create_line(C[i][0], C[i][1], cx, cy, points[i][0], points[i]
                    [1],  fill='black', smooth=True, width=20)

    cx = points[i][0] + (points[(i+1) % nLines][0] - points[i][0])/2 + \
        radius/5 * math.sin(lineAngles[(i - 1) % nLines] * angle)
    cy = points[i][1] + (points[(i+1) % nLines][1] - points[i][1])/2 + \
        radius/5 * math.cos(lineAngles[(i - 1) % nLines] * angle)

    win.create_line(points[(i+1) % nLines][0], points[(i+1) % nLines][1], cx, cy, points[i][0], points[i]
                    [1],  fill='black', smooth=True, width=20)

    win.create_oval(B[0]-10, B[1]-10, B[0]+10, B[1]+10, fill="#a6052d")
    win.update()


# Can save using this

# win.pack()
# win.update()
# win.postscript(file="file_name.eps", colormode='color')
# img = Image.open("file_name.eps")
# img.save('filename.png')

root.mainloop()
