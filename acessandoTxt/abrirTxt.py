#logar
def logar(nm, index):
    password = input("password: ")
    with open("./txt/pass.txt", "r", encoding="utf-8") as arqPass:
        liPass = []
        for n in arqPass.readlines():
            liPass.append(n.replace("\n", ""))
        while liPass[index] != password:
            a1 = input("The password is incorrect! Would do you like to try again? y/n ").lower().strip()
            if a1 == "y":
                password = input("password: ")
            else:
                break
        if (password == liPass[index]) and (nm == li[index]):
            print(f"Welcome! {nm}!")
            return True

#criar conta
def verificationName(nm):
    for i in li:
        if nm == i:
            print("nickname is already being used! Try another")
            return False

def criarConta():
    temp = False
    while temp == False:
        temp = True
        name = input("nickname: ")
        temp = verificationName(name)
    password = input("Enter a secure password: ").strip()
    with open("./txt/user.txt", "a", encoding="utf-8") as arqUser:
        arqUser.write("\n" + name)
        print(f"{name} has been registered successfully!")
    with open("./txt/pass.txt", "a", encoding="utf-8") as arqPass:
        arqPass.write("\n" + password)
        print(f"{password} has been registered successfully!")


#código
with open("./txt/user.txt", "r", encoding="utf-8") as arq:
    name = input("name: ").strip()
    log = False
    li = []
    for i in arq.readlines():
        li.append(i.replace("\n", ""))
    for i in li:
        if(i == name):
            pos = li.index(name)
            log = logar(name, pos)
    if log == False:
        print("not connected...")
        a2 = input("Would do you like to create a new and free account? y/n ").lower().strip()
        if a2 == "y":
            print("okay")
            criarConta()
        else:
            print("OK! Bye :D")
    