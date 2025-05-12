import random

lista_de_pratos = ["lasanha", "feijoada", "strogonoff", "pizza", "hambúrguer", "sushi", "tacos", "risoto", "coxinha", "churrasco" , "podrão" , "rabada"]

prato_secreto = random.choice(lista_de_pratos)
print(prato_secreto)    


while True:
    nivel = str(input("\n1 - Fácil \n2 - Médio \n3 - Difícil \nEscolha seu nível: "))

    if nivel == "1":
        tentativa = 7
        print("Você terá {} jogadas".format(tentativa))
        break
    elif nivel == "2":
        tentativa = 5
        print("Você terá {} jogadas".format(tentativa))
        break       
    elif nivel == "3":
        tentativa = 3     
        print("Você terá {} jogadas".format(tentativa))
        break
    else:
        print("Escolha corretamente sua dificuldade de jogo")
    

print("-"*200)
print("Jogo de Adivinhação: Descubra o prato secreto!")
print(", ".join(lista_de_pratos))

for jogada in range(1, tentativa+1):
    palpite = str(input("Qual o prato delicioso secreto ? ").lower())
    if palpite == prato_secreto:
        print("Parabéns você acertou o prato secreto! {} é meu favorito também!".format(palpite))
        break
    else:
        restam = (tentativa) - jogada
        print("Você errou! Restam {} tentativas".format(restam))
