import re
txt = input()
txt = re.sub('\s',':',txt)
txt = re.sub('\.',':',txt)
txt = re.sub('\,',':',txt)
print(txt)