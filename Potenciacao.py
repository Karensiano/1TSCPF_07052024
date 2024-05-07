titulo = "Potenciacao"
print(f"{titulo: ^30}")

base = int(input('Entre com a base: '))
exponencial = int(input('Entre com o exponencial: '))

total = 1
i = 1
if base <= 1 or exponencial < 2:
    print('A base deve ser maior que 1 e o exponencial maior que 2.')
else:
    while i <= exponencial:
        total = total * base
        i += 1
    print(f'{base} elevado a {exponencial} é igual a {total}')
