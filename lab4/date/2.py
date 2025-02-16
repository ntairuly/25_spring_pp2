from datetime import *
a = datetime.now()
change=a.day-1
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
print("Yesterday:",a)
a = datetime.now()
print("Today:    ",a)
change=a.day+1
if change>=29:
    if a.month in (12) and change==32:
        a.replace(year=a.year+1,month= 1,day=1)
    if a.month in (1,3,5,7,8,10) and change==32:
        a.replace(month= a.month+1,day=abs(31-change))
    elif a.month in (2) and change==29:
        a.replace(month= a.month+1,day=abs(28-change))
    elif change == 31:
        a.replace(month= a.month+1,day=abs(30-change))
    else:
        a = a.replace(day=change)
else:
    a = a.replace(day=change)
print("Tomorrow: ",a)