'''Interactive loop with verbose prompt each time.'''

lines = list()
testAnswer = raw_input('Press y if you want to enter more lines: ')
while testAnswer == 'y':
    line = raw_input('Next line: ')
    lines.append(line)
    testAnswer = raw_input('Press y if you want to enter more lines: ')

print 'Your lines were:'
for line in lines:
    print line
