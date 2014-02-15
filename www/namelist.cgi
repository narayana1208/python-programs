#!/usr/bin/python

import cgi

DEFAULT_NAME = "no name"
DEFAULT_ADDR = "nowhere"

def main():
    form = cgi.FieldStorage()   
    
    name = form.getfirst("name", DEFAULT_NAME)
    addr = form.getfirst("addr", DEFAULT_ADDR)
	
    contents = processInput(name, addr)   
    print contents
    
def processInput(name, addr):  
    '''Process input parameters and return the final page as a string.'''
    fileName= "namelist.txt"
    if name != DEFAULT_NAME or addr != DEFAULT_ADDR:
        line = "Name: %s  Address:  %s\n" % (name, addr)
        append(fileName, line)
    lines = fileLinesToHTMLLines(fileName)
    return makePage("nameListOutput.html", lines ) 

def append(fileName, s):
    """Append string s to file with name fileName.
    This fails if there are multiple people trying simultaneously.
    """
    fout = open(fileName,'a') # 'a' means append to the end of the file
    fout.write(s)
    fout.close()

def safePlainText(s):
    '''Return string s with reserved html markup characters replaced
    and newlines replaced by <br>.'''
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('\n', '<br>')

def fileLinesToHTMLLines(fileName):
    """Allow lines of the file with name fileName to be embedded in html.
    This fails if there are multiple people trying."""
    
    lines = fileToStr(fileName).splitlines()
    safeLines = list()
    for line in lines:
        safeLines.append(safePlainText(line))
    return "<br>\n".join(safeLines)

# standard functions and code from here on
def fileToStr(fileName): 
    """Return a string containing the contents of the named file."""
    fin = open(fileName); 
    contents = fin.read();  
    fin.close() 
    return contents

def makePage(templateFileName, substitutions): 
    """Returns a string with substitutions into a format string taken
    from the named file.  the single parameter substitutions must be in
    a format usable in the format operation: a single data item, a
    dictionary, or an explicit tuple."""

    pageTemplate = fileToStr(templateFileName)
    return  pageTemplate % substitutions

try:
    print "Content-type: text/html\n\n"   # say generating html
    main() 
except:
    cgi.print_exception()                 # catch and print errors
