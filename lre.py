B=[11,22,31,44,51,65,71,82,91]
print("List Items=",B)

for ev in B:
	if(ev%2==0):
	 	B.remove(ev)
print("List Items after removing even items=",B)
