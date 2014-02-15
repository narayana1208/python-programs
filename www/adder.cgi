#!/usr/bin/python

import cgi   # NEW

def main(): # NEW except for the call to processInput
    form = cgi.FieldStorage()      # standard cgi script lines to here!
    
    # use format of next two lines with YOUR names and default data
    numStr1 = form.getfirst("x", "0") # get the form value associated with form
                                   # name 'x'.  Use default "0" if there is none. 
    numStr2 = form.getfirst("y", "0") # similarly for name 'y'
    contents = processInput(numStr1, numStr2)   # process input into a page
    print contents
    
def processInput(numStr1, numStr2):  
    '''Process input parameters and return the final page as a string.'''
    num1 = int(numStr1) # transform input to output data
    num2 = int(numStr2)
    total = num1+num2
    return makePage('additionTemplate.html', (num1, num2, total))

# standard functions and code from here on
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

try:   # NEW
    print "Content-type: text/html\n\n"   # say generating html
    main() 
except:
    cgi.print_exception()                 # catch and print errors


