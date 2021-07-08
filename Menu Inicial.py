from Pesquisa3 import *
from Pesquisa4 import *
from Pesquisa5 import *
from Pesquisa6 import *
from Pesquisa7 import *
from Pesquisa8 import *
import os.path
import re


print("-"*80)
print("")
titulo = 'BEM VINDO AO SISTEMA DE BUSCAS'
print(titulo.center(50))
print("")
print("-"*80)

login = ""

#-----------------------------------------------------------
def cadastrarPessoa():
    nome = input("Digite seu nome completo\n")
    cargo = input("Digite seu cargo na empresa\n")
    while cargo != "gerente" and cargo!="funcionario":
        print("cargo inexistente.Tente outra vez")
        cargo = input("Digite seu cargo na empresa\n")
    global login
    login = input("Digite um login\n")
    while os.path.isfile(login+'.txt'):
        print("Login já existe, tente outra vez")
        login = input("Digite um login\n")
        
    senha = input("Digite uma senha\n")
    print("Cadastrado com sucesso!")
    arquivoPessoa = open(login+'.txt','a')
    arquivoPessoa.write(str(cargo)+'\n')
    arquivoPessoa.write(str(nome)+'\n')
    arquivoPessoa.write(str(senha)+'\n')
    arquivoPessoa.close()
    #--------lendo arquivo para ver se é gerente ou funcionario
    arq = open(login+'.txt', 'r')
    form1 = (arq.read().split('\n'))
    arq.close()
    if str(form1[0]).upper() == "FUNCIONARIO":
        menuFuncionario()
    elif str(form1[0]).upper() == "GERENTE":
        menuGerente()

        
#----------------------------------------------------------   
def logarPessoa():
    global login
    login = input("Digite seu login:\n")
    senha = input("Digite sua senha:\n")
    
    if os.path.isfile(login+'.txt'):
        arq = open(login+'.txt', 'r')
        form1 = (arq.read().split('\n'))
        arq.close()
        if str(form1[2]) == str(senha):
            if str(form1[0]).upper() == "FUNCIONARIO":
                menuFuncionario()
            elif str(form1[0]).upper() == "GERENTE":
                menuGerente()
        else:
            print("Senha incorreta. Tente novamente!")
            menuInicial()
    else:
        print("Login não cadastrado")
        menuInicial()

#-------------------------------------------------------------------
        
def salvarDado(dado, login):
    arq = open('{}.txt'.format(login),'a')
    arq.write(dado)
    arq.close()
    

#-----------------------MENUS---------------------------------------       

def menuInicial():
    print("MENU INICIAL")
    print("""
    1.Cadastro
    2.Login
    """)
    numero = int(input("Escolha uma opção\n"))
    if numero == 1:
        cadastrarPessoa()
    elif numero == 2:
        logarPessoa()
    while numero >=3:
        ("Número inválido. Digite novamente")
        numero = int(input("Escolha uma opção\n"))

        
#-------------Guardando arquivo csv em uma lista---------------
handle = open('vgsales.csv','r')
form1 = (handle.read().split('\n'))
dados = []
for i in range(len(form1)):
    dados.append(form1[i].split(','))
dados.remove(dados[0])
handle.close()

