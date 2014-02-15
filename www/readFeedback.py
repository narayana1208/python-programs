'''Process files from the generic surveyFeedback.cgi into a report.
Supply a parameter containing the survey base name.  Assume survey
form is  base+'survey.html', and responses from surveyFeedback.cgi in
subdirectory base+ 'Surveys'. The original survey is just used to
scrape out the names of fields in their original order.
    
Survey data in processed and formatted in two orders, first grouping all
responses by a respondent,and the second time throught the surveys
responses from all surveys to one question are grouped together.

If you want wrapped paragraphs, change cols to a positive number.
I dump the output into a word process document set up for multiple
narrow columns, which wraps automatically.
'''
import sys
import os
import os.path
import textwrap

WRAP = False
cols = 50 # limit on size of single line etries; if WRAP, used for wrapping

def str2file(str, filename):
    """ Make a string be a full file."""    
    f = open(filename, "w")
    f.write(str)
    f.close()

def file2str(filename):
    """ Return full file contents as a string."""    
    f = open(filename)
    str = f.read()
    f.close()
    return str

def getKeys(surveyBase = None):
    '''Default assumes current dir is surveyBase like 150 and survey doc
    is in form surveyBase + 'survey.html' like 150survey.html.
    '''
    if surveyBase is None: # operator is means same object; there is only 1 None
        surveyBase = os.path.basename(os.path.abspath("."))
    surveyFile = surveyBase + "survey.html"
    page = file2str(surveyFile)
    unique = []
    for piece in page.split('name="')[1:]: # pieces starting as specified
        name = piece.split('"', 1)[0] # piece up to '"' is the name
        if name not in unique: # keeps in same order, unlike a set
            unique.append(name)
    unique.remove('surveyBase') # this is a hidden ID field
    return surveyBase, unique

def printLongOrShort(name, val):
    '''Print name and value on one line if it all fits.  Otherwise
    put just name and dashes on the first line and the rest afterward,
    wrapping if cols > 0.'''
    if '\n' in val or '\r' in val or len(val)+ len(name) > cols-10:
        print (name +'-'*cols)[:cols - 15]
        if WRAP:
            print textwrap.fill(val, cols)
        else:
            print val  # if pasting into a wrapping wordprocessor
    else:
            print '>> ' + name + ': ' + val + '  <<'

    
def readData(surveyBase):
    '''return filename list, dict with filename keys of survey dictionaries.
    Assume surveys in direct subdir = surveyBase + 'Surveys'
    '''
    surveyDir = surveyBase+ 'Surveys'
    if not os.path.isdir(surveyDir):
        sys.exit('Expect directory %s  Aborting.' % surveyDir)
    names = os.listdir(surveyDir)
    names.sort()
    allDict = dict()
    for name in names:
        fPath = os.path.join(surveyDir, name) # file path with dir and file
        # eval takes the string form of the dictionary and recreates the dict
        allDict[name] = eval(file2str(fPath)) # as a value in the allDict dict!   
    return names, allDict

def byRespondent(allDict, names, keys):
    print '\nSurveys by Respondent'
    for name in names:
        ans1 = allDict[name]   
        print '\n', (name + '='*cols)[:cols-20]
        for key in keys:
            val = ans1.get(key)
            if isinstance(val, list):
                val = val.__repr__()
            if val is not None and val.strip():
                printLongOrShort(key, val.strip())

def byTopic(allDict, names, keys):
    print '\n\nSurveys by Topic'
    for key in keys:
        print "\n%s ======================" % key 
        for name in names:
            ans1 = allDict[name]    
            val = ans1.get(key)
            if isinstance(val, list):
                val = val.__repr__()
            if val is None or not val.strip():
                val = 'NO-ANS'
            printLongOrShort(name, val.strip())

def main(args):  # dump data by student and by topic
    surveyBase = None;
    if args:
        surveyBase = args[0]
    else:
        surveyBase = raw_input(
            'Enter the survey base name, ot just press enter for help: ')
    if not surveyBase:
        print helpMessage
        return
    surveyBase, keys = getKeys(surveyBase)
    names, allDict = readData(surveyBase)
    print surveyBase, 'Surveys by Respondent and then by Topic'
    byRespondent(allDict, names, keys)
    byTopic(allDict, names, keys)

helpMessage = '''
Usage:  readFeedback.py surveyBase
    If surveyBase is left out, you are prompted for it.
    The script assumes:
       the directory surveyBase + "Surveys' was populated by surveyFeedback.cgi.
       the original survey form is in surveyBase + "survey.html".
    Output is all the survey data in two formats, first by respondent, and
    second by survey form field names.'''

if __name__ == '__main__':  
    main(sys.argv[1:]) # this allows a commandline parameter for the base name
