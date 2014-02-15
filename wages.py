'''if-else example:  calculate weekly wages'''

def calcWeeklyWages(totalHours, hourlyWage):
    '''Return the total weekly wages for a worker working totalHours,
    with a given regular hourlyWage.  Include overtime for hours over 40.
    '''

    if totalHours <= 40:
        totalWages = hourlyWage*totalHours
    else:
        overtime = totalHours - 40
        totalWages = hourlyWage*40 + (1.5*hourlyWage)*overtime
    return totalWages

def main():
    hours = input('Enter hours worked: ')
    wage = input('Enter dollars paid per hour: ')
    total = calcWeeklyWages(hours, wage)
    print 'Wages are $%.2f.' % total

main()
