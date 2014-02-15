'''prints numbered entries from the list'''

items = ['red', 'orange', 'yellow', 'green']
number = 1
for item in items:
    print number, item
    number = number + 1   # crucial added line
