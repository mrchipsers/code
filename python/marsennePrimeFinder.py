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
    for i in range(3, number):
        if number%i==0:
            return False
    return True

print(primeFinder(int(input("how many marsenne primes would you like generated? "))))