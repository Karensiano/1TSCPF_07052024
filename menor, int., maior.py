# Menor, intermediário, maior:. Entre com 3 números em 3 variáveis diferentes ordene
# imprimindo também a classificação: menor, intermediário, maior

titulo = "Menor, intermediário, maior"
print(f"{titulo: ^30}")

N1 = int(input('Entre com o 1º numero: '))
N2 = int(input('Entre com o 2º numero: '))
N3 = int(input('Entre com o 3º numero: '))
# atribuição múltipla pelo python
print(f'Os numeros {N1}, {N2}, {N3}', end=' ')
if N1 > N2:
    N1, N2 = N2, N1

if N1 > N3:
    N1, N3 = N3, N1

if N2 > N3:
    N2, N3 = N3, N2

print(f'o número menor é: {N1}, intermediario: {N2}, maior: {N3}')

