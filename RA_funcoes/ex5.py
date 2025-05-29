def soma(num1, num2):
    num1 = float(input("Digite um número: "))
    num2 = float(input("Digite um número: "))    
    return num1 + num2

def subtracao(num1, num2):
    num1 = float(input("Digite um número: "))
    num2 = float(input("Digite um número: "))  
    return num1 - num2

def multiplicacao(num1, num2):
    num1 = float(input("Digite um número: "))
    num2 = float(input("Digite um número: "))  
    return  num1 * num2

def divisao(num1, num2):
    num1 = float(input("Digite um número: "))
    num2 = float(input("Digite um número: "))  
    return num1 / num2

def sair():
    

i = 0

print("Bem vindo a calculadora supimpa!")

print("Qual opção deseja? 1.soma 2.subtração 3.multiplicação 4.divisão 5.menu ")

opcao = input("Digite sua opção: ")

while i == True:
    if opcao == 1:
        print(soma)
    elif opcao == 2:
        print(subtracao)
    elif opcao == 3:
        print(multiplicacao)
    elif opcao == 4:
        print(divisao)
    elif opcao == 5:
        sair