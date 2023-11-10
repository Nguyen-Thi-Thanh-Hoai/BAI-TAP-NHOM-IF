decibel=int(input("Nhap muc am thanh: "))
if decibel==130:
    print("Muc am thanh cua Bua khoan")
elif decibel==106:
    print("Muc am thanh cua May cat co")
elif decibel==70:
    print("Muc am thanh cua Dong ho bao thuc")
elif decibel==40:
    print("Muc am thanh cua Can phong yen tinh")
elif 40<decibel<70:
    print("Muc am thanh o giua Can phong yen tinh va Dong ho bao thuc")
elif 70<decibel<106:
    print("Muc am thanh o giua Dong ho bao thuc va May cat co")
elif 106<decibel<130:
    print("Muc am thanh o giua May cat co va Bua khoan")
else:
    print('Gia tri khong hop le')
    print('Vui long nhap lai')  
