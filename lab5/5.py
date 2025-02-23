import re
txt = input()
pattern = '^a.*b$'
if re.search(pattern,  txt):
    print('Found!')
else:
    print('Not found!')
