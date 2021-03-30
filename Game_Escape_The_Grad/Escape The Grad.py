# Não comentei todos os códigos do algoritmo por ser muito longo, além disso, muitos possuem as mesmas funções

# No fim do algoritmo, está detalhado o while de chegada e a situação de ataque

# O algoritmo ficou muito grande porque criei um while para cada coordenada pelo motivo de cada uma delas possuir um diálogo diferente
    #então o jogador sempre terá um feedback do que está ao seu redor a medida do possível

# Mapa se baseia em (X,Y)
    # Para mover o personagem para a direita  = (X+1)
    # Para mover o personagem para a esquerda = (X-1)
    # Para mover o personagem para frente     = (Y+1)
    # Para mover o personagem para trás       = (Y-1)

print('''
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Informática (CIn) (http://www.cin.ufpe.br)
Graduando em Sistemas de Informação
IF968 - Programação 1

Autor: Vinícius Luiz da Silva França (vlsf2)
Email: vlsf2@cin.ufpe.br
Data: 2019-08-26

Copyright(c) 2019 Vinícius Luiz da Silva França
''')

print('!!!ESCAPE THE GRAD!!!\n') 
print('''< Comandos >

olhar: para olhar a interação
pegar: para  pegar  o  objeto
usar : para   usar  o  objeto

andar p/ frente   : w
andar p/ trás     : s
andar p/ esquerda : a
andar p/ direita  : d

-> Utilize todos os comandos com a letra MINÚSCULA
-> Digite apenas os comandos que o jogo descreve como possíveis
-> Jogue primeiro para depois visualizar o algoritmo, evite spoilers
-> A cada passo, considere que o jogador se movimentou 1 metro
-> Há muitas possibilidades diferentes após cada ação, apenas uma jogatina não é sucifiente para a experiência completa\n''')

skip=input('Aperte Enter para iniciar\n')

localizacao   = 'x0y0'
#localizacao  = 'x6y5' ##Para começar de um ponto específico
acao          = 0 # variável usada para mover o personagem
lanterna      = 0 # para usar futuramente (não obrigatória)
canivete      = 0 # para usar futuramente (dependendo da circunstância não é obrigatório)
chave         = 0 # para usar futuramente (obrigatório)
olhar         = 0 # ação usados em blocos interativos
suspeito_dead = 0 # variável para captar se o suspeito está vivo ou não
mochilax1y3   = 0 # variável para usar futuramente num while
janela        = 0 # variável para modificar texto caso o personagem veja a janela mais de uma vez
canivetex6y6  = -1 # variável para usar futuramente num while
acaox6y5      = 0 # variável para modificar texto caso o personagem passe por este local mais de uma vez

