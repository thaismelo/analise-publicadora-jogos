
import re

arq = open('thais.txt', 'r')
form1 = (arq.read().split(":"))
arq.close()
for i in range(len(form1)):
        if form1[i] == 'b3' and form1[i+1] == '3':
                print("{} - {}".format(form1[i+2],form1[i+3]))
print("{}".format(form1))
        
      
