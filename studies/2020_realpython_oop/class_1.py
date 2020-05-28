# ---------- #
#     OOP    #
# ---------- #

"""
Em OOP, uma entidade ou objetivo tem propriedades e comportamentos. Por
exemplo, uma pessoa. Ela tem nome, idade e endereço (são propriedades),
e ela caminha, come e dorme (são # comportamentos).

Um objeto é definido por uma classe. Uma classe única pode definir
inúmeros objetos. Essa definição leva o nome de instância.
"""


class Dog:
    """
    A função '__init__' é o inicializador, o construtor. É o que será
    chamado quando um objeto for instanciado. Cada objeto instanciado
    terá atributos iniciais próprios e independentes, como nome (name) e
    idade (age) e, por isso, usamos 'self'. Exceto quando o atributo
    estiver fora de '__init__'; neste caso, o atributo vale para todos
    os objetos instaciados.
    """

    species = 'mammal'  # Atributo de classe

    def __init__(self, name, age):
        self.name = name    # Atributo de instância
        self.age = age      # Atributo de instância


"""
Mesmo que eu use atributos de instância iguais em dois objetos, eles
serão distintos -- mas ambos serão objetos da classe 'Dog'
"""
dog_1 = Dog('Totó', 7)
dog_2 = Dog('Totó', 7)

print(dog_1 == dog_2)
# OUTPUT:
# False

print(dog_1, dog_2)
# OUTPUT:
# <__main__.Dog object at 0x7f94d6b0af50>
# <__main__.Dog object at 0x7f94d6b08050>

print(type(dog_1), type(dog_2))
# OUTPUT:
# <class '__main__.Dog'>
# <class '__main__.Dog'>

"""
É possível recuperar os atributos usando ponto (.).
"""
dog_3 = Dog('Brutus', 5)
print(dog_3.name, dog_3.age, dog_3.species)
# OUTPUT:
# Brutus 5 mammal

"""
Da mesma forma, é possível alterar atributos.
"""
dog_3.age = 4
print(dog_3.name, dog_3.age, dog_3.species)
# OUTPUT:
# Brutus 4 mammal
