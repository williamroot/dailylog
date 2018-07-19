# Carregar datasets
#
# Sintaxe:
#
# read.csv = lê csv
# header = como sabemos que há cabeçalho, TRUE
train <- read.csv("data/train.csv", header = TRUE)
test <- read.csv("data/test.csv", header = TRUE)

# Adicionar a variável 'Survived' ao dataframe 'test'
#
# Sintaxe:
#
# data.frame = manipula dataframe
# survived = nome da variável
# rep = replica o resultado 'None'...
# nrow(test) = ...na quantidade de linhas de 'test'
# test[,] = combina a nova variável ao dataframe sem definição de indexação, pois linha (antes da vírgula) e coluna (depois da vírgula) estão vazias
#
# Observação: 
#
# O nome da nova variável deve ser o mesmo nome da variável do segundo dataset
test.survived <- data.frame(Survived = rep("None", nrow(test)), test[,])

# Combinar os dois datasets
#
# Sintaxe:
#
# rbind = combina linhas de datasets
data.combined <- rbind(train, test.survived)

# Agora temos train (891 registros) com a indicação de sobreviventes, e test.survived (418 registros) sem a indicação de sobreviventes.
# Ambas agora têm a coluna 'Survived', mas train tem os valores preenchidos (0 para 'não', 1 para 'sim'), enquanto test.survived contém apenas 'None'.

# Ver a estrutura do dataframe
#
# Sintaxe:
#
# str = mostra a estrutura
#
# Observação: 
#
# 'factor' em R são valores categóricos ou enumerados; valores discretos; valores que não são úteis para operações matemáticas como soma e multiplicação
str(data.combined)

# Transformar números que são valores categóricos em factor
data.combined$Pclass <- as.factor(data.combined$Pclass)
data.combined$Survived <- as.factor(data.combined$Survived)

# Ver registros da variável 'Survived'
#
# Sintaxe:
#
# table = tabula a quantidade de registros
table(data.combined$Survived)

# Temos 549 registros com valor 0 (não sobreviveram), 342 com valor 1 (sobreviveram) e 418 com valor 'None' (não sabemos)

# Ver registros da variável 'Pclass'
table(data.combined$Pclass)

# Temos 323 registros de pessoas na 1a classe, 277 na 2a, 709 na 3a

# Importar biblioteca
library(ggplot2)

# Checar hipótese 1: Pessoas ricas têm taxa de sobrivivência maior
train$Pclass <- as.factor(train$Pclass)
str(train$Pclass)

# Criar gráfico
#
# Sintaxe:
#
# ggplot() = chama a biblioteca
# train = indica o dataframe que vamos usar no gráfico
# aes() = parametriza a estética do gráfico
# fill = factor() = transforma int em factor
# x = mostra o eixo x (no caso, valores categóricos)
# fill = indica com o que vamos preencher o gráfico
# geom_bar() = indica o tipo de gráfico
# width = define a largura das barras
# xlab = indica a label do eixo x
# ylab = indica a label do eixo y
# labs(fill) = indica as labels para os conjuntos no dataframe
ggplot(train, aes(x = Pclass, fill = factor(Survived))) +
  geom_bar(width = 0.9) +
  xlab("Classe") +
  ylab("Total de passageiros") +
  labs(fill = "Sobreviventes")

# Sim, a hipótese se confirma: o índice de sobrevivência é maior na primeira classe e menor na terceira classe

# Apresentar as primeiras linhas
#
# Sintaxe:
#
# head = apresenta as primeiras linhas...
# as.character() = ...com a variável como string
head(as.character(train$Name))

# Exibir quantidade de registros
#
# Sintaxe:
#
# lenght = mostra a quantidade...
# unique = ...de registros únicos...
# as.character = ...como string
length(unique(as.character(data.combined$Name)))

# Temos 1.307 nomes únicos
# Como há 1.309 registros no dataframe, há dois nomes duplicados

dup.names <- as.character(data.combined[which(duplicated(as.character(data.combined$Name))), "Name"])
data.combined[which(data.combined$Name %in% dup.names),]
