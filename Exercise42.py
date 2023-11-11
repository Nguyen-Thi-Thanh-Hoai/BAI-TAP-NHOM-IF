C4=261.63
D4=293.66
E4=329.63
F4=349.23
A4=440.00
B4=493.88
n=1
tan_so=float(input("Nhap tan so = "))
if C4-n<= tan_so <=C4+n:
    print("C4")
elif D4-n<= tan_so <=D4+n:
    print("D4")
elif E4-n<= tan_so <=E4+n:
    print("E4")
elif F4-n<= tan_so <=F4+n:
    print("F4")
elif A4-n<= tan_so <=A4+n:
    print("A4")
elif B4-n<= tan_so <=B4+n:
    print("B4")
else:
    print("Tan so khong tuong ung voi not nhac")