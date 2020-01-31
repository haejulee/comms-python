from Node import Node
import numpy as np


node = Node("send.json")

a = np.array([[10,10,39],[20,30,40]])
while True:
    node.send("array-out", a)

