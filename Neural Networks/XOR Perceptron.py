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

    def fire(self, inputvalues, layer):

        fire = 0

        # layers_list = list()

        print "\n inputs: ", inputvalues

        print "\n layer: ", layer

        input_counts = len(inputvalues)

        print "\n input counts : ", input_counts

        layers_count = len(layer)

        print "\n layers count: ", layers_count

        if type(layer[0]) is int:
            nodes_count = 1

            layers_list = layer

        else:
            nodes_count = len(layer[0])

            print "\n nodes count: " , nodes_count

            layers_list = list()

            for node_count in range(nodes_count):
                nodes_list = list()

                for nodes in layer:
                    # print nodes[node_count]

                    nodes_list.append(nodes[node_count])

                # print "\n nodes list \n"

                # print nodes_list

                layers_list.append(nodes_list)

        print "\n layer list: ", layers_list

        layer_list_count = len(layers_list)

        layer_list_cnt = 0

        print "\n layers list count:  ", layer_list_count

        layer_nodes = list()

        for input_value in range(input_counts):

            self.weights = layers_list[layer_list_cnt]

            print "\n input ", inputvalues[input_value]

            print "\n weights: ", self.weights

            # layer_nodes =list()

            if layer_list_cnt < layer_list_count:
                actv = self.activate(inputvalues[input_value])

                print "\n activation: ", actv

                layer_nodes.append(actv[0])

                fire = fire + actv[1]

                layer_list_cnt += 1

                print "\n layer_list_cnt: ", layer_list_cnt
            else:
                print "\n next layer nodes: ", layer_nodes, "\n percep : ", fire

                return [layer_nodes, fire]

                break

        print "\n node activations: ", layer_nodes, "\n percep : ", fire

        return [layer_nodes, fire]

    def OR_gate(node_activations):
        """
        OR Gate Threshold Selection: lesser of the two nodes

        Threshold : Lesser Node - 1
        """
        if node_activation[0][0] < node_activation[0][1]:

            return node_activation[0][0] - 1

        else:
            return node_activation[0][1] - 1

    def AND_gate(node_activations):
        """
        OR Gate Threshold Selection: lesser of the two nodes

        Threshold : (Greater Node + Lesser Node) - 1
        """
        return ((node_activation[0][0] + node_activation[0][1]) - 1)


# Part 1: Set up the perceptron network
Network = [
    # input layer, declare input layer perceptrons here
    [[3, 2], [4, 5], [2, 5]], \
    # output node, declare output layer perceptron here
    [1, 1]
]


# Part 2: Define a procedure to compute the output of the network, given inputs


def EvalNetwork(inputValues, Network):
    """
    Takes in @param inputValues, a list of input values, and @param Network
    that specifies a perceptron network. @return the output of the Network for
    the given set of inputs.
    """

    # YOUR CODE HERE

    # OR Gate:

    # fire = fire()

    or_gate = list()

    and_gate = list()

    perceptron_list = list()

    print "\n\n input values: ", inputValues

    print "\n network: ", Network

    print "\n Enters fire()  "

    # for Layer in Network:
    print "\n perceptron - fire: \n",

    for layer in Network:
        print layer

    for layer in Network:
        print "\n fire layer: ", layer
        perceptron = (
            Perceptron(weights=1, threshold=1).fire(inputvalues=inputValues, layer=layer))

        inputvalues = perceptron[0]

        print"\n perceptron - fire: ", perceptron

        perceptron_list.append(perceptron)

        print "\n perceptron_list: ", perceptron_list

    print "\n end"

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