import re
txt = input()
txt = re.findall('[A-Z][^A-Z]*',txt)
print(txt)