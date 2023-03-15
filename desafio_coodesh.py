# -*- coding: utf-8 -*-
"""desafio_coodesh.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JTuEhoi9cH4N3WdoDyEB9NtSL4RotmjV

## **Desafio Coodesh**

**Importando as bibliotecas necessárias para o projeto**
"""

# importando o pandas e fazendo a leitura dos arquivos CSV
import pandas as pd
import numpy as np
from collections import Counter
import itertools

"""**Leitura dos arquivos em CSV e mescla dos data frames**"""

# leitura dos arquivos em csv
df_amazon = pd.read_csv('/content/amazon_prime_titles.csv')
df_netflix = pd.read_csv('/content/netflix_titles.csv') 

# mescla dos data frames conforme orientação do desafio
merged_df = pd.merge(df_amazon, df_netflix, on='show_id', suffixes=('_amazon', '_netflix'))
print(merged_df.head(10))

"""**1- Top 10 atores/atrizes considerando todos os dados;**"""

# criando um DataFrame com as colunas de elenco de ambas plataformas
df_cast = pd.DataFrame(merged_df.loc[:,['cast_amazon', 'cast_netflix']])

# dropando os valores nan do DataFrame e transformando-os em string
df_cast = df_cast.dropna(subset=df_cast.columns).astype(str)

# como identifiquei listas dentro de listas na coluna de elenco, dei um split em cada coluna do DataFrame 
# para separar os elementos e contar de forma unitária 
cast_amazon = list(map(lambda x: x.split(','), df_cast['cast_amazon']))
cast_netflix = list(map(lambda x: x.split(','), df_cast['cast_netflix']))

# flatten a lista de listas em uma única lista
cast_amazon_chain = list(itertools.chain(*cast_amazon))
cast_netflix_chain = list(itertools.chain(*cast_netflix))

# transformei as listas criadas em séries para utilização do método value_counts()
cast_amazon_serie = pd.Series(cast_amazon_chain)
cast_netflix_serie = pd.Series(cast_netflix_chain)

# contar quantas vezes cada nome se repete em cada lista
contagem_cast_amazon = cast_amazon_serie.value_counts()
contagem_cast_netflix = cast_amazon_serie.value_counts()

# mescla das contagens de cada lista para criar o top10
contagem_cast_total = contagem_cast_amazon + contagem_cast_netflix

# criar o top 10 de atores do DataFrame
cast_top_10 = contagem_cast_total.head(10)

# impressão do resultado
print(cast_top_10)

"""**2- Top 5 países produtores de conteúdos considerando todos os dados e comparando as duas plataformas**

"""

# criando um DataFrame com as colunas de elenco de ambas plataformas
df_country = pd.DataFrame(merged_df.loc[:,['country_amazon', 'country_netflix']])

# dropando os valores nan do DataFrame e transformando-os em string
df_country = df_country.dropna(subset=df_country.columns).astype(str)

# como identifiquei listas dentro de listas na coluna de elenco, dei um split em cada coluna do DataFrame 
# para separar os elementos e contar de forma unitária 
country_amazon = list(map(lambda x: x.split(','), df_country['country_amazon']))
country_netflix = list(map(lambda x: x.split(','), df_country['country_netflix']))

# flatten a lista de listas em uma única lista
country_amazon_chain = list(itertools.chain(*country_amazon))
country_netflix_chain = list(itertools.chain(*country_netflix))

# transformei as listas criadas em séries para utilização do método value_counts()
country_amazon_serie = pd.Series(country_amazon_chain)
country_netflix_serie = pd.Series(country_netflix_chain)

# removendo os espaços em branco das séries criadas
country_amazon_serie = country_amazon_serie.str.strip()
country_netflix_serie = country_netflix_serie.str.strip()

# contar quantas vezes cada nome se repete em cada lista
contagem_country_amazon = country_amazon_serie.value_counts()
contagem_country_netflix = country_amazon_serie.value_counts()

# mescla das contagens de cada lista para criar o top10
contagem_country_total = contagem_country_amazon + contagem_country_netflix

