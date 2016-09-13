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

        print "\n +++++++++++ Entering activate ++++++++++++++++\n"

        print "\n values: " , values

        print "\n weights: ", self.weights

        print "\n strenght: ", strength, " ---> ", np.sum(strength)

        print "\n threshold ", self.threshold,

        print "\n\n perceptron fire..."

        if (sum(strength) > self.threshold):

            # print [np.sum(strength), 1]

            print "\n ++++++++++ Exiting Activate ++++++++++++++++++\n"

            return [np.sum(strength), 1]

        else:
            # print [np.sum(strength), 0]

            print "\n ++++++++++ Exiting Activate ++++++++++++++++++\n"

            return [np.sum(strength), 0]

    def single_node_activation(self, inputvalues, layer):
        print "\n^^^^^^^^Entering single node activation^^^^^^^^^^^^^^^\n"

        print "\n input nodes: ", inputvalues

        print "\n weights: ", layer

        self.weights = layer

        print "\n -------------- computing strength and activation of perceptron ------------------\n"

        print self.activate(inputvalues)

        print "\n -------------- End of computing strength and activation of perceptron ------------------\n"

        print "\n^^^^^^^^^^^^Exiting single node activation^^^^^^^^^^^^^^^\n"

        return None

    def multiple_node_activation(self, inputvalues, layer):
        """
        processing activation when there are more than one nodes in the network.
        If there is only one node in the layer, it will route it to single_node_activation
        :param inputvalues:
        :param layer:
        :return:
        """

        print "\n *********Entering multiple nodes activation *********** \n"

        # checking the number of nodes in a layer
        print layer

        print inputvalues

        for nodes in layer:
            if type(nodes) is not list:
                print "\n**********Exiting multiple nodes activation**********\n "

                return self.single_node_activation(inputvalues,layer)

            else:

                print "\n---------------------number of items in the input parameters------------------ "

                print "\n inputs: ", inputvalues

                print "\n layer: ", layer

                print "\n nodes: ", nodes

                input_counts = len(inputvalues)

                print "\n number of inputs: ", input_counts

                layers_count = len(layer)

                print "\n number of layers: ", layers_count

                nodes_count = len(layer[0])

                print "\n nodes in each layer: ", nodes_count

                print "\n -----------------End of number of items in the argument--------------------"

                break

        print "\n -----------------Seperating weight nodes for computation-----------------------\n"

        weights_list = list()

        for node_count in range(nodes_count):
            nodes_list = list()

            for nodes in layer:
                #print nodes[node_count]

                nodes_list.append(nodes[node_count])

            print "\n weights of the nodes: ", nodes_list

            weights_list.append(nodes_list)

        print "\n weights in the layer: ", weights_list

        weights_list_count = len(weights_list)

        print "\n number of weight nodes in the layer: ", weights_list_count

        print "\n ----------------End of seperation of weight nodes for activation ------------------\n"

        print "\n----------------Iterating and computing activation------------------------------------\n"

        wgt_lst_cnt = 0

        fire = 0

        layer_strengths = list()

        for input_count in range(input_counts):

            #updating weights one by one
            self.weights = weights_list[wgt_lst_cnt]

            print "\n current input value of X: ", inputvalues[input_count]

            print "\n current weight in the node, W: ", self.weights

            if wgt_lst_cnt < weights_list_count:
                actv = self.activate(inputvalues[input_count])

                print "\n activation [strength, perceptron activation]: ", actv

                layer_strengths.append(actv[0])

                fire = fire + actv[1]

                print "\n current count of the weight layer: ", wgt_lst_cnt

                wgt_lst_cnt += 1

        print "\n strengths: ", layer_strengths, "\n perceptron activation : ", fire

        print "\n----------------Exiting iteration and computing activation------------------------------------\n"

        return [layer_strengths, fire]












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

        perceptron = (
            Perceptron(weights= 1,threshold= 1).multiple_node_activation(inputvalues= inputValues, layer= layer))

        print perceptron

        if perceptron != None:

            inputValues = perceptron[0]

            print "\n <><><><<><><> Moving to the next layer <><><><><><><><><> \n "

            print "\n next input : ", inputValues

            #print "\n previous layer: ", layer

            print "\n <><><><><><><> Entering the next layer of the neaural network <><><><><><><><> \n "





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