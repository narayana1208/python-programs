'''Quick illustration of reading a file.
(needs revisedFile.py run first to create sample3.txt)
'''

inFile = file('sample3.txt', 'r')
contents = inFile.read()
print contents

