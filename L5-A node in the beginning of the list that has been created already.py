class Node:
    def _init_(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def _init_(self):
        self.head = None
    def AppendNode(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        k=self.head
        while k.next!=None:
            k=k.next
        k.next=new_node
    def addAtStart(self,data):    
        new_Node = Node(data)   
        if self.head.data == None:      
            self.head = newNode  
            new_Node.next = self.head   
        else:      
            temp = self.head    
            new_Node.next = temp    
            self.head = new_Node        
    def PrintList( self ):
        node = self.head
        while node != None:
            print (node.data)
            node = node.next
list = LinkedList()
list.AppendNode(1)
q=input().strip().split()
for i in q:
    list.addAtStart(i)
list.PrintList()

Output:-
1 2 3 4
4
3
2
1
1
