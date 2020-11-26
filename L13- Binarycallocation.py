class node:
    def __init__(self,data=None):
        self.data=data
        self.left_node=None
        self.right_node=None
class BinaryTree:
    def __init__(self):
        self.root=None

    def inorder(self):
        if(self.root==None):
            print("Tree is Empty.....")
        else:
            self.__inorder(self.root)

    def __inorder(self,current):
        if current:
            print(current.data, end="")
            self.__inorder(current.left_node)
            self.__inorder(current.right_node)


ob1=BinaryTree()
a=int(input("enter the nodes"))
b=int(input())
c=int(input())
d=int(input())
e=int(input())
f=int(input())
g=int(input())
h=int(input())
i=int(input())
j=int(input())
k=int(input())
l=int(input())

first=node(a)
second=node(b)
third=node(c)
forth=node(d)
fifth=node(e)
sixth=node(f)
seventh=node(g)
eight=node(h)
ninth=node(i)
tenth=node(j)
eleventh=node(k)
twelth=node(l)
ob1.root=first
first.left_node=second
first.right_node=third
second.left_node=forth
second.right_node=fifth
third.left_node=sixth
third.right_node=seventh
forth.left_node=eight
forth.right_node=ninth
fifth.left_node=tenth
fifth.right_node=eleventh
print("inorder is",end=" ")
ob1.inorder()

Output:-
enter the nodes12
1
2
3
4
5
6
7
8
9
10
11
inorder is 1213784910256
