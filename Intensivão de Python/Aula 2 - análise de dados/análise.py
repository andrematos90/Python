import pandas as pd

#PASSO1: PEGAR E IMPORTAR BASE DE DADOS
tabela = pd.read_csv(r'C:\Users\andre\OneDrive\Documentos\GitHub\Python\Intensivão de Python\Aula 2 - análise de dados\clientes.csv', encoding='latin', sep=';')



#PASSO2: VISUALIZAR BASE DE DADOS
print(tabela)
#Entender informações que você tem disponíveis
#entender as caracteristicas dos clientes
#Procurar as "cagadas" na base de dados
#identificada coluna "Unnamed: 8" vazia que foi deletada
#deletar colunas inuteis
tabela = tabela.drop('Unnamed: 8', axis = 1)
#axis = 0 --> deletar a linha axis = 1 --> deletar uma coluna

#PASSO3: TRATAMENTO DE DADOS
#valores no formato errado
#converte a coluna "Salário Anual (R$)" para numérico e o parametro 'coerce' força a virar numérico no caso deixa ele vazio caso aja algum erro
tabela['Salário Anual (R$)'] = pd.to_numeric(tabela['Salário Anual (R$)'], errors='coerce') 
#valores vazios
tabela = tabela.dropna() # exclui todas as linhas que estão vazias
#print(tabela.info())

#PASSO4: ANÁLISE INÍCIAL
print(tabela.describe()) # descreve a tabela
#mostra o valores min e max, médias, porcentagens etc..

#PASSO5: ANÁLISE COMPLETA = TRAÇAR O PERFIL IDEAL DE CLIENTE = ENTENDER COMO CADA CARACTERISTICA IMPACTA NA NOTA 

#installar bibliotecas plotly, matplotlib, ou seaborn
import plotly.express as px

#criar gráfico
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, y='Nota (1-100)', histfunc='avg', text_auto = True, nbins=10)
    #histfunc='avg' altera a função padrao que é de soma das notas dos clientes para a de calcular a média, text_auto = True mostra o texto no gráfico, nbins=10 define o numero maximo de divisoes exibidas no gráfico

    #exibre gráfico
    grafico.show()


