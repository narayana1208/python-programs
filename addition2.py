'''Conversion of strings to int before addition'''

xString = raw_input("Enter a number: ")
x = int(xString)
yString = raw_input("Enter a second number: ")
y = int(yString)
print 'The sum of %s and %s is %s.' % (x, y, x+y)
