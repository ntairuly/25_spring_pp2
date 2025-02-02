class Stringmathods:
    def getString(self):
        self.string = input()
    def printString(self):
        print(f"In upper case:{self.string.upper()}")
a = Stringmathods()
a.getString()
a.printString()
