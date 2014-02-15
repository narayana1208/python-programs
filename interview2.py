'''Compare print with concatenation and with format string.'''

applicant = raw_input("Enter the applicant's name: ")
interviewer = raw_input("Enter the interviewer's name: ")
time = raw_input("Enter the appointment time: ")
print interviewer + ' will interview ' + applicant + ' at ' + time +'.'
print '%s will interview %s at %s.' % (interviewer, applicant, time)
