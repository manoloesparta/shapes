from math import gcd
from random import choice

prime_number1 = 7907
prime_number2 = 7919

mod = prime_number1 * prime_number2

phi = (prime_number1 - 1) * (prime_number2 - 1)

coprime_list = []
for i in range(phi):
	if gcd(i, phi) == 1:
		coprime_list.append(i)

public_exp = choice(coprime_list[1:])

print("Public key:", public_exp, mod)

private_exp = 0
for i in range(mod):
	if (i * public_exp) % phi == 1:
		private_exp = i

print("Private key:", private_exp, mod)