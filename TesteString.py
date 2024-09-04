while True:
    string = input("Digite uma string para inverter: ")

    invertida = ""

    #A cada iteração, o primeiro caractere é mantido no fim e assim subsequentemente
    
    for char in string:
        invertida = char + invertida  

    print("String invertida:", invertida)

    continuar = input("Deseja inverter outra string? (s/n): ").strip().lower()
    
    if continuar != 's':
        print("Saindo do programa.")
        break
