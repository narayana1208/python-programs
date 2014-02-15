#!/usr/bin/python

from os import getcwd, listdir, stat as osStat
from os.path import exists, splitext, join as osJoin, split as osSplit
from time import time as curTime, localtime, strftime
from stat import S_IMODE, S_ISREG, S_ISDIR
import cgi

def main():
    startTime = curTime()
    
    EXCLUDED_FILES = ['index.cgi', '.metadata', 'cgi-bin']
    EXCLUDED_EXTS = ['.swp']
    EXCLUDED_PREFIXES = ['.']
    EXCLUDED_SUFFIXES = ['~']
    METADATA = '.metadata'
    INDEX_METADATA = osJoin(METADATA,'index.cgi')
    toPrint = []

    if exists(INDEX_METADATA):
        try:
            f = open(INDEX_METADATA)
            title_text = f.readlines()
            f.close()
        except:
            title_text = "Failed to read metadata %s" % INDEX_METADATA
    else:
        (parent, curdir) = osSplit(getcwd())
        title_text = ["Directory Index of %s" % curdir]    

    toPrint.append("""
    <html>
    <title>%s</title>
    <body>

    <h1>%s</h1>
    <p>%s</p>
    <hr/>
    """ % (title_text[0], title_text[0], '\n<br/>'.join(title_text[1:])))

    form = cgi.FieldStorage() 
    byDate = int(form.getfirst("byDate",0))
    otherIndex = 1 - byDate
    otherOrder = ("Name", "Date")[otherIndex]
    toPrint.append("""<a href="..">Parent Directory</a> &nbsp; &nbsp; &nbsp;
          &nbsp; &nbsp; &nbsp; <a href="index.cgi?byDate=%d">Sort By %s</a><br/>
          """ % (otherIndex, otherOrder) )

    contents = listdir('.')
    contents.sort()
    entries = []
    for item in contents:
       if item[0] in EXCLUDED_PREFIXES:
           continue
       if item[-1] in EXCLUDED_SUFFIXES:
           continue
       if item in EXCLUDED_FILES:
           continue
       (name, ext) = splitext(item)
       if ext in EXCLUDED_EXTS: 
           continue

       st = osStat(item) 
       mode = st.st_mode
       if not S_IMODE(mode) & 4: # readable by others
           continue
       mtime = st.st_mtime
       mtimeStr = strftime("%c", localtime(mtime))
       if S_ISREG(mode):
           size = st.st_size
           if size < 1024:
                size = "%d B" % size
           elif size < 1024*1024:
                size = "%.1f KB" % (size/1024.0)
           else:
                size = "%.2f MB" % (size/(1024.0*1024.0))
           item_type = "file (%s)" % size
       elif S_ISDIR(mode):
           item_type = '<span style="color: rgb(255, 0, 0);">directory</span>'
       else:
           item_type = "unknown"
          
       data = '<a href="%s">%s</a> [%s  Modified: %s] ' % \
              (item, item, item_type, mtimeStr) 

       metafile = osJoin(METADATA, item)
       if exists(metafile):
           try:
               f = open(metafile)
               metadata = f.read()
               f.close()
           except:
               metadata = "metadata not readable"
           if metadata:
               data += '<br/><i>%s</i>' % metadata

       if byDate:
           entries.append((-mtime, item, data)) #extra fields for sorting
       else:
           entries.append(data)  # items already sorted
       
    if entries:
        if byDate:  #use extra sorting fields and then remove them
            entries.sort()
            entries = [entry[2] for entry in entries]
        toPrint.append('<ul>\n<li>%s</li>\n</ul>' % '</li>\n<li>'.join(entries))
    else:
        toPrint.append("<p>This directory contains no readable files.</p>")

    toPrint.append("""
    <hr/>
    Page generation time: %.2f seconds
    </body>
    </html>
    """ % (curTime() - startTime))
    print '\n'.join(toPrint)

try:
    print "Content-type: text/html\n\n" 
    main() 
except:
    cgi.print_exception()
