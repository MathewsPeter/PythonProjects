import math
bill = (int)(input("Enter bill amount: "))
n = (int)(input("Enter number of people to share with: "))
tipperc = 18
billtip = math.ceil(bill*(100.0+tipperc)/100)
print("Bill with tip is",billtip)
print("Bill per person is %.2f"%(billtip/n)) 

shareperc=[]
while(1):
    i=0
    for i in range(n):
        shareperc.append((int)(input("Enter percentage share of next person")))
    if sum(shareperc)==100:
        break
    else:
        print("Sum of share percentage is", sum(shareperc), ".It should be 100")
    
for i in range(n):
    print("Bill of person#",(i+1)," is",billtip*(shareperc[i]/100.0))
        