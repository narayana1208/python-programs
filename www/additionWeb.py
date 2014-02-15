'''Prompt the user for two integers and display a web page with the sum.'''

def processInput(numStr1, numStr2):  # NEW
    '''Process input parameters and return the final page as a string.'''
    num1 = int(numStr1) # transform input to output data
    num2 = int(numStr2)
    total = num1+num2
    return makePage('additionTemplate.html', (num1, num2, total))

def main(): # NEW
    numStr1 = raw_input('Enter an integer: ')  # obtain input
    numStr2 = raw_input('Enter another integer: ')  
    contents = processInput(numStr1, numStr2)   # process input into a page
    browseLocal(contents, 'helloPython3.html') # display page

def fileToStr(fileName): 
    """Return a string containing the contents of the named file."""
    fin = open(fileName); 
    contents = fin.read();  
    fin.close() 
    return contents

def makePage(templateFileName, substitutions): 
    """Returns a string with substitutions into a format string taken
    from the named file.  The single parameter substitutions must be in
    a format usable in the format operation: a single data item, a
    dictionary, or an explicit tuple."""

    pageTemplate = fileToStr(templateFileName)
    return  pageTemplate % substitutions

def strToFile(text, filename):
    """Write a file with the given name and the given text."""
    output = file(filename,"w")
    output.write(text)
    output.close()

def browseLocal(webpageText, filename):
    """Start your webbrowser on a local file containing the text."""
    strToFile(webpageText, filename)
    import webbrowser
    webbrowser.open(filename)

main()
