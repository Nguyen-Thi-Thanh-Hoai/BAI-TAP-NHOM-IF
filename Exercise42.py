C4=261.63
D4=293.66
E4=329.63
F4=349.23
G4=392.00
A4=440.00
B4=493.88
tan_so=float(input("Nhap tan so = "))
if C4-1<= tan_so <=C4+1:
    print("C4")
elif D4-1<= tan_so <=D4+1:
    print("D4")
elif E4-1<= tan_so <=E4+1:
    print("E4")
elif F4-1<= tan_so <=F4+1:
    print("F4")
elif G4-1<= tan_so <=G4+1:
    print("G4")
elif A4-1<= tan_so <=A4+1:
    print("A4")
elif B4-1<= tan_so <=B4+1:
    print("B4")
else:
    print("Tan so khong tuong ung voi not nhac")