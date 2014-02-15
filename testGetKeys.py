'''Test the function to extract keys from a format string for a dictionary.'''

def getKeys(formatString):
    '''formatString is a format string with embedded dictionary keys.
    Return a list containing all the keys from the format string.'''

    keyList = list()
    end = 0
    repetitions = formatString.count('%(')
    for i in range(repetitions):
        start = formatString.find('%(', end) + 2
        end = formatString.find(')', start)
        key = formatString[start : end]
        keyList.append(key)
    return keyList

originalStory = """
Once upon a time, deep in an ancient jungle,
there lived a %(animal)s.  This %(animal)s
liked to eat %(food)s, but the jungle had
very little %(food)s to offer.  One day, an
explorer found the %(animal)s and discovered
it liked %(food)s.  The explorer took the
%(animal)s back to %(city)s, where it could
eat as much %(food)s as it wanted.  However,
the %(animal)s became homesick, so the
explorer brought it back to the jungle,
leaving a large supply of %(food)s.

The End
"""

print getKeys(originalStory)