# criar o top 10 de atores do DataFrame
cast_top_5 = contagem_country_total.head(5)

# impressão do resultado
print(cast_top_5)

"""**3- Mês no qual há mais adições de filmes na plataforma Netflix**"""

# Criar um DataFrame com as colunas "Filmes" e "Data"
df_filmes_netflix = pd.DataFrame(merged_df.loc[:,['date_added_netflix', 'title_netflix']])

# Converter a coluna de datas em um objeto do tipo datetime
df_filmes_netflix["date_added_netflix"] = pd.to_datetime(df_filmes_netflix["date_added_netflix"])

# Extrair o mês de cada data
df_filmes_netflix["date_added_netflix"] = df_filmes_netflix["date_added_netflix"].dt.month

# Contar quantos filmes foram adicionados em cada mês
count_mes = df_filmes_netflix["date_added_netflix"].value_counts()

# Selecionar o mês com o maior número de filmes adicionados
mes_mais_filmes = count_mes.index[0]

# Imprimir o mês com o maior número de filmes adicionados
print("O mês com mais filmes adicionados é:", int(mes_mais_filmes))

"""**4- Quantidade de filmes listados como comédia**"""

# criando um DataFrame com as colunas de categoria de ambas plataformas
df_genre = pd.DataFrame(merged_df.loc[:,['listed_in_amazon', 'listed_in_netflix']])

# como identifiquei listas dentro de listas na coluna de elenco, dei um split em cada coluna do DataFrame 
# para separar os elementos e contar de forma unitária 
genre_amazon = list(map(lambda x: x.split(','), df_genre['listed_in_amazon']))
genre_netflix = list(map(lambda x: x.split(','), df_genre['listed_in_netflix']))

# flatten a lista de listas em uma única lista
genre_amazon_chain = list(itertools.chain(*genre_amazon))
genre_netflix_chain = list(itertools.chain(*genre_netflix))

# transformei as listas criadas em séries para utilização do método value_counts()
genre_amazon_serie = pd.Series(genre_amazon_chain)
genre_netflix_serie = pd.Series(genre_netflix_chain)

# removendo os espaços em branco das séries criadas
genre_amazon_serie = genre_amazon_serie.str.strip()
genre_netflix_serie = genre_netflix_serie.str.strip()

# contar quantas vezes cada nome se repete na lista
contagem_genre_amazon = genre_amazon_serie.value_counts()
contagem_genre_netflix = genre_amazon_serie.value_counts()

# mescla das contagens de cada lista para criar o top10
contagem_total = contagem_genre_amazon + contagem_genre_netflix

# contagem apenas dos filmes que fazem parte da categoria comédia
contagem_total_comedia = contagem_total['Comedy']

# impressão do resultado
print(contagem_total_comedia)

"""**5- Lista de todos os gêneros de filmes**"""

# mescla das séries que trazem os gêneros dos filmes
genre_total_serie = genre_amazon_serie + genre_netflix_serie

# trazendo os valores únicos dentro da série de gêneros
generos_distintos = genre_total_serie.unique()

# impressão do resultado
print(generos_distintos)

"""**6 e 7 - A frequência de "TV Show" e "Movies" de todos os dados e comparativamente em relação as duas plataformas**"""

# concatenação das colunas de tipo de ambas plataformas
tv_show_merge = pd.concat([merged_df['type_amazon'], merged_df['type_netflix']])

# contagem dos valores dentro do DataFrame de ambas as plataformas
tv_show_count = tv_show_merge.value_counts()

# contagem dos valores apenas da coluna de tipo dos filmes da Amazon
tv_show_amazon_count = merged_df['type_amazon'].value_counts()

# contagem dos valores apenas da coluna de tipo dos filmes da Netflix
tv_show_netflix_count = merged_df['type_netflix'].value_counts()

# impressão do resultado de forma organizada
print("Quantidade de registros por tipo:")
print(tv_show_count)
print("\nQuantidade de registros na Amazon por tipo:")
print(tv_show_amazon_count)
print("\nQuantidade de registros na Netflix por tipo:")
print(tv_show_netflix_count)