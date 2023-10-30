from Crypto.Util.number import long_to_bytes,bytes_to_long
from Crypto import Random
import Crypto
import sys
import libnum
from math import isqrt

from sympy import *
import random

def get_prime(bits):
	p = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
	return(p)

# Rational numbers have finite a continued fraction expansion.
def get_cf_expansion(n, d):
    e = []
    q = n // d
    r = n % d
    
    e.append(q)

    while r != 0:
        n, d = d, r           
        q = n // d
        r = n % d
        e.append(q)

    return e

def get_convergents(e):
    n = [] # Nominators
    d = [] # Denominators

    for i in range(len(e)):
        if i == 0:
            ni = e[i]
            di = 1
        elif i == 1:
            ni = e[i]*e[i-1] + 1
            di = e[i]
        else: # i > 1 
            ni = e[i]*n[i-1] + n[i-2]
            di = e[i]*d[i-1] + d[i-2]

        n.append(ni)
        d.append(di)
        yield (ni, di)



e=65537
N = 150459385706485253914441877113384979120500190162060302508541299821944089329499694790524295291567135320851306118878915105907451588623958757693847782920309145753994837129247899050065917279292484317798035721308006529470560777407483024961882645653400385816416526996027114542480513056100444908809723540145733606413
C=2307423154990120835718508986514267143655326830191633946685219656220840494132925634069678170936781595742873539412034460586639622885239343246714559828497111273868089182257159904851948098861145910137615097694560608874412798124055642460363270612990137075678106724613406247492210136960473648165963598137216228495

     
if (len(sys.argv)>1):
        C=int(sys.argv[1])
if (len(sys.argv)>2):
        e=int(sys.argv[2])
if (len(sys.argv)>3):
        N=int(sys.argv[3])


print(f'Bob uses RSA to send an encrypted message to Alice. The public exponent (e) is {e} and the modulus (N) is {N}. With a cipher of {C}, determine the decrypted message:')

cf_expansion = get_cf_expansion(e, N)
convergents = get_convergents(cf_expansion)

for pk, pd in convergents: # pk - possible k, pd - possible d
	if pk == 0:
		continue;

	possible_phi = (e*pd - 1)//pk

	p = Symbol('p', integer=True)
	roots = solve(p**2 + (possible_phi - N - 1)*p + N, p)

	if len(roots) == 2:
		pp, pq = roots # pp - possible p, pq - possible q
		if pp*pq == N:
			print('\nAnswer:')
			print('Using Wiener attack')
			d=pow(e,-1,possible_phi)
			print('Found d:',d)
			print('Found p:',pp)
			print('Found q:',pq)
			print('Found PHI:',possible_phi)
			print('Now using C^d mod N')
			M=pow(C,d,N)
			print(f"\nDecipher: {long_to_bytes(M)}")
			sys.exit(0)

print('[-] Wiener\'s Attack failed; Could not factor N')
sys.exit(1)