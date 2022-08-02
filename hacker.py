"""
Complete a seguinte função para que a mesma devolva todos os possíveis números de 4 dígitos,
onde cada um seja menor ou igual a<maxDigit>, e a soma dos dígitos de cada número gerado seja 21
Exemplo maxDigit=6: 3666, 4566...
"""

def cria_sequencia(max_digit):
    multiplo = str(max_digit) * 4
    lista2 = []
    for x in range(1000, int(multiplo)):
        soma = 0
        for y in str(x):
            if int(y) <= max_digit:
                soma += int(y)
        if soma == 21:
            lista2.append(x)

    return lista2


max_digit = input("Digite um numero inteiro entre 6 à 9: ")

for x in cria_sequencia(int(max_digit)):
  print(x)


