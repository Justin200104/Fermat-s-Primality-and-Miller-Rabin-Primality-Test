
# Fermat's Primality Test and Miller-Rabin Primality Test

## 1. Fermat's Primality Test

**Fermat's Primality Test** is based on **Fermat's Little Theorem**, which states that if `p` is a prime number and `a` is an integer such that `1 < a < p-1`, then:

a^(p-1) ≡ 1 (mod p)


This means that when a number `a` is raised to the power `p-1`, and then divided by `p`, the remainder will be `1`. The test works by choosing a random number `a` and checking if the above condition holds. If it does not hold, then `p` is **composite** (not prime).

### Key Points:
- **Probabilistic**: Fermat's test can sometimes mistakenly identify composite numbers as prime, especially with special numbers called **Carmichael numbers**.
- **Efficiency**: It is a quick test for checking if a number might be prime, but not always reliable.

### Steps:
1. Pick a random number `a`.
2. Check if `a^(p-1) % p == 1`.
3. If the condition holds for several random `a` values, then `p` is probably prime.

## 2. Miller-Rabin Primality Test

**Miller-Rabin Primality Test** is an improved version of Fermat's test that reduces the risk of mistakenly identifying composite numbers as primes. It is also based on properties of modular arithmetic, but with additional checks.

The Miller-Rabin test works by expressing `n-1` as a product of powers of 2 and an odd number, i.e., `n-1 = 2^s * d`. It then performs a series of tests using random numbers to check if `n` behaves like a prime number.

### Key Points:
- **Probabilistic**: Like Fermat's test, Miller-Rabin is probabilistic, but it is much more reliable.
- **Wide Use**: It is commonly used in cryptography for generating large prime numbers.
  
### Steps:
1. Express `n-1` as `2^s * d`.
2. Pick a random base `a`.
3. Check conditions based on modular arithmetic and squaring.
4. Repeat the process several times to improve the accuracy.

### Reliability:
- If Miller-Rabin reports that a number is composite, it is **definitely composite**.
- If it reports that the number is prime after multiple rounds of testing, the number is **probably prime** with high confidence.

## Summary

- **Fermat's Primality Test** is a quick but less reliable way to check if a number is prime.
- **Miller-Rabin Primality Test** is a more reliable test that is widely used in cryptography to ensure the generation of large prime numbers.
