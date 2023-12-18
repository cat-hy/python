
print("......PROGRAM FOR DISPLAYING LEAP YEARS.......")
list=[]
start=2000
end=int(input("Enter end year:"))
while start<=end:
	if(start%4==0 and (start%100!=0 or start%400==0)):
		list.append(start)
	start+=1
print("List of leap years from 2000 to",end,"is:",list)

