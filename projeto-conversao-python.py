#NOME: GIOVANNI SILVA CERQUEIRA
#RGM: 25653130
#NOME: GUILHERME JORGE DA SILVA
#RGM: 25647466

print("Converta um numero decimal para outra base\n")
base = input("Qual base deseja converter? \n [1]Binário \n [2]Octodecimal \n [3]Hexadecimal \n Digite a opção: ")

if base == "1" or base == "2" or base == "3":
    if base == "1":
        num1 = int(input("Digite o numero : "))
        resto = "."
        while num1 > 0:
            resto = str(num1 % 2) + resto
            num1 = int(num1 // 2)
        print(f'o numero é {resto}')
            
    elif base == "2":
        num1 = int(input("Digite o numero : "))
        resto = "."
        while num1 > 0:
            resto = str(num1 % 8) + resto
            num1 = int(num1 // 8)
        print(f'o numero é {resto}')
        
    elif base == "3":
        
        num1 = int(input("Digite o numero : "))
        resto = "."
        
        while num1 > 0:
            
            verificacao = (num1 % 16)

            if verificacao == 10:
                letra = "A"
                resto = letra + resto
                num1 = int(num1 // 16)
                
            elif verificacao == 11:
                letra = "B"
                resto = letra + resto
                num1 = int(num1 // 16)

            elif verificacao == 12:
                letra = "C"
                resto = letra + resto
                num1 = int(num1 // 16)
                
            elif verificacao == 13:
                letra = "D"
                resto = letra + resto
                num1 = int(num1 // 16)

            elif verificacao == 14:
                letra = "E"
                resto = letra + resto
                num1 = int(num1 // 16)

            elif verificacao == 15:
                letra = "F"
                resto = letra + resto
                num1 = int(num1 // 16)
                
            else:
                
                resto = str(num1 % 16) + resto

                num1 = int(num1 // 16)
            
            
            
        print(f'o numero é {resto}')
        
    
else:
    print("Opção invalida")
