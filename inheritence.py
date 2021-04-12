class A:
    def __init__(self, a):
        self.a = a
    
    def disp(self):
        print(self.a)
        
class B(A):
    def __init__(self,a,b):
        A.__init__(self, a)
        self.b = b
        
    def disp(self):
        print(self.a,self.b)
        
class C(B):
    def __init__(self,a,b,c):
        B.__init__(self, a,b)
        self.c = c
        
    def disp(self):
        print(self.a,self.b,self.c)
                
#Aobj = A(1)
#Bobj = B(1,2)
Cobj = C(1,2,3)
#Aobj.disp()
#Bobj.disp()
Cobj.disp()
        
