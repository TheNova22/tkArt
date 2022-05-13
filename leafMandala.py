import math
import numpy as np
import random
import tkinter as tk
import time

from PIL import Image

root = tk.Tk()

width = 500
height = 500
win = tk.Canvas(root,width=width ,height=height)
win.pack()

nLines = 12
angle = (2 * math.pi) / float(nLines)
lineAngles = [x for x in range(nLines)]
allLines = []
# Radius decreases each time
for radius in range((min(width,height) // 2) - 30,0,-50):
    # If ABC is a right angled triangle, with A and B being two points in the base and C on the top being a point on the hypotenuse
    # Let Angle(ABC) be 90 degree, and let Angle(BAC) = Angle(ACB) = 45 degrees
    # Theta will be the angle at which a line will be drawn with respect to the center
    for theta in lineAngles:
        # This line shall be the hyptenuse
        C = [(math.cos(theta * angle) * (radius)) + width / 2, (math.sin(theta* angle) * (radius )) + height / 2 ]
        # B is at the center
        B = [(width / 2),(height / 2)]
        # Since now we know C,B, we have to find A
        # A regular pythagorean formula wont do the job as it gives distance, but we want coordinates
        # You shall hence have to use some geometry to figure out the point. The below link explains it perfectly
        # https://math.stackexchange.com/questions/927802/how-to-find-coordinates-of-3rd-vertex-of-a-right-angled-triangle-when-everything
        
        # We want to make a leaf, and hence a leaf when split in center forms two traingles.
        # Due to this we shall find two A's
        # This is also directly achieved as a quadratic equation shall return two values
        x = (C[0] + B[1] + B[0] - C[1]) / 2
        A = [ x, C[1] - B[0] + x]
        xd = (C[0] - B[1] + B[0] + C[1]) / 2
        Ad = [xd,C[1] - xd + B[0]]
        # Create both the sides of the lead and smoothen it
        win.create_line(C[0],C[1],A[0],A[1],B[0],B[1],smooth=True)
        win.create_line(C[0],C[1],Ad[0],Ad[1],B[0],B[1],smooth=True)
        win.update()
    # time.sleep(1)



# Can save using this

# win.pack()
# win.update()
# win.postscript(file="file_name.eps", colormode='color')
# img = Image.open("file_name.eps")
# img.save('filename.png')

root.mainloop()