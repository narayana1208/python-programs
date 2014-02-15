'''program causing an error with an undifined variable'''

def main():
    x = 3
    f()

def f():
    print x  # error: f does not know about the x defined in main

main()
