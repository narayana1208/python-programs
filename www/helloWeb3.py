'''Prompt the user for a name, and display a web page including the name,
taking the web page template from a file.'''

def fileToStr(fileName): # NEW
    """Return a string containing the contents of the named file."""
    fin = open(fileName); 
    contents = fin.read();  
    fin.close() 
    return contents

def makePage(templateFileName, substitutions): # NEW
    """Returns a string with substitutions into a format string taken
    from the named file.  The single parameter substitutions must be in
    a format usable in the format operation: a single data item, a
    dictionary, or an explicit tuple."""

    pageTemplate = fileToStr(templateFileName)
    return  pageTemplate % substitutions

def main():
    person = raw_input('Enter a name: ')  
    contents = makePage('helloTemplate.html', person)   # NEW
    browseLocal(contents, 'helloPython3.html') # NEW filename

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
