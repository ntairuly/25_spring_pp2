from datetime import *
print("YYYY-MM-DD hh:mm:ss")
a = datetime.fromisoformat(input('1 date:'))
b = datetime.fromisoformat(input('2 date:'))
seconds = abs(a.timestamp() - b.timestamp())
print(seconds)