#-------------------------------------------------------------------        
def menuFuncionario():
    print("-"*20+"Bem vindo a sua página"+"-"*20)
    print("""
    1. Busca 5: Media de vendas por genero em um intervalo de ano
    2. Busca 8: ToX de vendas NA e EU
    """)
    numero = int(input("Escolha uma opção\n"))
    if numero == 1:
        ano1 = int(input("Digite o primeiro ano: "))
        ano2 = int(input("Digite o segundo ano: "))
        genero = input("Digite o genero desejado: ")
        flag = 0
        arq = open(login+'.txt', 'r')
        form = (arq.read().split(":"))
        arq.close()
        for i in range(len(form)):
            if form[i] == 'b5' and form[i+1] == str(ano1) and form[i+2] == str(ano2) and form[i+3]==str(genero):
                flag =1
                genero1 = form[i+3]
                x = [i for i in re.split('\W+',form[i+4])[1:-1]]
                y = [float(j) for j in re.findall('\d\.\d\d',form[i+5])]
        if flag ==1:
            plotarGrafico5(x,y,genero)
            menuFuncionario()
        else:
            plot = organizarListaGeneroAno(ano1,ano2,genero,dados)
            dado = ":b5:" + str(ano1)+":"+str(ano2)+":"+str(genero)+":"+str(plot[0])+ ":" +str(plot[1])+":"+"\n"
            plotarGrafico5(plot[0],plot[1],plot[2])
            salvarDado(dado,login)
            menuFuncionario()
    elif numero == 2:
        topX = int(input("Qual o top desejado?"))
        flag = 0
        arq = open(login+'.txt', 'r')
        form2 = (arq.read().split(":"))
        arq.close()
        for i in range(len(form2)):
            if form2[i] == 'b8' and form2[i+1] == str(topX):
                flag = 1
                top = form2[i+1]
                x = [float(i) for i in re.findall('\d\.\d\d',form2[i+2])]
                y = [float(j) for j in re.findall('\d\.\d\d',form2[i+3])]
                w = [k for k in re.split('\W+',form2[i+4])]
        if flag ==1:
            plotarGrafico8(top,x,y,w)                
            menuFuncionario()
        else:
            plot = organizarGrafico8(dados,topX)
            dado = ':b8:'+ str(plot[0]) + ":" +str(plot[1]) +":" + str(plot[2]) + ":" +str(plot[3])+":"+"\n"
            plotarGrafico8(plot[0],plot[1],plot[2],plot[3])
            salvarDado(dado,login)
            menuFuncionario()
    while numero >=3:
        ("Número inválido")
        menuFuncionario()
        
#--------------------------------------------------------------------------------    

