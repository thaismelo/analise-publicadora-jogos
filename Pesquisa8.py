import matplotlib.pyplot as plt

def listarVendasEu(lista):
    vendasEu = []
    for i in range(len(lista)):
        vendasEu.append(lista[i][2])
    return vendasEu

def listarVendasNa(lista):
    vendasNa = []
    for i in range(len(lista)):
        vendasNa.append(lista[i][1])
    return vendasNa

def listarJogos(lista):
    listaJogos = []
    for i in range(len(lista)):
        listaJogos.append(lista[i][0])
    return listaJogos

def plotarLinhas(listaNa,listaEu,listaJogos):
    for i in range(len(listaNa)):
        plt.plot(['NA','EU'],[listaNa[i],listaEu[i]],label = '{}'.format(listaJogos[i]))
        
def organizarGrafico8(listaDados,topX):
    listaJogos = []  
    for i in range(topX):
        listaJogos.append((listaDados[i][1],float(listaDados[i][6]),float(listaDados[i][7])))
    listaVendaNa = listarVendasNa(listaJogos)
    listaVendaEu = listarVendasEu(listaJogos)
    lista = listarJogos(listaJogos)
    return (topX,listaVendaNa,listaVendaEu,listaJogos)

def plotarGrafico8(topX,listaVendaNa,listaVendaEu,listaJogos):
    plotarLinhas(listaVendaNa,listaVendaEu,listaJogos)
    plt.title('Vendas nas regiões NA e EU\n Top {}'.format(topX))
    plt.xlabel('Região')
    plt.ylabel('Vendas')
    plt.legend(loc='upper right')
    plt.show()


