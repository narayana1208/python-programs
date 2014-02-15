'''Use a function to number the entries in any list INCORRECTLY.'''

def numberList(items): #WRONG code for illustration
    '''Print each item in a list items, numbered in order.'''
    for item in items:
        number = 1
        print number, item
        number = number + 1

numberList(['apples', 'pears', 'bananas'])
