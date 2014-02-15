"""
madlib2.py
Interactive display of a mad lib, which is provided as a Python format string,
with all the cues being dictionary formats, in the form %(cue)s.

In this version, the cues are extracted from the story automatically,
and the user is prompted for the replacements.

Original verison adapted from code of Kirby Urner
"""

def getKeys(formatString):
    '''formatString is a format string with embedded dictionary keys.
    Return a set containing all the keys from the format string.'''

    keyList = list()
    end = 0
    repetitions = formatString.count('%(')
    for i in range(repetitions):
        start = formatString.find('%(', end) + 2
        end = formatString.find(')', start)
        key = formatString[start : end]
        keyList.append(key) # may add duplicates

    return set(keyList) # removes duplicates: no duplicates in a set

def addPick(cue, dictionary):  # from madlib.py
    '''Prompt the user and add one cue to the dictionary.'''
    prompt = "Enter a specific example for %s: " % cue     
    dictionary[cue] = raw_input(prompt)

def getUserPicks(cues):
    '''Loop through the collection of cue keys and get user choices.
    Return the resulting dictionary.
    '''
    userPicks = dict()
    for cue in cues:
        addPick(cue, userPicks)
    return userPicks   

def tellStory(story):
    '''story is a format string with Python dictionary references embedded,
    in the form %(cue)s.  Prompt the user for the mad lib substitutions
    and then print the resulting story with the substitutions.
    '''
    cues = getKeys(story)
    userPicks = getUserPicks(cues)
    print story % userPicks    

def main():
    originalStory = '''
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
'''
    tellStory(originalStory)

main()
