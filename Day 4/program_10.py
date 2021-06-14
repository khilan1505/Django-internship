N1 = int(input("Enter Number One : \n"))
N2 = int(input("Enter Number Two : \n"))
class arith():
    def __init__(self,N1,N2):
       self.add  = N1 + N2
       self.sub  = N1 - N2
       self.mul  = N1 * N2
       
    def ans(self):
        print("Addition is : ",self.add)   
        print("Subtraction is",self.sub)   
        print("Multiplication is",self.mul)  
         
display = arith(N1,N2)   
display.ans()     