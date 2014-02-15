"""Example with two Entry objects and type conversion.
Do addition.
"""

from graphics import *

def main():
    winWidth = 300
    winHeight = 300
    
    win = GraphWin("Addition", winWidth, winHeight)
    win.setCoords(0,0, winWidth, winHeight)

    instructions = Text(Point(winWidth/2, 30),
                     "Enter two numbers.\nThen click the mouse.")
    instructions.draw(win)

    entry1 = Entry(Point(winWidth/2, 250),25)
    entry1.setText('0')
    entry1.draw(win)

    Text(Point(winWidth/2, 280),'First Number:').draw(win)                   
    
    entry2 = Entry(Point(winWidth/2, 180),25)
    entry2.setText('0')
    entry2.draw(win)

    Text(Point(winWidth/2, 210),'Second Number:').draw(win)
    
    win.getMouse()  # To know the user is finished with the text.

    numStr1 = entry1.getText()
    num1 = int(numStr1)

    numStr2 = entry2.getText()
    num2 = int(numStr2)

    result = "The sum of\n%s\nplus\n%s\nis %s." % (num1, num2, num1+num2)
    Text(Point(winWidth/2, 110), result).draw(win)                     
    
    instructions.setText("Click anywhere to quit.")
    win.getMouse()
    win.close()

main()
