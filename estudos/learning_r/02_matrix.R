# MATRIX

# A matrix is two-dimensional. It means it is a collection of elements 
# of # the same data type (numeric, character, or logical) arranged into 
# a fixed number of rows and columns. 

# To construct a matrix we use the matrix() function. 

# Example:

example <- matrix(1:9, byrow=TRUE, nrow=3)

# Here I constructed a matrix with number from 1 to 9 (1:9), and I
# indicated I wanted these number row-wise distributed (byrow=TRUE)
# and three rows (nrow=3).

# Let's see if it worked:

example
#      [,1] [,2] [,3]
# [1,]    1    2    3
# [2,]    4    5    6
# [3,]    7    8    9

# Let's see what it looks like if I choose column-wise distribution:

example_2 <- matrix(1:9, byrow=FALSE, nrow=3)

example_2
#      [,1] [,2] [,3]
# [1,]    1    4    7
# [2,]    2    5    8
# [3,]    3    6    9

# Now let's work with real data (from DataCamp course). First, we create three vectors:

new_hope <- c(460.998, 314.4)
empire_strikes <- c(290.475, 247.900)
return_jedi <- c(309.306, 165.8)

# Then we combine them.

box_office <- c(new_hope, empire_strikes, return_jedi)

# Let's check:

box_office
# [1] 460.998 314.400 290.475 247.900 309.306 165.800

# Let's convert them into a matrix:

star_wars_matrix <- matrix(box_office, byrow=TRUE, nrow=3)

# Let's check:

star_wars_matrix
#         [,1]  [,2]
# [1,] 460.998 314.4
# [2,] 290.475 247.9
# [3,] 309.306 165.8

# We have three rows (one for each title) and two columns (one for each 
# region). Let's name rows and columns using rownames() and colnames().
# These functions attribute names to rows and columns of a matrix.

rownames(star_wars_matrix) <- c("A New Hope", 
                                "The Empire Strikes Back", 
                                "Return of the Jedi")
colnames(star_wars_matrix) <- c("US", "non-US")

star_wars_matrix
#                              US non-US
# A New Hope              460.998  314.4
# The Empire Strikes Back 290.475  247.9
# Return of the Jedi      309.306  165.8

# Another way of naming rows and columns is using the argument 
# dimnames() -- first rows, then columns -- when building a matrix. It
# works like: dimnames=list(c(row1, row2), c(col1, col2)).

star_wars_matrix_2 <- matrix(box_office, nrow=3, byrow=TRUE,
                             dimnames=list(c("A New Hope", 
                                             "The Empire Strikes Back", 
                                             "Return of the Jedi"), 
                                           c("US", "non-US")))

star_wars_matrix_2
#                              US non-US
# A New Hope              460.998  314.4
# The Empire Strikes Back 290.475  247.9
# Return of the Jedi      309.306  165.8

# We can see the revenue by movie and region. What if we want to check
# the total by movie (US + non-US)? We can use rowSums(), function that
# sums the values of each row.

rowSums(star_wars_matrix)
#              A New Hope The Empire Strikes Back      Return of the Jedi 
#                 775.398                 538.375                 475.106

# Is there a colSums() to check the revenue by region?

colSums(star_wars_matrix)
#       US   non-US 
# 1060.779  728.100

# Now let's add a column with the total per title. To do that we need
# cbind() function. The arguments are the matrix to which we want to 
# add a column and what we want to add.

total <- cbind(star_wars_matrix, rowSums(star_wars_matrix))

total
#                              US non-US        
# A New Hope              460.998  314.4 775.398
# The Empire Strikes Back 290.475  247.9 538.375
# Return of the Jedi      309.306  165.8 475.106

# It worked, but there is a colname missing. Let's work it out:

colnames(total) <- c("US", "non-US", "Total")

total
#                              US non-US   Total
# A New Hope              460.998  314.4 775.398
# The Empire Strikes Back 290.475  247.9 538.375
# Return of the Jedi      309.306  165.8 475.106

# Let's do the same operation, now summing the columns and adding
# a row with rbind() function:

total <- rbind(total, colSums(total))

rownames(total) <- c("A New Hope", "The Empire Strikes Back", 
                     "Return of the Jedi", "Total")

total
#                               US non-US    Total
# A New Hope               460.998  314.4  775.398
# The Empire Strikes Back  290.475  247.9  538.375
# Return of the Jedi       309.306  165.8  475.106
# Total                   1060.779  728.1 1788.879

# cbind() and rbind() aggregate rows and columns to a matrix. They
# even concatenate two matrices. For instance, let's create two
# marices -- one for originals and another for prequels:

# Originals

new_hope <- c(460.998, 314.4)
empire_strikes <- c(290.475, 247.900)
return_jedi <- c(309.306, 165.8)
box_office_or <- c(new_hope, empire_strikes, return_jedi)
originals <- matrix(box_office_or, nrow=3, byrow=TRUE,
                    dimnames=list(c("A New Hope", 
                                    "The Empire Strikes Back", 
                                    "Return of the Jedi"), 
                                  c("US", "non-US")))

originals
#                              US non-US
# A New Hope              460.998  314.4
# The Empire Strikes Back 290.475  247.9
# Return of the Jedi      309.306  165.8

# Prequels

phantom_menace <- c(474.5, 552.5)
attack_of_clones <- c(310.7, 338.7)
revenge_of_sith <- c(380.3, 468.5)
box_office_pr <- c(phantom_menace, attack_of_clones, revenge_of_sith)
prequels <- matrix(box_office_pr, nrow=3, byrow=TRUE,
                   dimnames=list(c("The Phantom Menace", 
                                   "Attack of the Clones", 
                                   "Revenge of the Sith"),
                                 c("US", "non-US")))

prequels
#                         US non-US
# The Phantom Menace   474.5  552.5
# Attack of the Clones 310.7  338.7
# Revenge of the Sith  380.3  468.5

all_movies <- rbind(originals, prequels)

all_movies
#                              US non-US
# A New Hope              460.998  314.4
# The Empire Strikes Back 290.475  247.9
# Return of the Jedi      309.306  165.8
# The Phantom Menace      474.500  552.5
# Attack of the Clones    310.700  338.7
# Revenge of the Sith     380.300  468.5

# Now let's do some operations:

# Checking total revenue by region:

colSums(all_movies)
#       US   non-US 
# 2226.279 2087.800

# Checking total revenue bu title:

rowSums(all_movies)
#              A New Hope The Empire Strikes Back      Return of the Jedi 
#                 775.398                 538.375                 475.106 
#      The Phantom Menace    Attack of the Clones     Revenge of the Sith 
#                1027.000                 649.400                 848.800

# Checking summary:

summary(all_movies)
#       US            non-US     
# Min.   :290.5   Min.   :165.8  
# 1st Qu.:309.7   1st Qu.:264.5  
# Median :345.5   Median :326.6  
# Mean   :371.0   Mean   :348.0  
# 3rd Qu.:440.8   3rd Qu.:436.1  
# Max.   :474.5   Max.   :552.5

