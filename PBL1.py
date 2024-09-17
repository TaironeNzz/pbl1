#Autor: Tairone de Jesus Lima
#Componente curricular: MI algoritmos 1
#Concluído em: 14/09/2024
#Eu declaro que este código foi elaborado por mim de forma individual e não contém nenhum
#trecho de código de outro colega ou de outro autor, tais como provindos de livros e
#apostilas, e páginas ou documentos eletrônicos da internet. Qualquer trecho de código
#de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
#do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.


#COMANDO PRA LIMPAR O TERMINAL:
import os
#MENU:
print("-----------------------MENU:----------------------")
print(" [1] Para digitar os nomes das equipes")
print(" [2] Para adicionar os pesos dos problemas")
print(" [3] Para adicionar pontos nas equipes e o tempo")
print(" [4] Para ver a tabela de Classificação e as informações")
print(" [5] Para encerrar")
print("--------------------------------------------------")
menu = int(input("=> Digite o número: "))
os.system("cls")
#DIGITAR OS NOMES DAS EQUIPES:
while menu > 0 and menu < 5:
    if menu == 1:
        equipe1 = input("Nome da equipe 1: ").upper()
        os.system("cls")
        equipe2 = input("Nome da equipe 2: ").upper()
        os.system("cls")
        equipe3 = input("Nome da equipe 3: ").upper()
        os.system("cls")
        equipe4 = input("Nome da equipe 4: ").upper()
        os.system("cls")
        equipe5 = input("Nome da equipe 5: ").upper()
        os.system("cls")
        #SAÍDA DOS NOMES DAS EQUIPES:
        print(f"EQUIPES => {equipe1} | {equipe2} | {equipe3} | {equipe4} | {equipe5}")
        #ESPAÇAMENTO ENTRE OS NOMES DAS EQUIPES E O MENU:
        print()
    #DIGITAR OS PESOS DE ACORDO COM A DIFICULDADE:
    elif menu == 2:
        facil = float(input("Digite o peso dos problemas fáceis: "))
        medio = float(input("Digite o peso dos problemas médios: "))
        dificil = float(input("Digite o peso dos problemas difíceis: "))
        os.system("cls")
        #SAÍDA DOS PESOS DE ACORDO COM A DIFICULDADE:
        print(f"o peso das fáceis são {facil} pontos")
        print(f"o peso das médias são {medio} pontos")
        print(f"o peso das difíceis são {dificil} pontos")
        #ESPAÇAMENTO ENTRE OS PESOS E O MENU:
        print()
    #QUANTIDADE DE PROBLEMAS RESOLVIDOS PELA EQUIPE 1,PONTUAÇÃO E O TEMPO
    elif menu == 3:
        print(f"-> Digite a quantidade de problemas resolvidos pela equipe {equipe1} de acordo com a dificuldade! <-")
        pf1 = int(input("Fácil: "))
        pm1 = int(input("Médio: "))
        pd1 = int(input("Difícil: "))
        print("-> Digite o tempo gasto em minutos! <-")
        t1 = float(input(f"Tempo total gasto: "))
        pontuacao1 = (pf1 * facil) + (pm1 * medio) + (pd1 * dificil)
        ranking1 = 1
        os.system("cls")
    #QUANTIDADE DE PROBLEMAS RESOLVIDOS PELA EQUIPE 2,PONTUAÇÃO E O TEMPO
        print(f"-> Digite a quantidade de problemas resolvidos pela equipe {equipe2} de acordo com a dificuldade! <-")
        pf2 = int(input("Fácil: "))
        pm2 = int(input("Médio: "))
        pd2 = int(input("Difícil: "))
        print("-> Digite o tempo gasto em minutos! <-")
        t2 = float(input("Tempo total gasto: "))
        pontuacao2 = (pf2 * facil) + (pm2 * medio) + (pd2 * dificil)
        ranking2 = 2
        os.system("cls")
    #QUANTIDADE DE PROBLEMAS RESOLVIDOS PELA EQUIPE 3,PONTUAÇÃO E O TEMPO
        print(f"-> Digite a quantidade de problemas resolvidos pela equipe {equipe3} de acordo com a dificuldade! <-")
        pf3 = int(input("Fácil: "))
        pm3 = int(input("Médio: "))
        pd3 = int(input("Difícil: "))
        print("-> Digite o tempo gasto em minutos! <-")
        t3 = float(input("Tempo total gasto: "))
        pontuacao3 = (pf3 * facil) + (pm3 * medio) + (pd3 * dificil)
        ranking3 = 3
        os.system("cls")
    #QUANTIDADE DE PROBLEMAS RESOLVIDOS PELA EQUIPE 4,PONTUAÇÃO E O TEMPO
        print(f"-> Digite a quantidade de problemas resolvidos pela equipe {equipe4} de acordo com a dificuldade! <-")
        pf4 = int(input("Fácil: "))
        pm4 = int(input("Médio: "))
        pd4 = int(input("Difícil: "))
        print("-> Digite o tempo gasto em minutos! <-")
        t4 = float(input("Tempo total gasto: "))
        pontuacao4 = (pf4 * facil) + (pm4 * medio) + (pd4 * dificil)
        ranking4 = 4
        os.system("cls")
    #QUANTIDADE DE PROBLEMAS RESOLVIDOS PELA EQUIPE 5,PONTUAÇÃO E O TEMPO
        print(f"-> Digite a quantidade de problemas resolvidos pela equipe {equipe5} de acordo com a dificuldade! <-")
        pf5 = int(input("Fácil: "))
        pm5 = int(input("Médio: "))
        pd5 = int(input("Difícil: "))
        print("-> Digite o tempo gasto em minutos! <-")
        t5 = float(input("Tempo total gasto: "))
        pontuacao5 = (pf5 * facil) + (pm5 * medio) + (pd5 * dificil)
        ranking5 = 5
        troca = ()
        os.system("cls")
    #COMPARAÇÃO DOS RANKINGS:
    #OBS: USEI A VARIÁVEL TROCA PARA ARMAZENAR O VALOR DO ÚLTIMO RANKING DA CONDIÇÃO.
        #COMPARAÇÃO EQUIPE 2:
        if pontuacao2 > pontuacao1:
            troca = ranking2
            ranking2 = ranking1
            ranking1 = troca
        else:
            ranking1 = ranking1
            ranking2 = ranking2
        #COMPARAÇÃO EQUIPE 3:
        if pontuacao3 > pontuacao1:
            troca = ranking3
            ranking3 = ranking1
            ranking1 = troca
        else:
            ranking1 = ranking1
            ranking3 = ranking3
        if pontuacao3 > pontuacao2:
            troca = ranking3
            ranking3 = ranking2
            ranking2 = troca
        else:
            ranking2 = ranking2
            ranking3 = ranking3
        #COMPARAÇÃO EQUIPE 4:
        if pontuacao4 > pontuacao1:
            troca = ranking4
            ranking4 = ranking1
            ranking1 = troca
        else:
            ranking1 = ranking1
            ranking4 = ranking4
        if pontuacao4 > pontuacao2:
            troca = ranking4
            ranking4 = ranking2
            ranking2 = troca
        else:
            ranking2 = ranking2
            ranking4 = ranking4
        if pontuacao4 > pontuacao3:
            troca = ranking4
            ranking4 = ranking3
            ranking3 = troca
        else:
            ranking3 = ranking3
            ranking4 = ranking4
        #COMPARAÇÃO EQUIPE 5:
        if pontuacao5 > pontuacao1:
            troca = ranking5
            ranking5 = ranking1
            ranking1 = troca
        else:
            ranking1 = ranking1
            ranking5 = ranking5
        if pontuacao5 > pontuacao2:
            troca = ranking5
            ranking5 = ranking2
            ranking2 = troca
        else:
            ranking2 = ranking2
            ranking5 = ranking5
        if pontuacao5 > pontuacao3:
            troca = ranking5
            ranking5 = ranking3
            ranking3 = troca
        else:
            ranking3 = ranking3
            ranking5 = ranking5
        if pontuacao5 > pontuacao4:
            troca = ranking5
            ranking5 = ranking4
            ranking4 = troca
        else:
            ranking4 = ranking4
            ranking5 = ranking5
        #VARIÁVEIS PARA A ORDEM:
        finaltop1 = ()
        finaltop2 = ()
        finaltop3 = ()
        finaltop4 = ()
        finaltop5 = ()
        finalpf1,finalpf2,finalpf3,finalpf4,finalpf5 = (),(),(),(),()
        finalpm1,finalpm2,finalpm3,finalpm4,finalpm5 = (),(),(),(),()
        finalpd1,finalpd2,finalpd3,finalpd4,finalpd5 = (),(),(),(),()
        finalt1,finalt2,finalt3,finalt4,finalt5 = (),(),(),(),()
        finalpts1,finalpts2,finalpts3,finalpts4,finalpts5 = (),(),(),(),()
        #ORDENANDO OS RANKINGS:
        #EQUIPE 1:
        if ranking1 == 1:
            finaltop1,finalpf1,finalpm1,finalpd1,finalt1,finalpts1 = equipe1,pf1,pm1,pd1,t1,pontuacao1
        if ranking1 == 2:
            finaltop2,finalpf2,finalpm2,finalpd2,finalt2,finalpts2 = equipe1,pf1,pm1,pd1,t1,pontuacao1
        if ranking1 == 3:
            finaltop3,finalpf3,finalpm3,finalpd3,finalt3,finalpts3 = equipe1,pf1,pm1,pd1,t1,pontuacao1
        if ranking1 == 4:
            finaltop4,finalpf4,finalpm4,finalpd4,finalt4,finalpts4 = equipe1,pf1,pm1,pd1,t1,pontuacao1
        if ranking1 == 5:
            finaltop5,finalpf5,finalpm5,finalpd5,finalt5,finalpts5 = equipe1,pf1,pm1,pd1,t1,pontuacao1
        #EQUIPE 2:
        if ranking2 == 1:
            finaltop1,finalpf1,finalpm1,finalpd1,finalt1,finalpts1 = equipe2,pf2,pm2,pd2,t2,pontuacao2
        if ranking2 == 2:
            finaltop2,finalpf2,finalpm2,finalpd2,finalt2,finalpts2 = equipe2,pf2,pm2,pd2,t2,pontuacao2
        if ranking2 == 3:
            finaltop3,finalpf3,finalpm3,finalpd3,finalt3,finalpts3 = equipe2,pf2,pm2,pd2,t2,pontuacao2
        if ranking2 == 4:
            finaltop4,finalpf4,finalpm4,finalpd4,finalt4,finalpts4 = equipe2,pf2,pm2,pd2,t2,pontuacao2
        if ranking2 == 5:
            finaltop5,finalpf5,finalpm5,finalpd5,finalt5,finalpts5 = equipe2,pf2,pm2,pd2,t2,pontuacao2
        #EQUIPE 3:
        if ranking3 == 1:
            finaltop1,finalpf1,finalpm1,finalpd1,finalt1,finalpts1 = equipe3,pf3,pm3,pd3,t3,pontuacao3
        if ranking3 == 2:
            finaltop2,finalpf2,finalpm2,finalpd2,finalt2,finalpts2 = equipe3,pf3,pm3,pd3,t3,pontuacao3
        if ranking3 == 3:
            finaltop3,finalpf3,finalpm3,finalpd3,finalt3,finalpts3 = equipe3,pf3,pm3,pd3,t3,pontuacao3
        if ranking3 == 4:
            finaltop4,finalpf4,finalpm4,finalpd4,finalt4,finalpts4 = equipe3,pf3,pm3,pd3,t3,pontuacao3
        if ranking3 == 5:
            finaltop5,finalpf5,finalpm5,finalpd5,finalt5,finalpts5 = equipe3,pf3,pm3,pd3,t3,pontuacao3
        #EQUIPE 4:
        if ranking4 == 1:
            finaltop1,finalpf1,finalpm1,finalpd1,finalt1,finalpts1 = equipe4,pf4,pm4,pd4,t4,pontuacao4
        if ranking4 == 2:
            finaltop2,finalpf2,finalpm2,finalpd2,finalt2,finalpts2 = equipe4,pf4,pm4,pd4,t4,pontuacao4
        if ranking4 == 3:
            finaltop3,finalpf3,finalpm3,finalpd3,finalt3,finalpts3 = equipe4,pf4,pm4,pd4,t4,pontuacao4
        if ranking4 == 4:
            finaltop4,finalpf4,finalpm4,finalpd4,finalt4,finalpts4 = equipe4,pf4,pm4,pd4,t4,pontuacao4
        if ranking4 == 5:
            finaltop5,finalpf5,finalpm5,finalpd5,finalt5,finalpts5 = equipe4,pf4,pm4,pd4,t4,pontuacao4
        #EQUIPE 5:
        if ranking5 == 1:
            finaltop1,finalpf1,finalpm1,finalpd1,finalt1,finalpts1 = equipe5,pf5,pm5,pd5,t5,pontuacao5
        if ranking5 == 2:
            finaltop2,finalpf2,finalpm2,finalpd2,finalt2,finalpts2 = equipe5,pf5,pm5,pd5,t5,pontuacao5
        if ranking5 == 3:
            finaltop3,finalpf3,finalpm3,finalpd3,finalt3,finalpts3 = equipe5,pf5,pm5,pd5,t5,pontuacao5
        if ranking5 == 4:
            finaltop4,finalpf4,finalpm4,finalpd4,finalt4,finalpts4 = equipe5,pf5,pm5,pd5,t5,pontuacao5
        if ranking5 == 5:
            finaltop5,finalpf5,finalpm5,finalpd5,finalt5,finalpts5 = equipe5,pf5,pm5,pd5,t5,pontuacao5
    #TABELA DE CLASSIFICAÇÃO:
    elif menu == 4:
            print('----------------------------TABELA-------------------------------------')
            print('RANK | \tEQUIPE\t     | FÁCIL | MÉDIO | DIFÍCIL | TEMPO | PONTUAÇÃO |')
            print('-----------------------------------------------------------------------')
            print(f'1º  |\t{finaltop1}\t\t  {finalpf1}\t{finalpm1}\t {finalpd1}\t{finalt1}\t {finalpts1}')
            print('-----------------------------------------------------------------------')
            print(f'2º  |\t{finaltop2}\t\t  {finalpf2}\t{finalpm2}\t {finalpd2}\t{finalt2}\t {finalpts2}')
            print('-----------------------------------------------------------------------')
            print(f'3º  |\t{finaltop3}\t\t  {finalpf3}\t{finalpm3}\t {finalpd3}\t{finalt3}\t {finalpts3}')
            print('-----------------------------------------------------------------------')
            print(f'4º  |\t{finaltop4}\t\t  {finalpf4}\t{finalpm4}\t {finalpd4}\t{finalt4}\t {finalpts4}')
            print('-----------------------------------------------------------------------')
            print(f'5º  |\t{finaltop5}\t\t  {finalpf5}\t{finalpm5}\t {finalpd5}\t{finalt5}\t {finalpts5}')
            print('-----------------------------------------------------------------------')
            print('*OBS: O TEMPO ESTÁ EM MINUTOS!')

            #EQUIPE VENCEDORA,SUA PONTUAÇÃO E O TEMPO:
            print(f'*A EQUIPE VENCEDORA FOI A EQUIPE {finaltop1}, COM {finalpts1} PONTOS. A EQUIPE GASTOU UM TOTAL DE {finalt1} MINUTOS!')
            #DEFININDO A EQUIPE QUE RESPONDEU MAIS PROBLEMAS DIFÍCEIS:
            if pd1 > pd2  and pd1 > pd3 and pd1 > pd4 and pd1 > pd5:
                print(f'*A EQUIPE QUE RESOLVEU MAIS PROBLEMAS DIFÍCEIS FOI A {equipe1}, COM {pd1} PROBLEMAS RESOLVIDOS!')
            if pd2 > pd1  and pd2 > pd3 and pd2 > pd4 and pd2 > pd5:
                print(f'*A EQUIPE QUE RESOLVEU MAIS PROBLEMAS DIFÍCEIS FOI A {equipe2}, COM {pd2} PROBLEMAS RESOLVIDOS!')
            if pd3 > pd1  and pd3 > pd2 and pd3 > pd4 and pd3 > pd5:
                print(f'*A EQUIPE QUE RESOLVEU MAIS PROBLEMAS DIFÍCEIS FOI A {equipe3}, COM {pd3} PROBLEMAS RESOLVIDOS!')
            if pd4 > pd1  and pd4 > pd2 and pd4 > pd3 and pd4 > pd5:
                print(f'*A EQUIPE QUE RESOLVEU MAIS PROBLEMAS DIFÍCEIS FOI A {equipe4}, COM {pd4} PROBLEMAS RESOLVIDOS!')
            if pd5 > pd1  and pd5 > pd2 and pd5 > pd3 and pd5 > pd4:
                print(f'*A EQUIPE QUE RESOLVEU MAIS PROBLEMAS DIFÍCEIS FOI A {equipe5}, COM {pd5} PROBLEMAS RESOLVIDOS!')
            
            #MÉDIA DE PONTOS POR EQUIPE:
            soma = pontuacao1 + pontuacao2 + pontuacao3 + pontuacao4 + pontuacao5
            mediatotal = soma / 5
            print(f'*A MÉDIA DE PONTOS POR EQUIPE FOI DE {mediatotal} PONTOS!')
            num = int(input('Digite qualquer número para voltar para a tabela: '))
            os.system("cls")
    #ENCERRAMENTO CASO NÃO SEJA DIGITADO UM DOS NÚMEROS ACIMA:
    else:
        print('ENCERRADO!!!')
    #MENU:
    print("-----------------------MENU:----------------------")
    print(" [1] Para digitar os nomes das equipes")
    print(" [2] Para adicionar os pesos dos problemas")
    print(" [3] Para adicionar pontos nas equipes e o tempo")
    print(" [4] Para ver a tabela de Classificação e as informações")
    print(" [5] Para encerrar")
    print("--------------------------------------------------")
    menu = int(input("=> Digite o número: "))
    os.system("cls")