def menuGerente():
    print("-"*20+"Bem vindo a sua página"+"-"*20)
    print("""
    1. Busca 3: Top10 media de vendas por região
    2. Busca 4: Media de vendas por genero
    3. Busca 5: Media de vendas por genero em um intervalo de ano
    4. Busca 6: Numero de jogos de acordo com os X maiores
    5. Busca 7: Vendas globais de jogos de uma determinada publicadora
    6. Busca 8: TopX de vendas NA e EU
    7. Busca 15: Mostrar PIB
    """)
    numero = int(input("Escolha uma opção\n"))
    if numero == 1:
        numero = 0
        while numero !=6:
            print("-----Menu-----")
            print("Digite 1 para escolher NA_Sales")
            print("Digite 2 para escolher EU_Sales")
            print("Digite 3 para escolher JP_Sales")
            print("Digite 4 para escolher Other_Sales")
            print("Digite 5 para escolher Global_Sales")
            print("Digite 6 para sair")
            numero = int(input("Digite o numero desejado"))
            if numero == 1:
                nmr = 6
                flag = 0
                arq = open(login+'.txt', 'r')
                form2 = (arq.read().split(":"))
                arq.close()
                for i in range(len(form2)):
                    if form2[i] == 'b3' and form2[i+1] == str(nmr):
                        flag =1
                        n = form2[i+1]
                        x = [k for k in re.split('\W+',form2[i+2])[1:-1]]
                        y = [float(j) for j in re.findall('\d\.\d\d',form2[i+3])]
                if flag ==1:
                    plotagem(n,x,y)
                else:
                    plot = mediaPlataforma(nmr,dados)
                    dado = ':b3:' + str(plot[0]) + ":" +str(plot[1]) +":" + str(plot[2])+":"+"\n"
                    plotagem(plot[0],plot[1],plot[2])
                    salvarDado(dado,login)
            elif numero ==2:
                nmr = 7
                flag =0
                arq = open(login+'.txt', 'r')
                form2 = (arq.read().split(":"))
                arq.close()
                for i in range(len(form2)):
                    if form2[i] == 'b3' and form2[i+1] == str(nmr):
                        flag =1
                        n = form2[i+1]
                        x = [k for k in re.split('\W+',form2[i+2])[1:-1]]
                        y = [float(j) for j in re.findall('\d\.\d\d',form2[i+3])]
                if flag ==1:
                    plotagem(n,x,y)
                else:
                    plot = mediaPlataforma(nmr,dados)
                    dado = ':b3:' + str(plot[0]) + ":" +str(plot[1]) +":" + str(plot[2])+":"+"\n"
                    plotagem(plot[0],plot[1],plot[2])
                    salvarDado(dado,login)
            elif numero ==3:
                nmr = 8
                flag =0
                arq = open(login+'.txt', 'r')
                form2 = (arq.read().split(":"))
                arq.close()
                for i in range(len(form2)):
                    if form2[i] == 'b3' and form2[i+1] == str(nmr):
                        flag =1
                        n = form2[i+1]
                        x = [k for k in re.split('\W+',form2[i+2])[1:-1]]
                        y = [float(j) for j in re.findall('\d\.\d\d',form2[i+3])]
                if flag ==1:
                    plotagem(n,x,y)
                else:
                    plot = mediaPlataforma(nmr,dados)
                    dado = ':b3:' + str(plot[0]) + ":" +str(plot[1]) +":" + str(plot[2])+":"+"\n"
                    plotagem(plot[0],plot[1],plot[2])
                    salvarDado(dado,login)
            elif numero == 4:
                nmr = 9
                flag =0
                arq = open(login+'.txt', 'r')
                form2 = (arq.read().split(":"))
                arq.close()
                for i in range(len(form2)):
                    if form2[i] == 'b3' and form2[i+1] == str(nmr):
                        flag =1
                        n = form2[i+1]
                        x = [k for k in re.split('\W+',form2[i+2])[1:-1]]
                        y = [float(j) for j in re.findall('\d\.\d\d',form2[i+3])]
                if flag ==1:
                    plotagem(n,x,y)
                else:
                    plot = mediaPlataforma(nmr,dados)
                    dado = ':b3:' + str(plot[0]) + ":" +str(plot[1]) +":" + str(plot[2])+":"+"\n"
                    plotagem(plot[0],plot[1],plot[2])
                    salvarDado(dado,login)
            elif numero == 5:
                nmr = 10
                flag =0
                arq = open(login+'.txt', 'r')
                form2 = (arq.read().split(":"))
                arq.close()
                for i in range(len(form2)):
                    if form2[i] == 'b3' and form2[i+1] == str(nmr):
                        flag =1
                        n = form2[i+1]
                        x = [k for k in re.split('\W+',form2[i+2])[1:-1]]
                        y = [float(j) for j in re.findall('\d\.\d\d',form2[i+3])]
                if flag ==1:
                    plotagem(n,x,y)
                else:
                    plot = mediaPlataforma(nmr,dados)
                    dado = ':b3:' + str(plot[0]) + ":" +str(plot[1]) +":" + str(plot[2])+":"+"\n"
                    plotagem(plot[0],plot[1],plot[2])
                    salvarDado(dado,login)
            elif numero == 6:
                print("Finalizando....")
            else:
                print("Opção inválida, tente novamente")
        print("Fim da busca")
        menuGerente()
    elif numero == 2:
        genero = input("Digite um genero:\n")
        flag = 0
        arq = open(login+'.txt', 'r')
        form2 = (arq.read().split(":"))
        arq.close()
        for i in range(len(form2)):
            if form2[i] == 'b4' and form2[i+1] == str(genero):
                flag = 1
                genero1 = form2[i+1]
                x = [float(j) for j in re.findall('\d\.\d\d',form2[i+2])]
                y = [float(a) for a in re.findall('\d\.\d\d',form2[i+3])]
                w = [float(b) for b in re.findall('\d\.\d\d',form2[i+4])]
                t = [float(c) for c in re.findall('\d\.\d\d',form2[i+5])]
                p = [float(d) for d in re.findall('\d\.\d\d',form2[i+6])]
        if flag ==1:
            plotagem4(genero1,x,y,w,t,p)
            menuGerente()
        else:
            plot = listaMedias(genero,dados)
            plotagem4(plot[0],plot[1],plot[2],plot[3],plot[4],plot[5])
            dado = ':b4:' +str(plot[0]) + ":" +str(plot[1]) +":" + str(plot[2]) + ":" +str(plot[3]) + ":"+ str(plot[4]) + ":" +str(plot[5])+":"+"\n"
            salvarDado(dado,login)
            menuGerente()
    elif numero ==3:
        ano1= int(input("Digite o primeiro ano do intervalo:\n"))
        ano2 = int(input("Digite o segundo ano do intervalo:\n"))
        genero = input("Digite o genero desejado:\n")
        flag = 0
        arq = open(login+'.txt', 'r')
        form = (arq.read().split(":"))
        arq.close()
        for i in range(len(form)):
            if form[i] == 'b5' and form[i+1] == str(ano1) and form[i+2] == str(ano2) and form[i+3]==str(genero):
                flag =1
                genero1 = form[i+3]
                x = [i for i in re.split('\W+',form[i+4])[1:-1]]
                y = [float(j) for j in re.findall('\d\.\d\d',form[i+5])]
        if flag ==1:
            plotarGrafico5(x,y,genero)
            menuGerente()
        else:
            plot = organizarListaGeneroAno(ano1,ano2,genero,dados)
            dado = ":b5:" + str(ano1)+":"+str(ano2)+":"+str(genero)+":"+str(plot[0])+ ":" +str(plot[1])+":"+"\n"
            plotarGrafico5(plot[0],plot[1],plot[2])
            salvarDado(dado,login)
            menuGerente()
    elif numero == 4:
        ano1 = int(input("Digite o primeiro ano: "))
        ano2 = int(input("Digite o segundo ano: "))
        top = int(input("Digite o topX que deseja: "))
        flag =0
        arq = open(login+'.txt', 'r')
        form = (arq.read().split(":"))
        arq.close()
        for i in range(len(form)):
            if form[i] == 'b6' and form[i+1] == str(top) and form[i+2] == str(ano1) and form[i+3]==str(ano2):
                flag =1
                top1 = form[i+1]
                anoI = form[i+2]
                anoF = form[i+3]
                x = [i for i in re.split('\W+',form[i+4])]
                y = [j for j in re.split('\W+',form[i+5])]
                z = [k for k in re.split('\W+',form[i+6])]
        if flag == 1:
            plotarGrafico6(top1,anoI,anoF,x,y,z)
            menuGerente()
        else:
            plot = buscarTopX(ano1,ano2,top,dados)
            dado = ':b6:' + str(plot[0]) + ":" +str(plot[1]) +":" + str(plot[2]) + ":" +str(plot[3]) + ":"+ str(plot[4]) + ":" +str(plot[5])+":"+"\n"
            plotarGrafico6(plot[0],plot[1],plot[2],plot[3],plot[4],plot[5])
            salvarDado(dado,login)
            menuGerente()
    elif numero == 5:
        plubicadora = input("Digite a publicadora desejada: ")
        flag = 0
        arq = open(login+'.txt', 'r')
        form = (arq.read().split(":"))
        arq.close()
        for i in range(len(form)):
            if form[i] == 'b7' and form[i+1] == str(plubicadora):
                flag = 1
                pub = str(form[i+1])
                x = [i for i in re.split('\W+',form[i+2])[1:-1]]
                y = [j for j in re.findall('\d\.\d\d',form[i+3])]
                print("{} - {} -- {}".format(x,y, form[i+3]))
        if flag==1:
            plotarGrafico7(pub,x,y)
            menuGerente()
        else:
            plot = organizarGrafico7(dados,plubicadora)
            dado = ':b7:' +  str(plot[0]) + ":" +str(plot[1]) +":" + str(plot[2])+":"+"\n"
            plotarGrafico7(plot[0],plot[1],plot[2])
            salvarDado(dado,login)
            menuGerente()
    elif numero == 6:
        topX = int(input("Qual o top desejado?"))
        flag = 0
        arq = open(login+'.txt', 'r')
        form2 = (arq.read().split(":"))
        arq.close()
        for i in range(len(form2)):
            if form2[i] == 'b8' and form2[i+1] == str(topX):
                flag = 1
                top = form2[i+1]
                x = [float(i) for i in re.findall('\d\.\d\d',form2[i+2])]
                y = [float(j) for j in re.findall('\d\.\d\d',form2[i+3])]
                w = [k for k in re.split('\W+',form2[i+4])]
        if flag ==1:
            plotarGrafico8(top,x,y,w)                
            menuGerente()
        else:
            plot = organizarGrafico8(dados,topX)
            dado = ':b8:'+ str(plot[0]) + ":" +str(plot[1]) +":" + str(plot[2]) + ":" +str(plot[3])+":"+"\n"
            plotarGrafico8(plot[0],plot[1],plot[2],plot[3])
            salvarDado(dado,login)
            menuGerente()
    while numero>=8:
        ("Número inválido. Digite novamente")
        menuGerente()
        

            
menuInicial()    
    
