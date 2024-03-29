'''Illustrate building a modified list in a loop.'''

def multipleAll(numList, multiplier):
    '''Return a new list containing all of the elements of numList,
    each multiplied by multiplier.  For example:
    >>> print multipleAll([3, 1, 7], 5)
    [15, 5, 35]
    '''

    newList = list()
    for num in numList:
        newList.append(num*multiplier)
    return newList

print multipleAll([3, 1, 7], 5)
