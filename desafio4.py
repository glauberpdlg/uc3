import random

lista_de_pratos = ["Lasanha", "Feijoada", "Strogonoff", "Pizza", "Hambúrguer", "Sushi", "Tacos", "Risoto", "Coxinha", "Churrasco" , "Churrasco" , "Podrão" , "Rabada"]

prato_secreto = random.choice(lista_de_pratos)
print(prato_secreto)    

nivel = str(input("\n1 - Fácil \n2 - Médio \n3 - Difícil \nEscolha seu nível: "))
 
if nivel == "1":
    tentativa = 7
    print("Você terá {} jogadas".format(tentativa))
elif nivel == "2":
    tentativa = 5
    print("Você terá {} jogadas".format(tentativa))
elif nivel == "3":
    tentativa = 3
    print("Você terá {} jogadas".format(tentativa))
else:
    print("Escolha corretamente sua dificuldade de jogo")

print("-"*200)
print("Jogo de Adivinhação: Descubra o prato secreto!")
print(", ".join(lista_de_pratos))

jogada=1
for jogada in range(1, tentativa + 1):
    palpite = input(f"Tentativa {tentativa}: Digite o nome do prato: ")

    if palpite == prato_secreto:
        print(f"Parabéns! Você acertou o prato secreto: {prato_secreto}!")
        break
    else:
        restantes = tentativa - palpite
        if restantes > 0:
            print(f"Errado! Você ainda tem {restantes} tentativa(s).")
        else:
            print(f"Suas tentativas acabaram! O prato secreto era: {prato_secreto}.")



