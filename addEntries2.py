"""Example with two Entry objects and type conversion.
Version 2 with a function.
Do addition.
"""

from graphics import *

def makeLabeledEntry(entryCenterPt, entryWidth, initialStr, labelText, win):
    '''Return an Entry object with specifed center, width in characters, and
    initial string value.  Also create a static label over it with
    specified text.  Draw everything in the GraphWin win.
    '''
    
    entry = Entry(entryCenterPt, entryWidth)
    entry.setText(initialStr)
    entry.draw(win)

    labelCenter = entryCenterPt.clone()
    labelCenter.move(0, 30)
    Text(labelCenter,labelText).draw(win)
    return entry

        
def main():
    winWidth = 300
    winHeight = 300
    
    win = GraphWin("Addition", winWidth, winHeight)
    win.setCoords(0,0, winWidth, winHeight)

    instructions = Text(Point(winWidth/2, 30),
                     "Enter two numbers.\nThen click the mouse.")
    instructions.draw(win)

    entry1 = makeLabeledEntry(Point(winWidth/2, 250), 25,
                              '0', 'First Number:', win)
    entry2 = makeLabeledEntry(Point(winWidth/2, 180), 25,
                              '0', 'Second Number:', win)
     
    win.getMouse()  # To know the user is finished with the text.

    num1 = int(entry1.getText())
    num2 = int(entry2.getText())

    result = "The sum of\n%s\nplus\n%s\nis %s." % (num1, num2, num1+num2)
    Text(Point(winWidth/2, 110), result).draw(win)                     
    
    instructions.setText("Click anywhere to quit.")
    win.getMouse()
    win.close()

main()
