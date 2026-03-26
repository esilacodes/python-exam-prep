"""
Question: How many of the first 10,000 prime numbers start with 3 and end with 7?
Logic: Generate the first 10,000 prime numbers, convert each to a string, 
       then count how many satisfy: first digit = '3' and last digit = '7'
Difficulty: Medium-Hard
"""



def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):    #reduces the time bcs spuare root
        if n%i==0:
            return False
    return True

primes=[]
num=2

while len(primes)<10000:
    if is_prime(num):
        primes.append(num)
    num+=1 

count=0
for j in primes:
    s=str(j)
    if s[0]=="3" and s[-1]=="7":
        count+=1

print(count)



"""
Question: Find all prime numbers less than 10,000 whose sum of digits is also a prime number.
Logic: 
1. Generate all prime numbers below 10,000.
2. For each prime, calculate the sum of its digits.
3. Check if that sum is also prime.
4. Count how many such numbers exist.
Difficulty: Medium-Hard
"""



