nm_valor = input("Digite um valor: ")
print(f"Ele é um valor númerico? {nm_valor.strip().isnumeric()}")
print(f"Ele é um valor alfabético? {nm_valor.strip().isalpha()}")
print(f"Ele é um valor composto por números e letras? {nm_valor.strip().isalnum()}")
print(f"Ele é composto apenas por espaços? {nm_valor.isspace()}")
nm_list_valor = list(nm_valor)
print(nm_list_valor)
if len(nm_list_valor) == len(list(nm_valor.strip())):
    print(f"É composta por {len(list(nm_valor.strip()))} caracteres!")
else:
    if len(nm_list_valor) > len(list(nm_valor.strip())):
        print(f"É composta por {len(nm_list_valor)} caracteres! Com os epsaços!")
        print(f"É composta por {len(list(nm_valor.strip()))} caracteres! Sem os epsaços!")
