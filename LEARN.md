## What is tkArt?
tkArt is an accumulation of python programs made using _tkinter_, a standard GUI library for Python.

Each program is written to create a type of art/image using general programming knowledge and coordinate geometry.

## Python
You can download and set up your python using the instructions given [here](https://wiki.python.org/moin/BeginnersGuide/Download).

To know the basics and understand the data structure usage in Python, a good start will be to view the [freeCodeCamp tutotial](https://www.youtube.com/watch?v=rfscVS0vtbw) on Python Basics.

## Tkinter
_tkinter_ is a standard GUI package that comes preinstalled with the default python library.

You can go through the documentation [here](https://docs.python.org/3/library/tkinter.html).

Below, we shall also go through the basic workings of it.

### Initialisation
Every program that uses tkinter shall begin with an import statement.
```python
import tkinter as tk
```

Generally each tkinter program begins with definition of the root. This shall be responsible for creating a root window.

```python
root = tk.Tk()
```

To set up UI instances and get events like clicks, etc, tkinter provides a method that shall set everything in a while loop until the window gets closed. This is referred to as mainloop and is generally implemented in a tkinter program.

```python
root.mainloop()
```

A root shall contain a Canvas, this will act as a drawing board on which lines, circles, etc will be drawn.
We also call a method called _pack()_ which shall manage widget organisation in blocks before placing them in the parent widget.

```python
width = 500
height = 500
win = tk.Canvas(root,width=width,height=height)
win.pack()
```

