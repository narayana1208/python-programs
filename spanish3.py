"""Illustrate using a dictionary with a format string."""

def createDictionary():
    '''Returns a tiny Spanish dictionary'''
    spanish = dict()
    spanish['hello'] = 'hola'
    spanish['yes'] = 'si'
    spanish['one'] = 'uno'
    spanish['two'] = 'dos'
    spanish['three'] = 'tres'
    spanish['red'] = 'rojo'
    spanish['black'] = 'negro'
    spanish['green'] = 'verde'
    spanish['blue'] = 'azul'
    return spanish

def main():
    dictionary = createDictionary()
    print "Count in Spanish: %(one)s, %(two)s, %(three)s, ..." % dictionary
    print "Spanish colors: %(red)s, %(blue)s, %(green)s, ..." % dictionary
    
main()
