import re
txt = input()
txt = re.findall('[A-Z][a-z]*',txt)
for i in range(0,len(txt)):
    txt[i]=txt[i][0]+txt[i][1:]
print(' '.join(txt))