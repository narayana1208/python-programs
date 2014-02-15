#!/usr/bin/python

# The form invoking this CGI script must include a hidden variable named
# surveyBase.  The value of the variable should not include spaces, and should
# be descriptive of the survey, like "pythonTutorial" or "COMP150".
# Then responses are stored in a subdirectory formed from the
# value of surveyBase + 'Surveys'.  All the stored results may be later
# formatted and printed with readFeedback.py.

import cgi
import os
import os.path
import random

def str2file(text, filename):
    """ Make a string be a full file."""    
    f = open(filename, "w")
    f.write(text)
    f.close()

def simplePage(msg, title = None):
    ''' generate a page with a specified title and message.'''
    print "<html>"
    if title == "":
        title = msg
    if title:
        print "<Title>%s</Title>" % title
    print """
             <body>
               <p>%s</p>
             </body>
          </html>"""  % msg

def main():
    form = cgi.FieldStorage() # standard cgi script lines to here!
    surveyBase = form.getfirst("surveyBase")
    surveyDir = surveyBase+'Surveys'
    if not os.path.isdir(surveyDir): # if no surveyDir
        os.mkdir(surveyDir)          #    make it the first time

    all = dict() # dictionary for form entry names and responses
    slash = os.sep # backward or forward slash string depending on OS
    for key in form:
        val = form.getlist(key) # returns values for key as a list
        if len(val) == 1: # generally there is just one value per key
            val = val[0]  #   if so I choose to display it without the list
        all[key] = val
        
    for i in range(5):  # Retry in case two processes want the same filename.
                        # Random file suffixes make clashes highly unlikely.
        try:            # (Databases handle this more neatly.)
            n = len(os.listdir(surveyDir)) # filename based on number of files
            filename = ("%s"+slash+"%02d-%02d.txt") % \
                       (surveyDir, n,random.randrange(100))
            str2file(all.__repr__(), filename) # save dictionary as a string
            simplePage("Thanks!<br>I appreciate your feedback.", "Thanks")
            return
        except:   # exception handling.  No code needed with return statement
            pass  #    until after the loop
    simplePage("Error saving data:<br>Back up and resubmit!", "Error")

	
#standard lines after here
try:
    print "Content-type: text/html\n\n" 
    main() 
except:
    cgi.print_exception()
