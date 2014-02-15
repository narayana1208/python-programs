'''Program: makeRectangle.py
Demonstrate the use of the clone method in a function makeRect, which
takes a ctakes a corner point and dimensions to construct a Rectangle.
'''

from graphics import *

def makeRect(corner, width, height):
    '''Return a new Rectangle given one corner Point and the dimensions.'''
    
    corner2 = corner.clone()  # !! Note the .clone()  !!
    corner2.move(width, height)
    return Rectangle(corner, corner2)

def main():
    winWidth = 300
    winHeight = 300
    win = GraphWin('Draw a Rectangle', winWidth, winHeight)
    win.setCoords(0, 0, winWidth, winHeight) # right side up coordinates

    rect = makeRect(Point(20, 50), 250, 200)
    rect.draw(win)
    
    # Wait for another click to exit
    msg = Text(Point(winWidth/2, 20),'Click anywhere to quit.')
    msg.draw(win)
    win.getMouse()
    win.close()

main()
