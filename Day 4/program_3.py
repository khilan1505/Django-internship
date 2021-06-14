class cal3():
    p=0
    t=0
    r=0
    def __init__(self,p,t,r):
        self.p=p
        self.t=t
        self.r=r
        print('The principal is', p)
        print('The time period is', t)
        print('The rate of interest is',r)
      
    def calinterst(self):
        interst = (self.p * self.t * self.r)/100
        print("The Simple Interest is : ", interst)
    
display = cal3(8,6,8)
display.calinterst()
 

        