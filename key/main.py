from math import gcd
from random import choice
from tqdm import tqdm

prime_number1 = 9967
prime_number2 = 9973

mod = prime_number1 * prime_number2

phi = (prime_number1 - 1) * (prime_number2 - 1)

coprime_list = []
for i in tqdm(range(phi)):
    if gcd(i, phi) == 1:
        coprime_list.append(i)

public_exp = choice(coprime_list[len(coprime_list)//2:])

print("Public key:", public_exp, mod)

private_exp = 0
for i in tqdm(range(mod)):
	if (i * public_exp) % phi == 1:
		private_exp = i

print("Private key:", private_exp, mod)
