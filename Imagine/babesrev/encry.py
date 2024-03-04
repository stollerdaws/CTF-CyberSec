import random

flag = open("flag.txt", "r").readline()

random.seed(42)
a = random.randint(1, 100)

def encrypt(string):
  s = ""
  for n in string:
    n = ord(n)
    n = n * 3 + 65 - 32 + a
    n = str(int(str(int(str(int(str(int(str(n)[1:]))))))))
    s += n
  return s

print(encrypt(flag))