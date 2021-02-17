from Crypto.Random.random import randint
n=randint(1,20)
i=0
for i in range(1,6):
    u=(int)(input("enter a guess: "))
    if u==n:
        print("Guessed correctly in %d attempts",i)
        break
    elif u>n:
        print("Guess is too big")
    else:
        print("Guess is too small")
    if i == 4:
        print("5 guesses over. Number was ",n,". Exiting...")
    
    
    
