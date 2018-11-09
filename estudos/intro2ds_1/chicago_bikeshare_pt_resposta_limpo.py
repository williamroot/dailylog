# coding: utf-8

import csv
import matplotlib.pyplot as plt

with open("data/chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Número de linhas:", len(data_list)) # Imprimindo a quantidade de registros
print("Linha 0: ", data_list[0]) # Imprimindo a primeira linha (cabeçalhos)
print("Linha 1: ", data_list[1]) # Imprimindo a segunda linha (primeiro registro)
input("\nAperte Enter para continuar...")
# ------------------------------

print("Imprimindo as primeiras 20 amostras")
for i, line in enumerate(data_list[1:21]): # Desconsiderando índice 0, de cabeçalhos
    print("Linha {}: {}".format(i + 1, line))
input("\nAperte Enter para continuar...")
# ------------------------------

data_list = data_list[1:] # Removendo o cabeçalho
print("Imprimindo o gênero das primeiras 20 amostras")
for i, line in enumerate(data_list[:20]):
    print("Linha {}: {}".format(i + 1, line[6]))
input("\nAperte Enter para continuar...")
# ------------------------------

print("Imprimindo a lista de gêneros das primeiras 20 amostras")


def column_to_list(data, index):
    """
    Adiciona colunas de uma lista em outra lista, na mesma ordem
    Argumentos:
    - data (list): a lista cujos valores serão copiados numa coluna
    - index (int): a posição na coluna; o índice
    Retorna:
    - column_list (list): lista com valores da coluna
    """
    column_list = []
    for line in data:
        column_list.append(line[index])
    return column_list


print(column_to_list(data_list, -2)[:20])
input("\nAperte Enter para continuar...")
# ------------------------------

print("Imprimindo quantos masculinos e femininos nós encontramos")
male = 0
female = 0
gender = column_to_list(data_list, -2)
for line in gender:
    if line == 'Male':
        male += 1
    elif line == 'Female':
        female += 1
    else:
        pass # Adicionando 'else: pass' porque, na lista, não temos apenas 'male' e 'female'
print("Masculinos: ", male, "\nFemininos: ", female)
input("\nAperte Enter para continuar...")
# ------------------------------

print("Imprimindo o resultado de count_gender")


def count_gender(data_list):
    """
    Conta os gêneros e retorna uma lista
    Argumentos:
    - data_list (list): conjunto de dados original
    Retorna:
    - valores (int) no tipo lista (list)
    """
    male = 0
    female = 0
    for item in data_list:
        if item[-2] == 'Male':
            male += 1
        elif item[-2] == 'Female':
            female += 1
        else:
            pass
    return [male, female]


print(count_gender(data_list))
input("\nAperte Enter para continuar...")
# ------------------------------

print("Qual é o gênero mais popular na lista?")


def most_popular_gender(data_list):
    """
    Compara os elementos da lista gerada pela função count_gender e
    retorna o gênero com maior quantidade de ocorrências
    Argumento:
        - data_list (list): lista de dados gerais
    Retorna:
        - "Male", "Female" ou "Equal" (str)
    """
    male = count_gender(data_list)[0]
    female = count_gender(data_list)[1]
    return 'Equal' if male == female else ('Male' if male > female else 'Female')
    # ANOTAÇÃO DO RODOLFO: uma outra forma de fazer isso é:
    # answer = ""
    # if male > female:
    #     answer = "Male"
    # elif male < female:
    #     answer = "Female"
    # else:
    #     answer = "Equal"
    # return answer


print("O gênero mais popular na lista é: ", most_popular_gender(data_list))
input("\nAperte Enter para continuar...")
# ------------------------------

print("Gráfico de gênero")
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("Gráfico de tipo")
usertype_list = column_to_list(data_list, -3)
usertypes = set(usertype_list) # Como não sei os tipos disponíveis, usei `set` em `usertypes`...
users_quantity = [usertype_list.count(x) for x in usertypes] # ...e list comprehension em `users_quantity`
y_pos = list(range(len(usertypes)))
plt.bar(y_pos, users_quantity)
plt.ylabel('Quantidade')
plt.xlabel('Categorias de usuários')
plt.xticks(y_pos, usertypes)
plt.title('Quantidade por categoria de usuários')
plt.show(block=True)
input("\nAperte Enter para continuar...")
# ------------------------------

print("Por que a condição a seguir é Falsa?")
male, female = count_gender(data_list)
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Porque há valores nulos em 'data_list' -- ou seja, não são \
contabilizados nem em 'male' nem em 'female'. Para obter a resposta 'True', a \
operação válida é: male + female < len(data_list)."
print("Resposta:", answer)
input("\nAperte Enter para continuar...")
# ------------------------------

print("Imprimindo o mínimo, máximo, média, e mediana sem usar .min(), .max() etc.")
trip_duration_list = column_to_list(data_list, 2)
sorted_trip = sorted(map(int, trip_duration_list))
min_trip = sorted_trip[0]
max_trip = sorted_trip[-1]
mean_trip = 0
for trip in sorted_trip:
    mean_trip += trip
mean_trip = round(mean_trip / len(trip_duration_list))
if len(trip_duration_list) % 2 == 0:
    median_trip = (sorted_trip[int(len(trip_duration_list) / 2) - 1] + \
                  sorted_trip[int(len(trip_duration_list) / 2) + 1]) / 2
else:
    median_trip = sorted_trip[int(len(trip_duration_list) / 2) + 1]
print("Min: ", min_trip, "\nMax: ", max_trip, "\nMédia: ", mean_trip, "\nMediana: ", median_trip)
input("\nAperte Enter para continuar...")
# ------------------------------

print("Imprimindo as start stations:")
start_stations = set(column_to_list(data_list, 3))
print(start_stations)
print("\nQuantidade de estações: ", len(start_stations))
input("\nAperte Enter para continuar...")
