# VECTOR

# Vectors are one-dimension arrays that can hold numeric data, character 
# data, or logical data.

# You create a vector with the combine function c(). You place the vector 
# elements separated by a comma between the parentheses.

# Let's work with this info (from Datacamp classes):

# You are gambling in Las Vegas. This is the result in a week:
 
# Poker:
# Monday: won $140
# Tuesday: lost $50
# Wednesday: won $20
# Thursday: lost $120
# Friday: won $240

# Roulette:
# Monday: lost $24
# Tuesday: lost $50
# Wednesday: won $100
# Thursday: lost $350
# Friday: won $10

# Let's create vectors:

poker <- c(140, -50, 20, -120, 240)

roulette <- c(-24, -50, 100, -350, 10)

# Let's check the output:

poker
# [1]  140  -50   20 -120  240

roulette
# [1]  -24  -50  100 -350   10

# There is no name in the output. Let's create them using name(), a 
# function designed to give a name to the elements of a vector.

# But first, let's assign the weekdays to a variable.

days <- c("Mon", "Tue", "Wed", "Thu", "Fri")
names(poker) <- days
names(roulette) <- days

# Let's check.
poker
# Mon  Tue  Wed  Thu  Fri 
# 140  -50   20 -120  240

roulette
# Mon  Tue  Wed  Thu  Fri 
# -24  -50  100 -350   10

# Right. We know hou much it was won or lost each weekday.

# Let's check the daily balance:

poker + roulette
# Mon  Tue  Wed  Thu  Fri 
# 116 -100  120 -470  250 

# We see Thursday was the worst day, and Friday, the best.

# But let's sum the values according to the vectors, and not to the 
# days. To do that we use the sum() function.

sum(poker)
# [1] 230

sum(roulette)
# [1] -314

# To sum everything, we do two operations: 1) we add the vector values 
# together and 2) sum them.

sum(poker + roulette)
# [1] -84

# Ok. Let's check some statistics. We can call summary() to show mean, 
# median, max...

summary(poker)
#   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
#   -120     -50      20      46     140     240

summary(poker + roulette)
#   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
# -470.0  -100.0   116.0   -16.8   120.0   250.0