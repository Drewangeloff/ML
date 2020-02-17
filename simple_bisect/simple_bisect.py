
import matplotlib.pyplot as plt

traindata = [[.2,.2,0],[.5,.5,1]]

class neuron():
    def __init__(self):
        self.weight = .25

node = neuron()

print (node)
print (node.weight)

#main loop
for i in range(0,2):
    print("epoch " + str(i))
    y = (node.weight * traindata[i][0])
    print("node weight " + str(node.weight))
    print("prediction for y is " + str(y))
    print("desired output for y is " +str(traindata[i][1]))

    error = traindata[i][1] - y
    delta = error / traindata[i][0]

    node.weight = delta * 0.1

    print("error " + str(error))
    print("delta " + str(delta))
    print("updated node " + str(node.weight))

    #visualize
    y = (node.weight *traindata[i][0])
    x = traindata[i][1]/node.weight

    plt.plot([0,x],[0,y])
    plt.scatter(traindata[0][0],traindata[0][1],s=5)
    plt.scatter(traindata[1][0],traindata[1][1],s=5)
    plt.pause(0.05)
plt.show()
