'''A simple test of the methods added to the graphics package for
the hands-on tutorials, so GraphWin objects can deal with the
last (previous) mouse click.
The animation stops when the mouse is clicked.
'''

from graphics import *
import time

win = GraphWin()

circle = Circle(Point(100,100), 15)
circle.draw(win)

Text(Point(100, 40), "Click to quit.").draw(win)

win.clearLastMouse()
while win.getLastMouse() == None:
    circle.move(50, 0)
    time.sleep(.5)
    circle.move(-50, 0)
    time.sleep(.5)

win.close()
