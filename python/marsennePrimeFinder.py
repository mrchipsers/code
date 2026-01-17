def primeFinder(n: int):
    primes=[]
    p=2
    i=0
    while i<n:
        nthPrime = (2**(p))-1
        if checker(nthPrime):
            primes.append(nthPrime)
            i+=1
        p+=1
    return primes

def checker(number: int):
    if number%2==0 or number%5==0:
        return False
    for i in range(3, (number//2),2):
        if number%i==0:
            return False
    return True

print(primeFinder(int(input("how many marsenne primes would you like generated? "))))