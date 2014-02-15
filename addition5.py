'''Display a sum problems with a function.
Handle keyboard input separately.
'''

def sumProblem(x, y):
    print 'The sum of %s and %s is %s.' % (x, y, x+y)

def main():
    sumProblem(2, 3)
    sumProblem(1234567890123, 535790269358)
    a, b = input("Enter two comma separated numbers: ")
    sumProblem(a, b)

main() 
