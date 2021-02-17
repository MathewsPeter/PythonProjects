from Crypto.Random.random import randint

choice=['R','P','S']
uscore=0
cscore=0
for i in range(5):
    u=input("Enter your choice: R or P or S: ")
    u = u.upper()
    if u == 'R' or u == 'P' or u == 'S':
        c = choice[randint(0,2)]
          
        if u == "R":
            if c == "R":
                print("R-R. It's a tie")
            if c == "P":
                print("R-P. Computer wins")
                cscore+=1
            if c == "S":
                print("R-S. You win")
                uscore+=1
          
        if u == "P":
            if c == "R":
                print("P-R. You win")
                uscore+=1
            if c == "P":
                print("P-P. It's a tie")
            if c == "S":
                print("P-S. Computer wins")
                cscore+=1
                                             
        if u == "S":
            if c == "R":
                print("S-R. Computer wins")
                cscore+=1
            if c == "P":
                print("S-P. You win")
                uscore+=1
            if c == "S":
                print("S-S. It's a tie")
    else:
        continue
if uscore > cscore :
    print("You win. ", uscore, ":", cscore)
elif uscore < cscore :
    print("Computer wins. ", cscore, ":", uscore)
else:
    print("Its a tie. ", cscore, ":", uscore)
