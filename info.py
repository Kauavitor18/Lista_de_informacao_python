'''Programa em python usando uma lista onde tem nome, idade e altura sobre um determinado usuario, e através dos seus metodos
poderemos adicionar um elemento ou fazer sua remoção'''


usuario = ["Kauã", 19, 1.83]
print(usuario)
print("Seus Dados estão corretos?")
interagir = int(input("Digite 1 para sim e 2 para não: "))
if interagir == 1:
     print(f"Nenhum erro, seus dados são{usuario}")
elif interagir == 2:
    error = int(input("O que está errado? 1 para nome, 2 para idade, 3 para altura: "))
    if error == 1:
            usuario.pop(0) #método pop para a remoção do indice 
            nome = str(input("Digite um novo nome: "))
            usuario.insert(0, nome) # método insert informando o indice onde será adicionado e nome escolhido
            print("Dado atualizado, suas informações são", usuario)
            
    elif error == 2:
            usuario.pop(1) 
            idade = int(input("Digite uma nova idade: "))
            usuario.insert(1, idade)
            print("Dado atualizado, suas informações são", usuario)
        
    elif error == 3:
            usuario.pop(2)
            altura = float(input("Digite uma nova altura: "))
            usuario.insert(2, altura)
            print("Dado atualizado, suas informações são", usuario)
            
else:
    print("Erro")
            
    
