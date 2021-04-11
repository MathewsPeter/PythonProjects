'''
input a 8bit Number
count the number of 1s in it's binary representation
consider that as a number, swap the bit at that position
'''

n = (int)(input("enter a number between [0,127] both inclusive"))
if n<0 or n>127:
    print("enter properly")
     
else:
    n_1= n
    c = 0
    while n:
        if n&0b1:
            c+=1
        n = n>>1
    print(c)    
    
    n_2 = n_1 ^ (1<<c)
    print(n_2)
