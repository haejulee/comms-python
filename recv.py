from Node import Node
import numpy as np

node = Node("recv.json")

while True:
    ar = node.recv("array-in")
    print(ar)
