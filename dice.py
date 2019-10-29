import string
from secrets import randbelow
from sys import platform
from os import system


class Dice:
    X = []
    x = y = 0

    def run(self):
        try:
            while True:
                print("0. Abort")
                print("1. Roll")
                print("2. Clear")
                print("3. Show")
                print("4. Statistics")
                c = input("Choice: ")
                if c == '0' or c == 'q':
                    return
                elif c == '' or c == '1':  # Roll
                    self.read()
                    print("Rolling {0}d{1}".format(self.x, self.y), end=' - ')
                    self.toss()
                    self.show(self.x)
                elif c == '2':  # Clear
                    self.clear()
                elif c == '3':  # Show
                    self.show(-1)
                elif c == '4':  # Statistics
                    self.clear()
                    self.read()
                    self.toss()
                    self.percent()
                else:
                    print("Invalid option")
                input()
                self.clearscreen()
        except KeyboardInterrupt:
            pass

    def read(self):
        n = -1
        a = str(input("Roll example - 2d10: "))
        if a == "":
            self.x = 1
            self.y = 10
            return
        for i in range(len(a)):
            if a[i] in string.ascii_letters:
                n = i
        if n == 0:
            self.x = 1
        elif n == -1:
            self.x = 1
            self.y = int(a)
            return
        else:
            self.x = int((a[:n]))
        self.y = int((a[n + 1:]))

    def toss(self):
        for i in range(self.x):
            self.X.append(randbelow(self.y) + 1)

    def show(self, n):
        if n == -1:
            print(self.X)
        else:
            print(self.X[-n:], end=' ')
            if n > 1:
                sum = 0
                for i in range(len(self.X) - n, len(self.X)):
                    sum += self.X[i]
                print("=", sum)

    def clear(self):
        self.X = []

    def percent(self):
        W = [0 for x in range(self.y)]
        for i in range(1, self.y + 1):
            for j in self.X:
                if j == i:
                    W[i - 1] += 1
        for i in range(1, self.y + 1):
            print("{0}: {1}%".format(i, round(((W[i - 1]) / self.x) * 100, 2)))

    @staticmethod
    def clearscreen():
        system("cls") if "win" in platform.lower() else system("clear")


q = Dice()
q.run()
