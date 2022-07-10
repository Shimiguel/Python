vl_prod = float(input("Qual o valor do produto? "))

print("O produto cujo valor é R${:.2f}. Tem estes descontos: ".format(vl_prod))
qt_desconto = 5
vl_prod_descontado = vl_prod * ((100 - qt_desconto) / 100);
print("\t{}%: R${:.2f}".format(qt_desconto, vl_prod_descontado))
qt_desconto = 10
vl_prod_descontado = vl_prod * ((100 - qt_desconto) / 100);
print("\t{}%: R${:.2f}".format(qt_desconto, vl_prod_descontado))
qt_desconto = 25
vl_prod_descontado = vl_prod * ((100 - qt_desconto) / 100);
print("\t{}%: R${:.2f}".format(qt_desconto, vl_prod_descontado))
