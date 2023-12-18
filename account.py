class Account:
 def __init__(self,acc,name,type):
  self.balance=0
  self.acc=acc
  self.name=name
  if(type==1):
   self.type="current"
  else:
   self.type="savings"
 def deposit(self):
  amount=float(input("Enter amount to be deposited:"))
  self.balance+=amount
	
 def withdraw(self):
  amount=float(input("Enter amount to be withdrawn:"))	
  if(self.balance<amount):
   print("Insufficient Balance")
  else:
   self.balance-=amount
 def display(self):
  print("name:",self.name,"\taccount no:",self.acc,"\tbalance:",self.balance,"\tacc:",self.type)
  acc=input("Enter account number")
  name=input("Enter name")
  type=input("Choose account type:\n1.current\n2.savings")
  obj=Account(acc,name,type)
  while True:
   obj.display()
   ch=int(input("\n1.deposit\n2.withdraw\n3.exit"))
   if(ch==1):
    obj.deposit()
   elif(ch==2):
    obj.withdraw()
   elif(ch==3):
    break
   else:
    print("Invalid entry")
