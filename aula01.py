# faz a importação da biblioteca matplotlib e adiciona um alias (apelido)
# usar linha de comando: python3 -m pip install matplotlib
import matplotlib.pyplot as plt

def exibirGráfico():
    #Definição dos grupos e valores
   grupos = ['A', 'B', 'C',]
   valores = [23, 38, 12]

   # Configura um gráfico de barras, onde recebe os grupos, valores
   # E opcionalmente as cores 
   plt. bar(grupos, valores, color=['red', 'blue', 'grey',])
   
   #Define o titulo do grafico
   plt.title('Grafico de barras simples')

   #Define o titulo do eixo x
   plt.xlabel('Grupos')

   #Define o titulo do eixo x
   plt.ylabel ('Valores')
   
   #Crie o grafico 
   plt.show()

   #Salva dentro do arquivo de imagem
   plt.savefig('Chart.png')