'''if-else example:  calculate weekly wages -- alternate version'''

def calcWeeklyWages(totalHours, hourlyWage):  #NEW
    '''Return the total weekly wages for a worker working totalHours,
    with a given regular hourlyWage.  Include overtime for hours over 40.
    '''

    if totalHours <= 40:
        regularHours = totalHours
        overtime = 0
    else:
        overtime = totalHours - 40
        regularHours = 40
    return hourlyWage*regularHours + (1.5*hourlyWage)*overtime

def main():
    hours = input('Enter hours worked: ')
    wage = input('Enter dollars paid per hour: ')
    total = calcWeeklyWages(hours, wage)
    print 'Wages are $%.2f.' % total

main()
