import random

def daikiti():
    print("大吉です!!")

def chukiti():
    print("中吉です!")

def syoukiti():
    print("小吉です")

def kiti():
    print("吉です")

def kyou():
    print("凶です")

#ここから実行開始
kekka = random.randint(1, 10)
if kekka == 1:
    daikiti()
elif kekka == 2 or kekka == 3:
    chukiti()
elif kekka >= 4 and kekka <= 7:
    syoukiti()
elif kekka == 8 or kekka == 9:
    kiti()
else:
    kyou()