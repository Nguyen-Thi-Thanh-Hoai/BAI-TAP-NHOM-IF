tuoi_nguoi=int(input("Nhap so tuoi cua con nguoi: "))
if tuoi_nguoi <=2: 
   tuoi_cho= tuoi_nguoi*10.5
   print(tuoi_nguoi,"tuoi nguoi bang",tuoi_cho,"tuoi cho")
elif 2 < tuoi_nguoi:
    tuoi_cho= 21+ (tuoi_nguoi -2)*4
    print(tuoi_nguoi,"tuoi nguoi bang",tuoi_cho,"tuoi cho")
elif tuoi_nguoi<0:
    print("So tuoi nguoi khong hop le")