while(localizacao):
# primeiro while do algoritmo, enquanto 'localização' tiver valor True, o condição irá rodar
    
    while(localizacao == 'x0y0'): # Localização de início é (0,0) - Motivo: assim que mostrar o texto de introdução, irá transportar o player para a localização de início (x2y1), serve para o texto não ser reproduzido toda vez que o player for pra esta coord.
        if(acao == 0): # Serve para dar início a história (variável 'acao' ainda tem valor 0)
            print('''< Você estava andando pelos corredores escuros do CIn e.. acabou de acordar num dos Grad, não se sabe quanto tempo você esteve dentro nem quem colocou você aí,  a porta aparentemente está trancada e provavelmente você é a única pessoa que habita esse local. >\n
Você sabe que há outra saída nesta sala, porém não consegue enxergar nada! Tente encontrar logo a saída, pois, o clima tá bastante esquisito. >\n''')
            localizacao = 'x2y1'
            
    while(localizacao == 'x2y1'): #Início
        acao = input('''**Há uma carta de aluno na mesa a frente, deseja olhar?\n**Você está de costas para a porta de entrada\n**Você pode: olhar 'olhar' ou 'a' esquerda ou 'd' direita\n''')
        if (acao == 'olhar'): # Se a ação for olhar, mostrará a carta
            print('''\n "De: vlsf2 Para: tcr2 – Amanhã chego tarde, guarda meu lugar pf, não gosto dos cinco PC’s da 1ª fileira, escolhe qualquer um dos cinco computadores da última fileira (Fileira 3), tmj!"\n''')
        if (acao == 'a'): # Se a ação for andar pra esquerda:
            print('''\n**Você andou para a esquerda, porém, lá não há movimentos possíveis, já que existe uma parede a sua esquerda, além de um computador desligado que não pode ser ultrapassado, você voltou para a posição que estava.\n''')
        if (acao == 'd'): # Se a ação for andar pra direita:
            localizacao = 'x3y1' # Novo movimento
        if (acao == 's'):
            print('''\n**Por favor leia o que é informado, foi dito logo acima que a porta está trancada, tens de encontrar outra saída\n''')

    while(localizacao == 'x3y1'): # Se a localização for essa: "Se aplica a todos os while(localizacao == (X,Y))" 
        print('''\n**Há um computador desligado em sua frente que não pode ser ultrapassado, a parede está atrás de você''') # Mostrará na tela como está a situação naquele bloco
        acao = input('''**Você pode: andar para a esquerda 'a', direita 'd'\n''') # Ação a ser tomara neste bloco
        if (acao == 'a'): # Se a ação for 'a' move a esquerda
            localizacao = 'x2y1' # Nova localização
        if (acao == 'd'): # Se a ação for 'd' move a direita
            localizacao = 'x4y1' # Nova licalização

    while(localizacao == 'x4y1'):
        if(lanterna == 0):
            acao = input('''\n< Há uma mesa interativa na sua frente, deseja olhar? >\n**A parede está atrás de você\n**Você pode: olhar 'olhar' ou andar p/ esquerda 'a', ou direita 'd'\n''')
            if (acao == 'olhar'):
                print('''\n<< Você encontrou uma pequena lanterna, pode servir para alguma coisa, ou não... >>''')
                acao = input('''**Deseja pegar a lanterna?\n**Você pode: pegar 'pegar' ou 'a' esquerda ou 'd' direita\n''')
                if (acao == 'pegar'):
                    print('''\n<< Você pegou a lanterna >>\n< A lanterna está muito fraca! Você ainda não consegue enxergar muito bem com a ajuda dela >''')
                    lanterna = 1
                elif (acao == 'a'):
                    localizacao = 'x3y1'
                elif (acao == 'd'):
                    localizacao = 'x5y1'
            if (acao == 'a'):
                localizacao = 'x3y1'
            elif (acao == 'd'):
                localizacao = 'x5y1'
        if(lanterna == 1):
            acao = input('''\n**Você está na frente da mesa onde pegou a lanterna.\n**Você pode: andar pra esquerda 'a', direita 'd'\n''')
            if (acao == 'a'):
                localizacao = 'x3y1'
            if (acao == 'd'):
                localizacao = 'x5y1'

    while(localizacao == 'x5y1'):
        acao = input('''\n**Há um computador desligado em sua frente que não pode ser ultrapassado\n**Há uma janela atrás de você, deseja olhar?\n**Você pode olhar 'olhar' ou andar para esquerda 'a', direita 'd'\n''')
        if(janela == 1):
            if(acao == 'olhar'):
                print('''\n< Você olha novamente para janela, ainda tem a impressão de estar sendo observado, que estranho >\n''')
        if(janela == 0):
            if (acao == 'olhar'):
                print('''\n< Você está olhando para a janela, aparenta ser madrugada o prédio aparenta não ter energia alguma, mas você tem a leve impressão de estar sendo observado. Será que você deve olhar novamente? >''')
                janela = 1
        if (acao == 'a'):
            localizacao = 'x4y1'
        elif (acao == 'd'):
            localizacao = 'x6y1'

    while(localizacao == 'x6y1'):
        acao = input('''\n**A parede está atrás de você\n**Você pode: andar para a esquerda 'a', direita 'd', frente 'w'\n''')
        if (acao == 'a'):
            localizacao = 'x5y1'
        elif (acao == 'd'):
            localizacao = 'x7y1'
        elif (acao == 'w'):
            localizacao = 'x6y2'

    while(localizacao == 'x7y1'):
        acao = input('''\n**A mesa do professor (que não deveria estar ai) está em sua frente, que não pode ser ultrapassado\n**A parede está atrás de você\n**Você pode: andar para a esquerda 'a', direita 'd'\n''')
        if (acao == 'a'):
            localizacao = 'x6y1'
        elif (acao == 'd'):
            localizacao = 'x8y1'

    while(localizacao == 'x8y1'):
        acao = input('''\n**A mesa do professor continua em sua frente, que nao pode ser ultrapassado\n**A parede está atrás de você\n**Você pode: andar para a esquerda 'a', direita 'd'\n''')
        if (acao == 'a'):
            localizacao = 'x7y1'
        elif (acao == 'd'):
            localizacao = 'x9y1'

    while(localizacao == 'x9y1'):
        acao = input('''\n**Há uma parede em sua direita e atrás de você, você está numa borda da sala\n**Você pode: andar para a esquerda 'a', frente 'w'\n''')
        if (acao == 'a'):
            localizacao = 'x8y1'
        elif (acao == 'w'):
            localizacao = 'x9y2'

    while(localizacao == 'x6y2'):
        acao = input('''\n**Há um computador desligado em sua esquerda que não pode ser ultrapassado\n**A mesa do professor (que não deveria estar ai) está em sua direita, que não pode ser ultrapassado\n**Você pode: andar para frente 'w', trás 's'\n''')
        if (acao == 's'):
            localizacao = 'x6y1'
        elif (acao == 'w'):
            localizacao = 'x6y3'
        
    while(localizacao == 'x6y3'):
        acao = input('''\n**Não há nada em seu redor\n**Você pode: andar para esquerda 'a', direita 'd', frente 'w', trás 's'\n''')
        if(acao == 'a'):
            localizacao = 'x5y3'
        elif(acao == 'd'):
            localizacao = 'x7y3'
        elif(acao == 'w'):
            localizacao = 'x6y4'
        elif(acao == 's'):
            localizacao = 'x6y2'

    while(localizacao == 'x7y3'):
        if(mochilax1y3 == 0):
            acao = input('''\n< Você acha que viu algo à sua esquerda, lá no fim da 2ª fileira dos computadores, o que será? >\n**A mesa do professor (que não deveria estar ai) está em suas costas, que não pode ser ultrapassado\n**Você pode: andar para esquerda 'a', direita 'd', frente 'w'\n''')
            if(acao == 'a'):
                localizacao = 'x6y3'
            elif(acao == 'd'):
                localizacao = 'x8y3'
            elif(acao == 'w'):
                localizacao = 'x7y4'
        if(mochilax1y3 == 1):
            acao = input('''\n**A mesa do professor (que não deveria estar ai) está em suas costas, que não pode ser ultrapassado\n**Você pode: andar para esquerda 'a', direita 'd', frente 'w'\n''')
            if(acao == 'a'):
                localizacao = 'x6y3'
            elif(acao == 'd'):
                localizacao = 'x8y3'
            elif(acao == 'w'):
                localizacao = 'x7y4'

    while(localizacao == 'x8y3'):
        acao = input('''\n**A mesa do professor continua em suas costas, que nao pode ser ultrapassado\n**Você pode: andar para esquerda 'a', direita 'd', frente 'w'\n''')
        if(acao == 'a'):
            localizacao = 'x7y3'
        elif(acao == 'd'):
            localizacao = 'x9y3'
        elif(acao == 'w'):
            localizacao = 'x8y4'

    while(localizacao == 'x9y3'):
        acao = input('''\n< Você está escutando muitos ruidos em sua frente, aparenta ser maribomdos, ou mosquitos. >\n**Há uma parede em sua direita\n**Você pode: andar para esquerda 'a', frente 'w', trás 's'\n''')
        if(acao == 'a'):
            localizacao = 'x8y3'
        elif(acao == 'w'):
            localizacao = 'x9y4'
        elif(acao == 's'):
            localizacao = 'x9y2'

    while(localizacao == 'x9y2'):
        acao = input('''\n**A mesa do professor (que não deveria estar ai) está em sua esquerda, que não pode ser ultrapassado\n**Há uma parede em sua direita\n**Você pode: andar para frente 'w', trás 's'\n''')
        if(acao == 'w'):
            localizacao = 'x9y3'
        elif(acao == 's'):
            localizacao = 'x9y1'

    while(localizacao == 'x5y3'):
        if(olhar == 0):
            acao = input('''\n**Há uma mesa interativa na sua frente, (na mesa 5 - fileira 2) deseja olhar?\n**Você pode: olhar 'olhar' ou 'a' esquerda ou 'd' direita\n''')
            if(acao == 'olhar'):
                print('''\n< Você encontrou um chaveiro, porém não há nenhuma chave nela, procure a chave para poder sair deste Grad. >''')
                olhar = 1
            elif(acao == 'a'):
                localizacao = 'x4y3'
            elif(acao == 'd'):
                localizacao = 'x6y3'
        if(olhar == 1):
            acao = input('''\n**Você está na frente da mesa onde viu o chaveiro\n**Você pode: andar para 'a' esquerda ou 'd' direita\n''')
            if(acao == 'a'):
                localizacao = 'x4y3'
            elif(acao == 'd'):
                localizacao = 'x6y3'

    while(localizacao == 'x4y3'):
        acao = input('''\n**Há um computador desligado em sua frente que não pode ser ultrapassado\n**Você pode: andar para esquerda 'a', direita 'd'\n''')
        if(acao == 'a'):
            localizacao = 'x3y3'
        if(acao == 'd'):
            localizacao = 'x5y3'

    while(localizacao == 'x3y3'):
        acao = input('''\n**Há outro computador desligado em sua frente que não pode ser ultrapassado\n**Você pode: andar para esquerda 'a', direita 'd'\n''')
        if(acao == 'a'):
            localizacao = 'x2y3'
        elif(acao == 'd'):
            localizacao = 'x4y3'

    while(localizacao == 'x2y3'):
        if(mochilax1y3 == 0):
            acao = input('''\n**Há um computador desligado em sua frente, você acha que viu algo em sua esquerda\n**Você pode: andar para esquerda 'a', direita 'd'\n''')
        if(mochilax1y3 == 1):
            acao = input('''\n**Há um computador desligado em sua frente\n**Você pode: andar para esquerda 'a', direita 'd'\n''')
        if(acao == 'a'):
            localizacao = 'x1y3'
        elif(acao == 'd'):
            localizacao = 'x3y3'

    while(localizacao == 'x1y3'):
        if(mochilax1y3 == 0):
            acao = input('''\n**Você encontrou uma mochila de um aluno!\n**Há uma parede em sua esquerda\n**Você pode: olhar mochila 'olhar', andar para direita 'd'\n''')
            if(acao == 'olhar'):
                print('''<< Você encontrou:\n   Uma foto com a legenda "tcr2" e escrito "eliminar o mais rápido possível" >>\n   Um rascunho escrito:\n   "Flávio, tranquei tudo deixei ele lá dentro, tentei levar o chaveiro mas eu acho que a chave caiu e não sei onde está, caiu muito pela direi... ahuby ... ..">> \n<< Que estranho, parece que o escritor teve que interromper sua carta imediatamente, por que será? >>''')
                mochilax1y3 = 1
            if(acao == 'd'):
                localizacao = 'x2y3'
        if(mochilax1y3 == 1):
            acao = input('''\n**Você está na frente da mesa onde achou a mochila\n**Há uma parede em sua esquerda\n**Você pode: andar para direita 'd'\n''')
            if(acao == 'd'):
                localizacao = 'x2y3'
            
    while(localizacao == 'x7y4'):
        acao = input('''\n**Não há nada em seu redor\n**Você pode: andar para esquerda 'a', direita 'd', frente 'w', trás 's'\n''')
        if(acao == 'a'):
            localizacao = 'x6y4'
        elif(acao == 'd'):
            localizacao = 'x8y4'
        elif(acao == 'w'):
            localizacao = 'x7y5'
        elif(acao == 's'):
            localizacao = 'x7y3'

    while(localizacao == 'x6y4'):
        if(olhar == 0):
            acao = input('''\n**Há uma mesa interativa em sua esquerda, (na mesa 5 - fileira 2) deseja olhar?\n**Você pode: olhar 'olhar', andar para direita 'd', frente 'w', trás 's'\n''')
            if(acao == 'olhar'):
                acao = input('''\n< Você encontrou um chaveiro, porém não há nenhuma chave nela, procure a chave para poder sair deste Grad. >\n**Você pode: andar para direita 'd', frente 'w', trás 's'\n''')
            if(acao == 'd'):
                localizacao = 'x7y4'
            elif(acao == 'w'):
                localizacao = 'x6y5'
            elif(acao == 's'):
                localizacao = 'x6y3'
        if(olhar == 1):
            acao = input('''\n**Você está do lado da mesa onde encontrou o chaveiro\n**Você pode: andar para direita 'd', frente 'w', trás 's'\n''')
            if(acao == 'd'):
                localizacao = 'x7y4'
            elif(acao == 'w'):
                localizacao = 'x6y5'
            elif(acao == 's'):
                localizacao = 'x6y3'
            
    while(localizacao == 'x8y4'):
        acao = input('''\n< Você está escutando muito ruído em sua direita, parece ser mosquitos ou moscas. >\n**Você pode: andar para esquerda 'a', direita 'd', frente 'w', trás 's'\n''')
        if(acao == 'a'):
            localizacao = 'x7y4'
        elif(acao == 'd'):
            localizacao = 'x9y4'
        elif(acao == 'w'):
            localizacao = 'x8y5'
        elif(acao == 's'):
            localizacao = 'x8y3'

    while(localizacao == 'x8y5'):
        if(chave == 0):
            acao = input('''\n < Você encontrou a chave!! A porta de saída não deve estar muito longe, ou não... >\n**Não há nada em seu redor, exceto um ruído de inseto um pouco atrás de você\n**Você pode: pegar a chave 'pegar', andar para esquerda 'a', direita 'd', frente 'w', trás 's'\n''')
            if(acao == 'pegar'):
                print('''\n << Você pegou a chave >>''')
                chave = 1
            elif(acao == 'a'):
                localizacao = 'x7y5'
            elif(acao == 'd'):
                localizacao = 'x9y5'
            elif(acao == 'w'):
                localizacao = 'x8y6'
            elif(acao == 's'):
                localizacao = 'x8y4'
        elif(chave == 1):
            acao = input('''\n**Não há nada em seu redor\n**Você pode: andar para esquerda 'a', direita 'd', frente 'w', trás 's'\n''')
            if(acao == 'a'):
                localizacao = 'x7y5'
            elif(acao == 'd'):
                localizacao = 'x9y5'
            elif (acao == 'w'):
                localizacao = 'x8y6'
            elif (acao == 's'):
                localizacao = 'x8y4'

    while(localizacao == 'x9y5'):
        acao = input('''\n< As suas costas, você escuta um barulho muito forte de mosquitos, ou será algo mais perigoso? >\n**Há uma parede em sua direita\n**Você pode: andar para esquerda 'a', frente 'w', trás 's'\n''')
        if(acao == 'w'):
            localizacao = 'x9y6'
        elif(acao == 's'):
            localizacao = 'x9y4'
        elif(acao == 'a'):
            localizacao = 'x8y5'

    while(localizacao == 'x7y5'):
        acao = input('''\n**Não há nada em seu redor\n**Você pode: andar para esquerda 'a', direita 'd', frente 'w', trás 's'\n''')
        if(acao == 'a'):
            localizacao = 'x6y5'
        elif(acao == 'd'):
            localizacao = 'x8y5'
        elif (acao == 'w'):
            localizacao = 'x7y6'
        elif (acao == 's'):
            localizacao = 'x7y4' 

    while(localizacao == 'x6y5'):
        if(suspeito_dead == 0 and acaox6y5 == 0):
            acao = input('''\n< Você ouviu um barulho na janela, em seguida, ouviu uma mesa se movendo na sua frente, muito provavelmente você está sendo observado! Tente sair deste local >\n**Não há nada em seu redor\n**Você pode: andar para esquerda 'a', direita 'd', frente 'w', trás 's'\n''')
            acaox6y5 = 1
        elif(suspeito_dead == 0 and acaox6y5 == 1):
            acao = input('''\n< Você está muito desconfortável nesse momento, impressão sua ou você não está só? >\n**Não há nada em seu redor\n**Você pode: andar para esquerda 'a', direita 'd', frente 'w', trás 's'\n''')
        elif(suspeito_dead == 1):
            acao = input('''\n< Você está desnorteado após o confronto com o suspeito? >\n**Não há nada em seu redor\n**Você pode: andar para esquerda 'a', direita 'd', frente 'w', trás 's'\n''')
        if(acao == 'a'):
            localizacao = 'x5y5'
        elif(acao == 'd'):
            localizacao = 'x7y5'
        elif (acao == 'w'):
            localizacao = 'x6y6'
        elif (acao == 's'):
            localizacao = 'x6y4'
    
    while(localizacao == 'x5y5'):
        if(canivetex6y6 == -1):
            acao = input('''\n< Você encontrou um canivete e muitos fios cortados. (na mesa 5 - fileira 3) >\n**Há uma mesa (que não deveria estar ali) em sua esquerda, que não pode ser ultrapassado.\n**Você pode: pegar o canivete 'pegar', andar para direita 'd'\n''')
        if(canivetex6y6 == 1):
            acao = input('''\n< Você econtrou o canivete no chão! ao lado está sua lanterna >\n**Você pode: pegar o canivete e a lanterna 'pegar', andar para direita 'd'\n''')
        if(acao == 'pegar'):
            if(canivetex6y6 == -1):
                print('''\n << Você pegou o canivete >>''')
                canivete = 1
            elif(canivetex6y6 == 1):
                print('''\n<< Você pegou o canivete e a lanterna >>''')
                canivete = 1
                lanterna = 1
        if(acao == 'd'):
            localizacao = 'x6y5'
        if(canivete == 1):
            acao = input('''\n**Há um computador desligado (que não era pra estar ali) em sua direita que não pode ser ultrapassado\n**Você pode: andar para direita 'd'\n''')
            if(acao == 'd'):
                localizacao = 'x6y5'

    while(localizacao == 'x6y6'):
        if(canivete == 1):
            acao = input('''\n**Você está do lado da mesa onde viu o canivete\n**Você pode: andar para direita 'd', para frente 'w', para trás 's'\n''')
            if(acao == 'd'):
                localizacao = 'x7y6'
            elif (acao == 'w'):
                localizacao = 'x6y7'
            elif (acao == 's'):
                localizacao = 'x6y5'
        if(canivetex6y6 == -1):
            acao = input('''\n< Você encontrou um canivete e muitos fios cortados em sua esquerda. (na mesa 5 - fileira 3) >\n**Você pode: pegar a canivete 'pegar', andar para direita 'd', frente 'w', trás 's'\n''')
            if(acao == 'pegar'):
                canivetex6y6 = 1
                print('''\n< Você levou um choque nos fios cortados, o canivete caiu no chão, junto com a lanterna que você estava segurando, não caíram longe, procure-os >''')
                lanterna = 0
                acao = input('''**Você pode: andar para direita 'd', frente 'w', trás 's'\n''')
            if(acao == 'd'):
                localizacao = 'x9y5'
            elif (acao == 'w'):
                localizacao = 'x6y7'
            elif (acao == 's'):
                localizacao = 'x6y5'
        if(canivetex6y6 == 1 and canivete == 1):
            acao = input('''\n< Você tropeçou, está tonto ainda, foi desacordado a poucos minutos, você ainda está no mesmo local >\n**Você pode: andar para direita 'd', para frente 'w', para trás 's'\n''')
            if(acao == 'd'):
                localizacao = 'x7y6'
            elif (acao == 'w'):
                localizacao = 'x6y7'
            elif (acao == 's'):
                localizacao = 'x6y5'

    while(localizacao == 'x6y7'):
        if (suspeito_dead == 0):
            acao = input('''\n< Você escutou algo se mechendo à sua esquerda, estás com muito medo, mas pode ser apenas um rato qualquer, ou, sei lá... >\n**Há uma parede em sua frente\n**Você pode: andar para esquerda 'a', direita 'd', trás 's'\n''')
        if (suspeito_dead == 1):
            acao = input('''\n**Há uma parede em sua frente, que não pode ser ultrapassado\n**Você pode: andar para esquerda 'a', direita 'd', trás 's'\n''')
        if(acao == 'a'):
            if(suspeito_dead == 1):
                print('''\n< Não volte para lá, tem um defundo barrando a passagem (kkk) >''')
            else:
                localizacao = 'x5y7'
        elif (acao == 'd'):
            localizacao = 'x7y7'
        elif (acao == 's'):
            localizacao = 'x6y6'

    while(localizacao == 'x7y7'):
        if(suspeito_dead == 1):
            acao = input('''\n**Há uma parede em sua frente, depois da luta corporal você está muito desesperado!\n**Você pode: ir para esquerda 'a', direita 'd'\n''')
        elif(suspeito_dead == 0):
            acao = input('''\n**Há uma parede em sua frente, você escuta outra respiração além da sua, meu Jesus\n**Você pode: ir para esquerda 'a', direita 'd'\n''')
        if(acao == 'a'):
            localizacao = 'x6y7'
        elif(acao == 'd'):
            localizacao = 'x8y7'

    while(localizacao == 'x8y7'):
        acao = input('''\n**Há uma parede em sua frente\n**Você pode: ir para esquerda 'a', direita 'd'\n''')
        if(acao == 'a'):
            localizacao = 'x7y7'
        elif(acao == 'd'):
            localizacao = 'x9y7'
        
    while(localizacao == 'x8y6'):
        acao = input('''\n**Não há nada em seu redor\n**Você pode: andar para esquerda 'a', direita 'd', frente 'w', trás 's'\n''')
        if(acao == 'a'):
            localizacao = 'x7y6'
        elif(acao == 'd'):
            localizacao = 'x9y6'
        elif (acao == 'w'):
            localizacao = 'x8y7'
        elif (acao == 's'):
            localizacao = 'x8y5'

    while(localizacao == 'x7y6'):
        if(mochilax1y3 == 0):
            acao = input('''\n**Não há nada em seu redor\n**Você pode: andar para esquerda 'a', direita 'd', frente 'w', trás 's'\n''')
        if(mochilax1y3 == 1):
            acao = input('''\n**Não há nada em seu redor, você está pensando na carta que leu, tcr2 está definitamente encrencado\n**Você pode: andar para esquerda 'a', direita 'd', frente 'w', trás 's'\n''')
        if(acao == 'a'):
            localizacao = 'x6y6'
        elif(acao == 'd'):
            localizacao = 'x8y6'
        elif (acao == 'w'):
            localizacao = 'x7y7'
        elif (acao == 's'):
            localizacao = 'x7y5'

    while(localizacao == 'x9y6'):
        acao = input('''\n**Há uma parede em sua direita\n**Você pode: andar para esquerda 'a', frente 'w', trás 's'\n''')
        if(acao == 'a'):
            localizacao = 'x8y6'
        if(acao == 'w'):
            localizacao = 'x9y7'
        if(acao == 's'):
            localizacao = 'x9y5'
    
    while(localizacao == 'x9y7'):
        if(chave == 1): # Se você estiver com a chave:
            fim=input('''\n<< Você chegou até a porta! >>\n**Você possui a chave, para usar digite 'usar' \n''') #Mostrará este diálogo
            if(fim == 'usar'): 
                cont1 = 0
                while(cont1 < 5):
                    print('''<< VOCÊ SAIU DO GRAD!!! PARABÉNS!!! >>''')
                    cont1 += 1
                    localizacao = False # Declarei que localizacao é falso, significa que o while do início não irá rodar mais
        elif(chave == 0): # Se você NÃO estiver com a chave:
            acao = input('''\n<< Você chegou até a porta! >>\n< Você não possui a chave, volte e procure a chave pelo GRAD, não deve estar longe >\n**Você pode: andar para trás 's', para esquerda 'a'\n''')
            if(acao == 's'): # Você terá que voltar para procurar a chave
                localizacao = 'x9y6'
            if(acao == 'a'):
                localizacao = 'x8y7'
    
    while(localizacao == 'x9y4'): # Se você chegar nesta coordenada
        cont = 0
        while(cont < 5):
            print('''<< VOCÊ FOI ATACADO PELAS ABELHAS!!! PARABÉNS, VOCÊ MORREU! >>''') # Ataque a abelhas É hit-kill
            cont+=1
            localizacao = False # Declarei que localizacao é falso, significa que o while do início não irá rodar mais
    
    while(localizacao == 'x5y7'): # Se você chegar nesta coordenada:
        if(canivete == 0): # Se você não tiver um canivete você morrerá no ataque
                cont1 = 0
                while(cont1 < 5):
                    print('''\n<< VOCÊ FOI ATACADO!! VOCÊ NÃO POSSUI ALGUM OBJETO PARA SE DEFENDER, PARABÉNS VOCÊ MORREU!! >>\n''')
                    cont1 += 1
                    localizacao = False # Declarei que localizacao é falso, significa que o while do início não irá rodar mais
            
        if(canivete == 1 and lanterna == 1): # Se você tiver um canivete e uma lanterna:
            ataque = input('''\n<< VOCÊ FOI ATACADO!! VOCÊ POSSUI O CANIVETE E PODE SE DEFENDER, DIGITE 'USAR' PARA SE DEFENDER COM O CANIVETE >>\n''')
            if(ataque == 'usar'):
                usarlanterna = input('''\n< Você se defendeu e pode usar a lanterna para ver o rosto do suspeito, quem será que lhe atacou? >\n**Digite 'usar' para usar a lanterna\n**Você pode andar para direita 'd'\n''')
                if(usarlanterna == 'usar'): # Com a lanterna, você poderá ver o rosto do suspeito
                    acao = input('''\n< O suspeito era o vlsf2!! Mas você não o conhece, porque o atacou? >\n**Há uma parede na sua frente\n**Você pode andar para direita 'd'\n''')
                    suspeito_dead = 1 # Declarei valor True para a variável 'suspeito_dead', ele altera textos futuros.
                if(acao == 'd'):
                    localizacao = 'x6y7'

        elif(canivete == 1): # Se você tiver apenas o canivete
            ataque = input('''\n<< VOCÊ FOI ATACADO!! VOCÊ POSSUI O CANIVETE E PODE SE DEFENDER, DIGITE 'USAR' PARA SE DEFENDER COM O CANIVETE >>\n''')
            if(ataque == 'usar'): # Você poderá usá-lo, porém, não saberá quem é o suspeito
                acao = input('''\n< Você se defendeu, precisa sair o mais rápido possível deste GRAD! >\n**Você pode andar para direita 'd'\n''')
                suspeito_dead = 1 # Declarei valor True para a variável 'suspeito_dead', ele altera textos futuros.
                if(acao == 'd'):
                    localizacao = 'x6y7'

