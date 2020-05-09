print("Bem-vindo ao sistema de conversao")
print("Pressione 'n' se desejar converter")
print("Pressione 'x' se desejar sair")

i = 6

def calcula():
    binario = input("Insira o seu numero binario: ")
    if binario == "x":
        exit()
    else:
        decimal = int(binario, 2)
        print(binario, "em decimal é ",decimal)

resposta01 = input("Opcao escolhida: ")

if resposta01 == 'n':
    calcula()
elif resposta01 == 'x':
    exit()

while i > 2:
    print("Deseja sair do programa?")
    print("Para sair pressione 'x'")
    print("Para converter novamente 'n'")
    resposta02 = input("Opcao escolhida: ")

    if resposta02 == 'n':
        calcula()
    elif resposta02 == 'x':
        exit()
