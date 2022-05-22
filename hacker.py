"""
Complete a seguinte função para que a mesma devolva todos os possíveis números de 4 dígitos,
onde cada um seja menor ou igual a<maxDigit>, e a soma dos dígitos de cada número gerado seja 21
Exemplo maxDigit=6: 3666, 4566...
"""

def converte_texto_em_numero(texto):

    try:
        if type(int(texto)) == type(6) and len(texto) == 1:
            if int(texto) >= 6:
                numero = int(texto)
                return numero
            else:
                raise Exception("Valor de entrada menor que dígito 6")
        else:
            raise Exception("Número com mais de uma unidade ou caractere diferente de nº")
    except:

        print("Por favor digite apenas um número inteiro entre 6 à 9")
        texto = input("Pode digitar o número: ")
        numero = converte_texto_em_numero(texto)
        return  numero

max_digit = input("Digite um numero inteiro entre 6 à 9: ")

max_digit = converte_texto_em_numero(max_digit)

multiplo = str(max_digit) * 4

for x in range(1000, int(multiplo)):
    lista = [int(n) for n in str(x) if int(n) <= max_digit]
    if sum(lista) == 21:
        for h in lista:
            print(h, end="")

        print()