The term Deep Learning refers to training Neural Networks, sometimes very large Neural Networks. So what exactly is a Neural Network?

Let's start to the Housing Price Prediction example:

> You have a data set with six houses, and you know the size and the price of the houses. You want to fit a function to predict the price of other houses based on their sizes.

![01](https://github.com/rodolfo-viana/dailylog/blob/master/estudos/deep_learning/01_neural_networks%2Bdeep_learning/src/01.png)

If you are familiar with linear regression you might say, "well, let's put a straight line to these data" and we get a straight line.

![02](https://github.com/rodolfo-viana/dailylog/blob/master/estudos/deep_learning/01_neural_networks%2Bdeep_learning/src/02.png)

We know that prices can never be negative, right? So instead of the straight line fit which eventually will become negative, let's bend the line.

![03](https://github.com/rodolfo-viana/dailylog/blob/master/estudos/deep_learning/01_neural_networks%2Bdeep_learning/src/03.png)

So **this blue line ends up being your function for predicting the price of the house, whereas zero here and then there's a straight line fit to the right**. So you can think of this function that you've just fit the housing prices as a very simple neural network.

It's almost as simple as possible neural network. Let me draw it here:

![04](https://github.com/rodolfo-viana/dailylog/blob/master/estudos/deep_learning/01_neural_networks%2Bdeep_learning/src/04.png)

We have as the input to the neural network the size of a house which one we call x. It goes into a node -- the little circle -- and then outputs the price which we call y. The node, which is a **single neuron** in a neural network, implements this function that we drew earlier. And all the neuron does is:

1. it inputs the size,
2. computes this linear function,
3. takes a max of zero,
4. outputs the estimated price.

In the neural network literature, you see this function a lot -- this function which goes to zero sometimes and then it'll takes of as a straight line. It is called a **ReLU function, which stands for rectified linear units**. Rectify just means taking a max of zero which is why you get a function shape like this.

So if this is a single neuron, and it is really a tiny little neural network, a larger neural network is then formed by taking many of the single neurons and stacking them together. If you think of this neuron that's being like a single Lego brick, you then get a bigger neural network by stacking together many of these Lego bricks. Let's see an example:

> Instead of predicting the price of a house just from the size, you now have other features: number of bedrooms, por instance. So one of the things that really affects the price of a house is family size. Another feature is the zip code, which tells us about walkability. Another one is the neighborhood wealth...

![05](https://github.com/rodolfo-viana/dailylog/blob/master/estudos/deep_learning/01_neural_networks%2Bdeep_learning/src/05.png)

Each of these little circles can be one of those ReLU, rectified linear units or some other slightly non linear function. In the example, x is all of these inputs, and y is the price you're trying to predict.

By stacking together a few of the single neurons or the simple predictors we have from the previous slide, we now have a slightly larger neural network.

How you manage neural network is that when you implement it, you need to give it just the input x and the output y for a number of examples in your training set and all this things in the middle, they will figure out by itself.

So what you actually implement is this:

![06](https://github.com/rodolfo-viana/dailylog/blob/master/estudos/deep_learning/01_neural_networks%2Bdeep_learning/src/06.png)

Here, you have a neural network with four inputs. The input features might be the size, number of bedrooms, the zip code, and the wealth of the neighborhood. Given these input features, the job of the neural network
will be to predict the price y.

The circles are called **hidden units** in the neural network, and each of them takes its inputs all four input features.

Rather than saying the first nodes represent family size and family size depends only on the features x1 and x2, we're going to say "well, neural network, you decide whatever you want this known to be, and we'll give you all four of the features to complete whatever you want".

So the input layer is connected to the layers in the middle of the neural network. Every input feature is connected to every one of these circles in the middle: the hidden units.

And the remarkable thing about neural networks is that, given enough data about x and y, given enough training examples with both x and y, neural networks are remarkably good at figuring out functions that accurately map from x to y.

So, that's a basic neural network.
