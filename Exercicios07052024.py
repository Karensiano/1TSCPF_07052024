#Estado onde nasceu: Entre com o estado da pessoa e imprima as mensagens: carioca, paulista, mineiro,
#baiano, cearense, outros estados


titulo = "Estado de Nascimento"
print(f"{titulo: ^30}")

estado = input ("Qual o estado que você nasceu? ").upper()
if estado in ('BH', 'Bahia'):
    print("Você é baiano.")
if estado in ('CE', "Ceará", 'CEARA'):
    print("Vocé é cearense.")
if estado in ('RJ', 'RIO DE JANEIRO', 'Rio de Janeiro'):
    print("Você é carioca.")
if estado in ('São Paulo', 'SP', 'SÃO PAULO'):
    print("Você é paulista.")
else:
    print("Você é de outro estado.")
