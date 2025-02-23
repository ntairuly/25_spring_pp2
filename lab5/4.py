import re
txt = input()
pattern = '[A-Z][a-z]'
if re.search(pattern,  txt):
    print('Found!')
else:
    print('Not found!')
