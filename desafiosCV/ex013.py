vl_salario = float(input("Digite o salário do funcionário: R$"))
pc_amnt_slrio = 15
vl_slrio_amntdo = vl_salario * (1 + (pc_amnt_slrio / 100))
print("O salário passará a ser de {:.2f}, com aumento de {}%".format(vl_slrio_amntdo, pc_amnt_slrio))
