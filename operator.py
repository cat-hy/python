class rectangle:
 area=0
 def __init__(self,a,b):
  self.a=a
  self.b=b
 def calc_area(self):
  self.area=self.a*self.b
  print()
  print("Area is:",self.area)
 def __lt__(self,second):
  if self.area<second.area:
    return True
  else:
    return False
print("\tCOMPARING AREA OF 2 RECTANGLES USING < OPERATOR\n")
length1=int(input("Enter length of rectangle 1:"))
width1=int(input("Enter width of rectangle 1:"))
length2=int(input("\nEnter length of rectangle 2:"))
width2=int(input("Enter width of rectangle 2:"))
obj1=rectangle(length1,width1)
obj2=rectangle(length2,width2)
obj1.calc_area()
obj2.calc_area()
if(obj1<obj2):
 print("\nRectangle 2 is large")
elif(obj1==obj2):
 print("\nRectangles are same")
else:
 print("\nRectangle 1 is large") 
