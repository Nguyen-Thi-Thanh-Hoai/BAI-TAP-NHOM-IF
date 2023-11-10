# a=float(input("Nhap canh a="))
# b=float(input("Nhap canh b="))
# c=float(input("Nhap canh c="))
# if ((a+b)>c and (b+c)>a and (c+a)>b) and (a>0 and b>0 and c>0):
#    if a*a==(b*b)+(c*c) or b*b==(a*a)+(c*c) or c*c==(a*a)+(b*b):
#      print('Tam giac vuong')
#    elif a==b and b==c and c==a:
#      print('Tam giac deu')
#    else:
#      print('Tam giac loai khac')  
# else:
#  print('So lieu nhap vao khong co tam giac nao tuong ung')  
print("Nhap do dai cac canh cua tam giac: ")
a = int(input("Canh 1: "))
b = int(input("Canh 2: "))
c = int(input("Canh 3: "))
if ((a+b)>c and (b+c)>a and (c+a)>b) and (a>0 and b>0 and c>0):
  if a*a==(b*b)+(c*c) or b*b==(a*a)+(c*c) or c*c==(a*a)+(b*b):
    print('Tam giac vuong')
  elif a == b == c:
	  print('Tam giac deu')
  elif a == b or a == c or b == c:
	  print('Tam giac can')
  else:
    print('Tam giac loai khac') 
else:
	print('TSo lieu nhap vao khong co tam giac nao tuong ung')