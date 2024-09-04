def verificar_letra_a(string):
    # Conta a ocorrência de 'a' e 'A'
    count_a = string.count('a')
    count_A = string.count('A')
    total = count_a + count_A
    
    if total > 0:
        return f"A letra 'a' e/ou 'A' aparecem {total} vez(es) na string."
    else:
        return "A letra 'a' e 'A' não aparecem na string."

while True:
    entrada = input("Digite uma string para verificar a ocorrência da letra 'a' (ou digite 'sair' para encerrar): ")
    if entrada.lower() == 'sair':
        print("Encerrando o programa.")
        break
    resultado = verificar_letra_a(entrada)
    print(resultado)
