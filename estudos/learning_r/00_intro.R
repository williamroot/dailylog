# DATA TYPES

# Scalar is a single number 0-dimensional
scalar <- 12

# Vector or arrays is a row of numbers `-dimensional
vector <- c(3, 4, 5) # c() is a function to concatenate

scalar * vector
# [1] 36 48 60

scalar / vector
# [1] 4.0 3.0 2.4

# Now let's try some functions...

mean(vector)
# [1] 4

summary(vector)
# Min.  1st Qu. Median  Mean  3rd Qu. Max. 
# 3.0   3.5     4.0     4.0   4.5     5.0

# ...and plot a graph
  
x <- rnorm(100) # rnorm() is random generation. In this case it generates 100 random numbers
plot(x) # plot() plots a graph
# It worked but it cannot be shown here.

# Let's check x

summary(x)
# Min.      1st Qu.   Median  Mean      3rd Qu. Max. 
# -2.07944  -0.70927  0.03106 -0.02948  0.65696 1.66807 