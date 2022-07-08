nm_valor = input("Digite um valor: ")
print(f"Ele é um valor númerico? {nm_valor.strip().isnumeric()}")
print(f"Ele é um valor alfabético? {nm_valor.strip().isalpha()}")
print(f"Ele é um valor composto por números e letras? {nm_valor.strip().isalnum()}")
print(f"Ele é composto apenas por espaços? {nm_valor.isspace()}")
print(f"Ele está em MAIÚSCULAS? {nm_valor.isupper()}")
print(f"Ele está em minúsculas? {nm_valor.islower()}")
print(f"Ele está Capitalizado? {nm_valor.istitle()}")

nm_list_valor = list(nm_valor)
# list() foi usada para dividir Todos os valores de uma string
print(nm_list_valor)
if len(nm_list_valor) == len(list(nm_valor.strip())):
    print(f"É composta por {len(list(nm_valor.strip()))} caracteres!")
else:
    if len(nm_list_valor) > len(list(nm_valor.strip())):
        print(f"É composta por {len(nm_list_valor)} caracteres! Com os epsaços!")
        print(f"É composta por {len(list(nm_valor.strip()))} caracteres! Sem os epsaços!")
        