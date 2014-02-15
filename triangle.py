'''Program: triangle.py or triangle.pyw (best name for Windows)
Interactive graphics program to draw a triangle,
with prompts in a Text object and feedback via mouse clicks.
'''

from graphics import *

def main():
    winWidth = 300
    winHeight = 300
    win = GraphWin('Draw a Triangle', winWidth, winHeight)
    win.setCoords(0, 0, winWidth, winHeight) # right side up coordinates
    win.setBackground('yellow')
    message = Text(Point(winWidth/2, 20), 'Click on three points')
    message.draw(win)

    # Get and draw three vertices of triangle
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)
    vertices = [p1, p2, p3]

    # Use Polygon object to draw the triangle
    triangle = Polygon(vertices)
    triangle.setFill('gray')
    triangle.setOutline('cyan')
    triangle.setWidth(4)  # width of boundary line
    triangle.draw(win)

    # Wait for another click to exit
    message.setText('Click anywhere to quit.')
    message.setTextColor('red')
    message.setStyle('italic')
    message.setSize(20)
    win.getMouse()
    win.close()

main()
