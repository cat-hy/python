fn=open('bcd.txt','r')
fn1=open('nfile.txt','w')
count=fn.readlines()
type(count)
for i in range(0,len(count)):
 if(i%2==0):
  fn1.write(count[i])
 else:
  pass
fn1.close()
fn1=open('nfile.txt','r')
count1=fn1.read()
print(count1)
fn.close()
fn1.close()