skip = input('''\n\na) Você foi atacado por alguém?\nb) Se você foi atacado, você sabe quem foi que lhe atacou?\nc) Se você descobriu quem o atacou, por que você acha que o suspeito lhe atacou?\n< Se você não sabe a resposta 'b', significa que você não pegou a lanterna de início ou deixou-a cair e não encontrou novamente >\n< Se você não foi atacado, jogue novamente e tente se salvar dessa situação >\n< Aperte Enter para ver o roteiro com completo >\n''')
skip = input('''vlsf2 planejava dar um fim em tcr2, então, ele escreveu um bilhete para tcr2 ir para o fundo da sala e ficou escondido, tcr2 viu a carta na sala, porém, saiu da sala paor motivos desconhecidos, o nosso personagem muito sortudo, estava caminhando no CIn, quando o cúmplice de vlsf2 - Flávio - estava vigiando conferindo se tcr2 voltava, ele se confundiu e desacordou o nosso personagem e o levou para dentro do Grad. vlsf2 achou que seria tcr2, tentou atacá-lo quando o personagem chegou próximo. tcr está sã e salvo.\n\nAperte Enter para ver os créditos finais.\n''')
print('''Chefe de algoritmo: Vinícius Luiz\nRoteirista: Vinícius Luiz\n\nDedico este jogo às abelhas e aos filhos de Flávio\nEles sabem quem são''')
    
        
        
        
    
    
    









    
