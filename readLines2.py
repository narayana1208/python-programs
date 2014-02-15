''' A neater interactive loop with an agreed upon sentinal value
to end the looping.'''

lines = list()
print 'Enter lines of text.'
print 'Enter an empty line to quit.'

line = raw_input('Next line: ') # initalize before the loop
while line != '':
    lines.append(line)
    line = raw_input('Next line: ')  # !! reset value at end of loop!

print 'Your lines were:'
for line in lines:
    print line
