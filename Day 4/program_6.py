l = int(input("Enter length :\n"))
h = int(input("Enter height :\n"))

class cal5():
    def __init__(self,l,h):
        print("length is : ",l)
        print("height is : ",h)
    
    def calArea(self):
        area = l * h
        print("Area of rectangle is : ",area)

display = cal5(l,h)
display.calArea()
        