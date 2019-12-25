# Handwritten Digit Predictor(MNIST Dataset)
Simple neural network to predict handwritten digits using Tensorflow and famous MNIST dataset


## What is a Neural Network ? 

A neural network (also called an ANN or an artificial neural network) is a sort of computer software, inspired by biological neurons. Biological brains are capable of solving difficult problems, but each neuron is only responsible for solving a very small part of the problem. Similarly, a neural network is made up of cells that work together to produce a desired result, although each individual cell is only responsible for solving a small part of the problem. This is one method for creating artificially intelligent programs.

From [Wikipedia](https://simple.wikipedia.org/wiki/Artificial_neural_network)

---

## The MNIST Dataset 

The [**MNIST database**](https://en.wikipedia.org/wiki/MNIST_database) is arguably the most famous database in the field of machine learning; it is a large database of **28**x**28** pixel images of handwritten digits created in 1999 by [Yann LeCun](http://yann.lecun.com/).

---

## The Model

Our model consists of 6 layers:

1. Input (**28**x**28** pixel image)
2. Dense(Relu activation)
3. Dropout (0.2)
4. Dense(Relu activation
5. Dropout (0.4)
6. Dense (Softmax activation)



## Draw and classify digits in Playground Canvas

[**Run draw and Predict **](https://github.com/sandeep021/Handwritten-digit-predictor-using-MNIST-data-set) on your Machine.
---

## Creating and Training The Model
Steps:

1. The data was preprocessed using keras and dataset api of Tensorflow. 
2. The model was created and trained using tensorflow 2.0.
3. The adam optimizer is used to reduce the cost.

Run the [Jupyter notebook](https://github.com/sandeep021/Handwritten-digit-predictor-using-MNIST-data-set/blob/master/Model_predictor.ipynb) to train the network on your own device

---

## Demo Video 
[demo](https://youtu.be/qGH3o8N4AYg)

## Contributing
Your feedback is always appreciated and welcomed. If you find a bug in the source code, you can help me by submitting an issue. Even better you can submit a Pull Request with a fix :)

---

## License

This project is released under the [MIT License](LICENSE)
