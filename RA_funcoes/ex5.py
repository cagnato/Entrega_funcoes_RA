def soma(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    if num2 == 0:
        return "Erro: divisão por zero."
    return num1 / num2

print("Bem-vindo à calculadora supimpa!")

while True:
    print("\nEscolha uma opção:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

    opcao = input("Digite sua opção: ")

    if opcao == "5":
        print("Saindo da calculadora. Até logo!")
        break

    if opcao in ["1", "2", "3", "4"]:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Erro: você precisa digitar números válidos.")
            continue

        if opcao == "1":
            resultado = soma(num1, num2)
        elif opcao == "2":
            resultado = subtracao(num1, num2)
        elif opcao == "3":
            resultado = multiplicacao(num1, num2)
        elif opcao == "4":
            resultado = divisao(num1, num2)

        print(f"Resultado: {resultado}")
    else:
        print("Opção inválida. Tente novamente.")
