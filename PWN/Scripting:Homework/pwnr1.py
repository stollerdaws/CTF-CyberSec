from pwn import *
from decimal import Decimal

def evaluate_expression(expression):
    # Split the expression into components
   components = expression.split()

     # Evaluate each component using Decimal
   print(components[0][2:].strip())
   x1 = int(components[0][2:].strip())
   op1 = components[1]
   x2 = int(components[2][:-1])
   op2 = components[3]
   x3 = int(components[4][:-1])
   op3 = components[5]
   x4 = int(components[6])

     # Evaluate the expression atomically
   if op1 == '+':
       result = x1 + x2
   elif op1 == '-':
       result = x1 - x2
   elif op1 == '*':
       result = int(x1 * x2)
   elif op1 == '/':
       result = int(x1 / x2)
   elif op1 == '%':
       result = x1 % x2
   else:
       raise ValueError(f"Invalid operator: {op1}")

   if op2 == '+':
       result = result + x3
   elif op2 == '-':
       result = result - x3
   elif op2 == '*':
       result = int(result * x3)
   elif op2 == '/':
       result = int(result / x3)
   elif op2 == '%':
       result = result % x3
   else:
       raise ValueError(f"Invalid operator: {op2}")

   if op3 == '+':
       result = result + x4
   elif op3 == '-':
       result = result - x4
   elif op3 == '*':
       result = int(result * x4)
   elif op3 == '/':
       result = int(result / x4)
   elif op3 == '%':
       result = result % x4
   else:
       raise ValueError(f"Invalid operator: {op3}")

   return int(result)
 
io = remote("ctf.hackucf.org", 10104)
flag = False
while(1):
   #recieve stream of characters until "value: "
   if flag == False:
      io.recvuntil("!\n")
      flag = True
   val1 = io.recvuntil("=").decode()
   print(val1)
   val1 = val1[:-1]
   val = evaluate_expression(val1)
   print(int(val))
   io.sendline(bytes(str(val), 'utf-8'))


