'''
convert a decimal number to binary.
assume only whole and positive number
'''

n = (int)(input("enter a whole positive integer"))
if n<0:
    print("enter proper")
else:
    n_1 = n
    b = 0
    i = 1
    while n:
        b+=(n%2)*i
        i*=10
        n//=2
        
    print(n_1, b)
            
        