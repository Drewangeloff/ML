import random
import matplotlib.pyplot as plt

def generate_semi_random_data_for_classification2():
    mydata = []
    for n in range(0, 1000):
        mydata.append([random.uniform(0.5,1), random.uniform(0.5,1), 0])
    for n in range(0, 1000):
        mydata.append([random.uniform(-0.5,-1), random.uniform(-0.5,-1), 1])

    random.shuffle(mydata)
    return (mydata)



# ---------------------------------------------------------------------------#

class PerceptronNode:
    def __init__(self):
        self.weight = random.uniform(-0.01, 0.01)

def create_layer(breadth):
    layer = []
    for i in range(0, breadth):
        layer.append(PerceptronNode())
    return layer

def activationfunction(input):
    if input < 0:
        output = 0
    else:
        output = 1
    return output



# create layer
#   node 1 x
#   node 2 y
#   node 3 bias
layer = create_layer(3)
layer[2].weight = 1

# generate inputs
inputmatrix = generate_semi_random_data_for_classification2()

# main training loop.  We will try to categorize on color
epoch = 0
error = 0
old_x = 0
old_y = 0
#MAIN LOOP  - goes through input values and trains on those values.

for i in inputmatrix:
    epoch += 1
    if (epoch % 100 == 0):
        print (epoch)
        plt.pause(0.05)
    #print ("----------------")
    #print("putting " + str(i) + " into the inputs")

    #put in inputs into function to determine activation

    ix = i[0]
    iy = i[1]

    wx = layer[0].weight
    wy = layer[1].weight
    wb = layer[2].weight #bias

    output = activationfunction((wx * ix) + (wy * iy) + wb)
    """
    print("predicted output:" + str(output))
    print("desired output:" + str(activationfunction(iy + ix + wb)))
    """
    if (output != activationfunction(iy + ix + wb)):
        error += 1
        #print ("error:" + str(error))


    learnrate = 0.01
    #error / ix will give us the slope delta we want to update the weights with
    """
    print("Weight before update:" + str(layer[0].weight))
    print("Weight before update:" + str(layer[1].weight))
    """
    layer[0].weight += (ix - output) * ix * learnrate
    layer[1].weight += (iy - output) * iy * learnrate
    """
    print("Weight after update:" + str(layer[0].weight))
    print("Weight after update:" + str(layer[1].weight))
    """
    #visualize
    if i[2] == 0:
        color = 'c'
    if i[2] == 1:
        color = 'r'
    #plot points
    #plt.scatter(i[0], i[1], s=5, c=color)
    #plt.text(i[0], i[1], str(output))
    #plt.scatter(epoch,error,s=5,c='g')
    plt.scatter(epoch,layer[0].weight,s=5,c='r')
    plt.scatter(epoch, layer[1].weight, s=5, c='b')
    #plt.scatter(epoch, error, s=5, c='g')
    #plt.pause(0.05)

plt.show()



