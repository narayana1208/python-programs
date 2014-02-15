'''Illustrate an awkward form of an interactive loop, entering lines,
with an explicit check about continuing before each line.'''

def main():
    lines = list()
    testAnswer = raw_input('Press y if you want to enter more lines: ')
    while testAnswer == 'y':
        line = raw_input('Next line: ')
        lines.append(line)
        testAnswer = raw_input('Press y if you want to enter more lines: ')

    print 'Your lines were:'
    for line in lines:
        print line

main()
