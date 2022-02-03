import math
import numpy as np
import random
import tkinter as tk
root = tk.Tk()

width = 1080
height = 1080
win = tk.Canvas(root,width=width,height=height)
win.pack()


# Get all the points present in a line
def getLine(x1,y1,x2,y2):
    if x1==x2: ## Perfectly horizontal line
        return [(x1,i) for i in range(y1,y2,int(abs(y2-y1)/(y2-y1)))]
    else: ## More of a problem, ratios can be used instead
        if x1>x2: ## If the line goes "backwards", flip the positions, to go "forwards" down it.
            x=x1
            x1=x2
            x2=x
            y=y1
            y1=y2
            y2=y
        slope=(y2-y1)/(x2-x1) ## Calculate the slope of the line
        line=[]
        i=0
        while x1+i < x2: ## Keep iterating until the end of the line is reached
            i+=1
            line.append((x1+i,y1+slope*i)) ## Add the next point on the line
        return line ## Finally, return the line

def draw():
    # Store the lines(Only the horizontal ones i.e. those that go from left to right) generated as a matrix here
    lines = []
    # Set up necesary border and offset to help iterate through the grid
    border = 50
    border_sQ = border*2
    num_lines = 20
    y_step = float((height-border_sQ)/num_lines)
    x_step = float((width-border_sQ)/num_lines)
    y_offset = y_step/2.0 
    x_offset = x_step/2.0
    totLines = num_lines
    for i in range(totLines):
        for j in range(totLines - 1):
            if j == 0:
                # If its the first line, generate two points with random angle offset
                p1 = [x_step*j + x_offset + random.uniform(-x_offset,x_offset) + border,y_step*i + y_offset + random.uniform(-y_offset,y_offset) + border]
                p2 = [x_step*(j+1) + x_offset + random.uniform(-x_offset,x_offset) + border,y_step*i + y_offset + random.uniform(-y_offset,y_offset) + border ]
                lines.append([])
                lines[-1].append([p1,p2])
            else:
                # Else the first point will be the same as the previous line's last point
                # So only generate second point
                p1 = lines[-1][-1][1]
                p2 = [x_step*(j+1) + x_offset + random.uniform(-x_offset,x_offset) + border,y_step*i + y_offset + random.uniform(-y_offset,y_offset) + border ]
                lines[-1].append([p1,p2])
    # Connectors connect each block together
    connectors = []
    # Interpolaters are the lines that are drawn in each block
    interp = []
    for i in range(len(lines) - 1):
        ct = 0
        if i < len(lines) / 3:
            ct = 6
        elif i < len(lines) / 1.5:
            ct = 3
        else: ct = 1
        for j in range(len(lines[0])):
            # Make a connector
            p1 = lines[i][j][0]
            p2 = lines[i + 1][j][0]
            connectors.append([p1,p2])
            line1From = p1
            line1To = lines[i][j][1]
            # Generate all points for both the lines and then randomly connect them
            points1 = getLine(line1From[0],line1From[1],line1To[0],line1To[1])
            line2From = p2
            line2To = lines[i + 1][j][1]
            points2 = getLine(line2From[0],line2From[1],line2To[0],line2To[1])
            k = 0
            if len(points1) > len(points2): points1,points2 = points2,points1
            while k < min(len(points1),len(points2)):
                p1 = [points1[k][0],points1[k][1]]
                p2 = [points2[k][0],points2[k][1]]
                interp.append([p1,p2])
                k += random.randint(ct,ct*3)
            
        p1 = lines[i][-1][1]
        p2 = lines[i + 1][-1][1]
        connectors.append([p1,p2])

    # Draw the horizontal lines
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            win.create_line(lines[i][j][0][0],lines[i][j][0][1],lines[i][j][1][0],lines[i][j][1][1])
            win.update()
    
    # Draw the connectors
    for l in connectors:
        win.create_line(l[0][0],l[0][1],l[1][0],l[1][1])
        win.update()

    # Draw the interpolators
    for l in interp:
        win.create_line(l[0][0],l[0][1],l[1][0],l[1][1])
        win.update()
    
draw()

# Can save using this

# win.pack()
# win.update()
# win.postscript(file="file_name.eps", colormode='color')
# img = Image.open("file_name.eps")
# img.save('filename.png')

root.mainloop()