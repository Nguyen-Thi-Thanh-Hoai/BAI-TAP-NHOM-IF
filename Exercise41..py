C4=261.63
D4=293.66
E4=329.63
F4=349.23
G4=392.00
A4=440.00
B4=493.88
ten_not=input("Nhap ten not nhac: ")
chu_cai=ten_not[0]
quang_tam=int(ten_not[1])
if chu_cai=="C":
    tan_so=C4
elif chu_cai=="D":
    tan_so=D4
elif chu_cai=="E":
    tan_so=E4
elif chu_cai=="F":
    tan_so=F4
elif chu_cai=="G":
    tan_so=G4
elif chu_cai=="A":
    tan_so=A4
elif chu_cai=="B":
    tan_so=B4
tan_so=tan_so/2**(4-quang_tam)
print("Tan so=",tan_so)