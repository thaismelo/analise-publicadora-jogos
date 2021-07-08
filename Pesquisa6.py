import matplotlib.pyplot as plt

def preencherDadosAnos(listaAnos,anoInicial,anoGenero,genero):
    flag = 0
    for i in range(len(listaAnos[anoGenero-anoInicial])):
        if listaAnos[anoGenero-anoInicial][i]['Genero'] == genero:
            listaAnos[anoGenero-anoInicial][i]['Valor'] += 1
            flag = 1
    if flag == 0:
        add = {'Genero': genero,'Valor': 1}
        listaAnos[anoGenero-anoInicial].append(add)

def formatarLista(listaAnos,listaGenero):
    listaAnosTemp = [[0 for k in range(len(listaGenero))] for k in range(len(listaAnos))]
    for i in range(len(listaGenero)):                                                   
        for k in range(len(listaAnos)):
            for j in range(len(listaAnos[k])):                                      
                if listaGenero[i] == listaAnos[k][j]['Genero']:
                    listaAnosTemp[k][i] = (listaAnos[k][j]['Valor'])
                    break    
    return listaAnosTemp

def plotarLinhas(intervaloAnos,listaDadosAnos,maximosGen):
    for k in range(len(maximosGen)):
        listaTemp = []
        for i in range(len(listaDadosAnos)):
            listaTemp.append(listaDadosAnos[i][k])
        plt.plot(intervaloAnos,listaTemp,label = '{}'.format(maximosGen[k]))

       
def buscarTopX(anoInicial,anoFinal,topX,listaForm):

    #Separar lista
    listaAnos = []
    for i in range(anoFinal-anoInicial+1):
        listaAnos.append([])

    #Intervalos dos anos
    intervaloAnos = [str(k) for k in range(anoInicial,anoFinal+1)]
    
    #Contagem total
    listaGeneros = []
    listaContadores = []
    for k in range(len(listaForm)):
        if listaForm[k][3] != "N/A":
                if int(listaForm[k][3]) >= anoInicial and int(listaForm[k][3]) <= anoFinal and listaForm[k][4] not in listaGeneros:
                    listaGeneros.append(listaForm[k][4])
                    listaContadores.append(1)
                    preencherDadosAnos(listaAnos,anoInicial,int(listaForm[k][3]),listaForm[k][4])
                elif int(listaForm[k][3]) >= anoInicial and int(listaForm[k][3]) <= anoFinal and listaForm[k][4] in listaGeneros:
                    listaContadores[listaGeneros.index(listaForm[k][4])] +=1
                    preencherDadosAnos(listaAnos,anoInicial,int(listaForm[k][3]),listaForm[k][4])

    #Separando os maiores generos
    maximos = []
    maximosGen = []
    for top in range(topX):
        maximos.append(max(listaContadores))
        maximosGen.append(listaGeneros[listaContadores.index(max(listaContadores))])
        listaGeneros.remove(maximosGen[top])
        listaContadores.remove(max(listaContadores))

    listaFormatada = formatarLista(listaAnos,maximosGen)
    return (topX,anoInicial,anoFinal,intervaloAnos,listaFormatada,maximosGen)

def plotarGrafico6(topX,anoInicial,anoFinal,intervaloAnos,listaFormatada,maximosGen):        
    plotarLinhas(intervaloAnos,listaFormatada,maximosGen)
    plt.title('Top {} de jogos produzidos por gênero\nEntre {} e {}'.format(topX,anoInicial,anoFinal))
    plt.xlabel('Anos')
    plt.ylabel('Quantidade de jogos produzidos')
    plt.legend(loc='upper right')
    plt.show()

