i1 = 0
i2 = 0
while(1):
    email = input("enter a email id: ")
    try:
        i1 = email.index("@")
        i2 = email.index(".")
        print("i1 =",i1,", i2 =",i2)
        if i1>0 and i2>i1+1:
            break
    except:
        continue

uname = email[:i1]
domain = email[i1+1:i2]
ending = email[i2+1:]
print(uname, domain, ending)
