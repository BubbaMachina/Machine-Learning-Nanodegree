# ----------
#
# In this exercise, you will create a network of perceptrons that can represent
# the XOR function, using a network structure like those shown in the previous
# quizzes.
#
# You will need to do two things:
# First, create a network of perceptrons with the correct weights
# Second, define a procedure EvalNetwork() which takes in a list of inputs and
# outputs the value of this network.
#
# ----------

import numpy as np


class Perceptron:
    """
    This class models an artificial neuron with step activation function.
    """

    def __init__(self, weights=np.array([1]), threshold=0):
        """
        Initialize weights and threshold based on input arguments. Note that no
        type-checking is being performed here for simplicity.
        """
        self.weights = weights
        self.threshold = threshold

    def activate(self, values):
        """
        Takes in @param values, a list of numbers equal to length of weights.
        @return the output of a threshold perceptron with given inputs based on
        perceptron weights and threshold.
        """

        # First calculate the strength with which the perceptron fires
        strength = np.dot(values, self.weights)

        # Then return 0 or 1 depending on strength compared to threshold
        print "\n strenght: ", strength, " ---> ", np.sum(strength)

        print "\n threshold ", self.threshold,

        print "\n\n perceptron fire..."

        if (sum(strength) > self.threshold):

            # print [np.sum(strength), 1]

            return [np.sum(strength), 1]

        else:
            # print [np.sum(strength), 0]

            return [np.sum(strength), 0]

    def single_node_activation(self, inputvalues, layer):
        print "single node activation"

    def multiple_node_activation(self, inputvalues, layer):
        """
        processing activation when there are more than one nodes in the network.
        If there is only one node in the layer, it will route it to single_node_activation
        :param inputvalues:
        :param layer:
        :return:
        """

        # checking the number of nodes in a layer
        print layer

        print inputvalues

        for nodes in layer:
            if type(nodes) is not list:
                return self.single_node_activation(inputvalues,layer)

            else:







# Part 1: Set up the perceptron network
Network = [
    # input layer, declare input layer perceptrons here
    [[3, 2], [4, 5], [2, 5]], \
    # output node, declare output layer perceptron here
    [1, 1]
]


def EvalNetwork(inputValues, Network):
    """
    Takes in @param inputValues, a list of input values, and @param Network
    that specifies a perceptron network. @return the output of the Network for
    the given set of inputs.
    """

    # YOUR CODE HERE

    # 1. computing the activations of the networks:
    for layer in Network:

        Perceptron(weights= 1,threshold= 1).multiple_node_activation(inputvalues= inputValues, layer= layer)


    # Be sure your output value is a single number
    # return OutputValue


def test():
    """
    A few tests to make sure that the perceptron class performs as expected.
    """
    print "0 XOR 0 = 0?:", EvalNetwork(np.array([0, 0]), Network)
    print "0 XOR 1 = 1?:", EvalNetwork(np.array([0, 1]), Network)
    print "1 XOR 0 = 1?:", EvalNetwork(np.array([1, 0]), Network)
    print "1 XOR 1 = 0?:", EvalNetwork(np.array([1, 1]), Network)


if __name__ == "__main__":
    test()