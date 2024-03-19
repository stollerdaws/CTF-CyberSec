from Crypto.Util.number import*
from gmpy2 import *
from secret import flag,hint,p,q,n,e

m = bytes_to_long(flag)
h = [i^n for i in hint]
print(f"h = {(h)}")
ct = pow(m,e,n)
print("ct = ",ct)
print("p = ",p)
print("q = ",q)