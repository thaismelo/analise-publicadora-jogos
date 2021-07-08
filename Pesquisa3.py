import matplotlib.pyplot as plt

def mediaPlataforma(regiao,listaForm):
    listaPlataforma = []
    listaSoma = []
    listaCont = []
    for i in range(len(listaForm)):
        if listaForm[i][2] in listaPlataforma:
            listaSoma[listaPlataforma.index(listaForm[i][2])] += float(listaForm[i][regiao])
            listaCont[listaPlataforma.index(listaForm[i][2])] +=1
        else:
            listaPlataforma.append(listaForm[i][2])
            listaSoma.append(float(listaForm[i][regiao]))
            listaCont.append(1)
            
    listaMedias = []
    for j in range(len(listaSoma)):
        media = float(listaSoma[j])/float(listaCont[j])
        listaMedias.append(media)
        
    mediasOrdenadas = sorted(listaMedias, reverse = True) #Nova lista com as medias decrescentes
    top10Media = []
    top10Nome = []
    for k in range(10):
        top10Media.append(mediasOrdenadas[k])
        top10Nome.append(listaPlataforma[listaMedias.index(mediasOrdenadas[k])])

    return (regiao,top10Nome,top10Media)

def plotagem(regiao,top10Nome,top10Media):    
    if regiao == 6:
        plt.scatter(top10Nome,top10Media)
        plt.title('Média X Plataforma, Regiao NA_Sales')
        plt.xlabel('Plataforma')
        plt.ylabel('Média')
        plt.show()
    elif regiao == 7:
        plt.scatter(top10Nome,top10Media)
        plt.title('Média X Plataforma, Regiao EU_Sales')
        plt.xlabel('Plataforma')
        plt.ylabel('Média')
        plt.show()
    elif regiao ==8:
        plt.scatter(top10Nome,top10Media)
        plt.title('Média X Plataforma, Regiao JP_Sales')
        plt.xlabel('Plataforma')
        plt.ylabel('Média')
        plt.show()
    elif regiao == 9:
        plt.scatter(top10Nome,top10Media)
        plt.title('Média X Plataforma, Regiao Other_Sales')
        plt.xlabel('Plataforma')
        plt.ylabel('Média')
        plt.show()
    else:
        plt.scatter(top10Nome,top10Media)
        plt.title('Média X Plataforma, Regiao Global_Sales')
        plt.xlabel('Plataforma')
        plt.ylabel('Média')
        plt.show()



