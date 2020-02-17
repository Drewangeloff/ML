import numpy as np
import matplotlib.pyplot as plt
import random
import scipy.special



class node():
    def __init__(self):
        activation = 0.001

class NN():

    def activation_function(self,input):
        output = scipy.special.expit(input)
        return output

    def __init__(self, inputnodes, hiddennodes, outputnodes, learnrate):
        self.learn_rate = learnrate

        #number of nodes
        self.number_of_layer1_nodes = inputnodes
        self.number_of_layer2_nodes = hiddennodes
        self.number_of_layer3_nodes = outputnodes

        #init weight arrays
        self.weights_ih = np.random.rand (self.number_of_layer2_nodes, self.number_of_layer1_nodes) - 0.5
        self.weights_oh = np.random.rand(self.number_of_layer3_nodes, self.number_of_layer2_nodes) - 0.5

    def calc(self):
        # calculate signals into hidden layer
        layer2_inputs = numpy.dot(self.weights_ih, inputs)  
        #calculate the signals emerging from hidden layer  
        layer2_outputs = self.activation_function(layer2_inputs)  
        
        #calculate signals into final output layer  
        layer3_outputs = numpy.dot(self.who, hidden_outputs)  
        #calculate the signals emerging from final output layer 
        final_outputs = self.activation_function(layer3_outputs) 

    def trainNN():
        pass

    def queryNN():
        pass


#inits
debug = False

#create NN
myNN = NN(3,3,3,0.1)



#debug goop
if debug == True:
    #weights
    plt.figure()
    plt.imshow(myNN.weights_ih, interpolation="nearest")
    plt.figure()
    plt.imshow(myNN.weights_oh, interpolation="nearest")
    plt.show()


print (myNN.activation_function())