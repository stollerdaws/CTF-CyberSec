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



e=52738220779177222065611850726791238874162775888686333896669828781316057311757771848912410509433452207747614746891617037913715074919674513256145229421402873754097411031818752203843691793783593095070928949649107264804092838320694689052632957024165414427897354093238350700592388939126795821351541141604897101071
N = 84360788240889392261649512357262623990260056711664677458371583095628972091526936848075075473197979638029603475933929915799278387788759619883149334885563577099703477918044606947899245622509311614768494823578922902666288654029646920764866412280288829733049866825413465379493095623386728875706348895881787826177
C=36263930581377926116010569130505274218542577051620278067408477209819587159849670266211125714972972449828506870632727824689409905859567973645333021914726124046673000336177462995774739533606211908003257448475882416187806447759911607761179041793011441509849681304392459533906542665300682861972671007605717136870

     
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