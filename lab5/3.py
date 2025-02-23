import re
txt = input()
pattern = '[a-z]_[a-z]'
if re.search(pattern,  txt):
    print('Found!')
else:
    print('Not found!')
