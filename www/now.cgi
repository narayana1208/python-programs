#!/usr/bin/python

import time
print "Content-Type: text/html\n\n"  # html markup follows

timeStr = time.strftime("%c") # obtains current time

htmlFormat = """
<html>
  <Title>The Time Now</Title>
<body>
  <p>The current Central date and time is:  %s</p>
</body>
</html> """

print htmlFormat % timeStr # see embedded %s ^ above


