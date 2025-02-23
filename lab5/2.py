import re
txt = input()
pattern = '^ab{2,3}'
if re.search(pattern,  txt):
    print('Found!')
else:
    print('Not found!')
