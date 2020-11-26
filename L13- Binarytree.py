class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data


    def DispTree(self):
        print(self.data)

root = Node(15)

root.DispTree()

Output:-
15
