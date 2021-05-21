from math import sqrt

def prime_normal(n):
    if n <=2:
        print("Not Prime")
        return 
    
    for i in range(3,1+n//2):
        if n%i == 0:
            print("Not Prime")
            return
    
    print("Prime")
    return 
    
def prime_sqrtOptimised(n):
    if n <=2:
        print("Not Prime")
        return 
    
    for i in range(3,1+(int)(sqrt(n))):
        if n%i == 0:
            print("Not Prime")
            return
    
    print("Prime")
    return 
    
def prime_EratoSieve(n):
    prime = [0 for i in range(n+1)]
    for i in range(2,n+1,2):
        prime[i] = 0
        #print(i)
    for i in range(3,1+(int)(sqrt(n)),2):
        for j in range(i, n+1,i):
            prime[j] = 0
            #print(j)
            
    if prime[n] == 1:
        print("Prime")
        return
    else:
        print("Not Prime")
        return
   
    
n = 1
prime_normal(n)
prime_sqrtOptimised(n)
prime_EratoSieve(n)
    