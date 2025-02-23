import re
txt = input()
txt = re.sub('\_','',txt)
print(txt)