import matplotlib.pyplot as plt
import sys
sys.setrecursionlimit(10000)
def calcularMedia(listaRegiao,tamanho):
    if len(listaRegiao)==0:
        return 0.0
    else:
        return listaRegiao[0]/tamanho + calcularMedia(listaRegiao[1:len(listaRegiao)],tamanho)
        
        
def listaMedias(genero,listaForm):
    listaGenero = []
    listaNA = []
    listaEU = []
    listaJP = []
    listaOther = []
    listaGlobal = []
    for i in range(len(listaForm)):
        if genero.upper() in listaForm[i][4].upper():
            listaGenero.append(genero)
            listaNA.append(float(listaForm[i][6]))
            listaEU.append(float(listaForm[i][7]))
            listaJP.append(float(listaForm[i][8]))
            listaOther.append(float(listaForm[i][9]))
            listaGlobal.append(float(listaForm[i][10]))

    tamanho = len(listaGenero)
    mediaNA = 100*calcularMedia(listaNA,tamanho)
    mediaEU = 100*calcularMedia(listaEU,tamanho)
    mediaJP = 100*calcularMedia(listaJP,tamanho)
    mediaOther = 100*calcularMedia(listaOther,tamanho)
    mediaGlobal = 100*calcularMedia(listaGlobal,int(tamanho))
    return (genero,mediaNA,mediaEU,mediaJP,mediaOther,mediaGlobal)
    
def plotagem4(genero,mediaNA,mediaEU,mediaJP,mediaOther,mediaGlobal):
    labels_list = ['NA', 'EU', 'JP', 'OTHER', 'GLOBAL']
    x_list = []
    x_list.append(mediaNA)
    x_list.append(mediaEU)
    x_list.append(mediaJP)
    x_list.append(mediaOther)
    x_list.append(mediaGlobal)
    plt.pie(x_list, labels=labels_list, autopct='%1.1f%%')
    plt.title("Locais X Media, genero {}".format(genero))
    plt.show()
    


