import matplotlib.pyplot as plt

#Funções
def calcularMediaAno(listaResult,listaCont,ano1,ano2):
    for i in range(len(listaResult)):
        listaResult[i] = float("{:.2f}".format(listaResult[i]/listaCont[i]))
        listaCont[i] = str(ano1+i)
         
def organizarListaGeneroAno(ano1,ano2,genero,listaDados):
    listaResult = [0 for x in range((ano2-ano1)+1)]
    listaCont = [0 for x in range((ano2-ano1)+1)]
    lista = []
    for i in range(len(listaDados)):
        if listaDados[i][4].upper() == genero.upper() and listaDados[i][4] != "N/A" and listaDados[i][3] != "N/A":
            if int(listaDados[i][3]) >= ano1 and int(listaDados[i][3]) <= ano2:
                listaResult[int(listaDados[i][3])-ano1] += float(listaDados[i][10])
                listaCont[int(listaDados[i][3])-ano1] += 1
    calcularMediaAno(listaResult,listaCont,ano1,ano2)
    return (listaCont,listaResult,genero)

def plotarGrafico5(listaCont,listaResult,genero):
    plt.plot(listaCont,listaResult)
    plt.title('Média das Vendas Globais\n Gênero: {}'.format(genero))
    plt.xlabel('Ano')
    plt.ylabel('Média')
    plt.show()




