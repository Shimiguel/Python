qt_metros = float(input("Digite um valor em metros: "))
qt_quilometro = qt_metros / 1000
qt_hectometro = qt_metros / 100
qt_decametro = qt_metros / 10
qt_decimetro = qt_metros * 10
qt_centimetro = qt_metros * 100
qt_milimetro = qt_metros * 1000
print(f"{qt_metros}m são iguais a: ")
print(f"\t{qt_quilometro:.4f}km")
print(f"\t{qt_hectometro:.4f}hm")
print(f"\t{qt_decametro:.4f}dam")
print(f"\t{qt_decimetro:.4f}dm")
print(f"\t{qt_centimetro:.4f}cm")
print(f"\t{qt_milimetro:.4f}mm")
