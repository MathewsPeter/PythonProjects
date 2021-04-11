y=(int)(input("input a positive number as year"))
if y<0:
    print("enter a positive integer")
else:
    if y%100 == 0:
        if y%400 ==0:
            print("leap")
        else:
            print("not leap")
    elif y%4 == 0:
        print("leap")
    else:
        print("not leap")  