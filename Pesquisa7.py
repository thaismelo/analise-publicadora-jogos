import matplotlib.pyplot as plt

def verificarPlataforma(listaDados,plataforma):
    for i in range(len(listaDados)):
        if plataforma.upper() == listaDados[i]['Plataforma'].upper():
            return i
    return -1    
    
def listarJogosPlub(listaDados,plubicadora):
    listaPlubicadora = []
    for i in range(len(listaDados)):
        if listaDados[i][5].upper() == plubicadora.upper():
            result = verificarPlataforma(listaPlubicadora,listaDados[i][2])
            if  result != -1:
                listaPlubicadora[result]['Quant'] += float(listaDados[i][10])
            else:
                novoDado = {'Plataforma': listaDados[i][2],'Quant': float(listaDados[i][10])}
                listaPlubicadora.append(novoDado)
    return listaPlubicadora

def organizarGrafico7(listaDados,plubicadora):
    listaPlubicadora = listarJogosPlub(listaDados,plubicadora)
    listaPlataformas = [listaPlubicadora[x]['Plataforma'] for x in range(len(listaPlubicadora))]
    listaQuant = [listaPlubicadora[x]['Quant'] for x in range(len(listaPlubicadora))]
    return (plubicadora,listaPlataformas,listaQuant)

def plotarGrafico7(plubicadora,listaPlataformas,listaQuant):
    plt.bar(listaPlataformas,listaQuant)
    plt.xlabel('Plataformas')
    plt.ylabel('Quantidade')
    plt.title('Vendas Globais De Jogos\n Plubicadora: {}'.format(plubicadora))
    plt.show()




