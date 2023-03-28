import time as q

#ban quyen NGUYEN VIET HOANG

x="TRẦN HÀ NHI"

b=len(x)
def cake():	
	print(" "*23,"i  i  i  i")
	y=q.sleep(1)
	print(" "*23,"i  i  i  i")
	y=q.sleep(1)
	print(" "*21,"__i__i__i__i__")
	y=q.sleep(1)
	print(" "*20,"|"," "*12,"|")
	y=q.sleep(1)
	print(" "*20,"|"," "*12,"|")
	y=q.sleep(1)
	print(" "*20,"|"," "*12,"|")
	y=q.sleep(1)
	print(" "*16,"-"*24)
	y=q.sleep(1)
	print(" "*16,"|"," "*20,"|")
	y=q.sleep(1)
	print(" "*16,"|"," "*int((20-b)/2),x," "*int((20-b)/2-2),"|")
	y=q.sleep(1)
	print(" "*16,"|"," "*20,"|")
	y=q.sleep(1)
	print(" "*16,"-"*24)


def menu():
	print()
	for i in range(4):
		if i==3:
			print(" "*13,"HAPPY HAPPY BIRTHDAY TO YOU")
		elif i==0 or i==1:
			print(" "*15,"HAPPY BIRTHDAY TO TRẦN HÀ NHI")
		elif i==2:
			print(" "*15,"HAPPY BIRTHDAY","*",x.upper(),"*","\n")
		q.sleep(1.8)
		print()
	
def heart():
	for row in range(6):
		for col in range(7):
			if (row==0 and col %3 != 0)or(row==1 and col %3==0) or(row-col==2) or(row+col==8):
				print("💙",end=" ")
			else:
				print(end="  ")
		print()	
print("#"*9," HAPPY BIRTHDAY ","*"+x.upper()+"*","#"*9)
q.sleep(1.5)
menu()
cake()

print(" "*2,"NGUYỄN VIỆT HOÀNG CHÚC BẠN SINH NHẬT VUI VE, THÀNH CÔNG HƠN \n \n\n".upper())
q.sleep(2)
x="TRẦN HÀ NHI"
a=x.split()
for i in a:
	print("\t\t",i.title())
	q.sleep(1)
print("")
q.sleep(2)
print(" "*18,"NGUYỄN VIỆT HOÀNG".upper())
q.sleep(1)
print(" "*18,"TRẦN HÀ NHI".upper())
q.sleep(1)
heart()