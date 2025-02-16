from datetime import *
a = datetime.now()
change=a.day-5
if change<=0:
    if a.month==1:
        a = a.replace(year=a.year-1,month=1,day=abs(change)+1)
    elif a.month in (3,5,7,8,10,12):
        a.replace(month= a.month-1,day=31+change)
    elif a.month in (2):
        a.replace(month= a.month-1,day=28+change)
    else:
        a.replace(month= a.month-1,day=30+change)
else:
    a = a.replace(day=change)
print(a)