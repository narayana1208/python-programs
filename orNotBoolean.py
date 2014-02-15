'''Display use of the OR operator with nonboolean operands.'''

defaultColor = 'red'
userColor = raw_input('Enter a color, or just press Enter for the default: ')
color = userColor or defaultColor
print 'The color is', color
