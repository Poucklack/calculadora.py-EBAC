print("Olá, me diga o primeiro número")
numero1 = int(input())

print('Olá, me diga o segundo número')
numero2 = int(input())

print("Me diga qual ação você quer fazer: somar, subtrair, multiplicar ou dividir?")
calculo = input()

if calculo == "somar":
    print("Resultado:", numero1 + numero2)
elif calculo == "subtrair":
    print("Resultado:", numero1 - numero2)
elif calculo == "multiplicar":
    print("Resultado:", numero1 * numero2)
elif calculo == "dividir":
    if numero2 != 0:
        print("Resultado:", numero1 / numero2)
    else:
        print("Erro: divisão por zero não é permitida.")
else:
    print("Operação inválida.")