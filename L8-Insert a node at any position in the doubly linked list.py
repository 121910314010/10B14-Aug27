# Insert a node at any position in the doubly linked list   
  
class Node:    
    def _init_(self,data):    
        self.data = data;    
        self.previous = None;    
        self.next = None;    
            
class InsertMid:    
    
    def _init_(self):    
        self.head = None;    
        self.tail = None;    
        self.size = 0;    
            
       
    def addNode(self, data):    
           
        newNode = Node(data);    
            
          
        if(self.head == None):    
               
            self.head = self.tail = newNode;    
             
            self.head.previous = None;    
               
            self.tail.next = None;    
        else:    
              
            self.tail.next = newNode;    
            
            newNode.previous = self.tail;    
               
            self.tail = newNode;    
                
            self.tail.next = None;    
          
        self.size = self.size + 1;    
            
  
    def addInMid(self, data):    
            
        newNode = Node(data);    
            
           
        if(self.head == None):    
               
            self.head = self.tail = newNode;    
               
            self.head.previous = None;    
              
            self.tail.next = None;    
        else:    
             
            current = self.head;    
                
            
            mid = (self.size//2) if(self.size % 2 == 0)  else ((self.size+1)//2);    
                
            
            for i in range(1, mid):    
                current = current.next;    
                    
            
            temp = current.next;    
            temp.previous = current;    
                
            
            current.next = newNode;    
            newNode.previous = current;    
            newNode.next = temp;    
            temp.previous = newNode;    
        self.size = self.size + 1;    
                
     
    def display(self):    
          
        current = self.head;    
        if(self.head == None):    
            print("List is empty");    
            return;    
        while(current != None):    
                
            print(current.data),    
            current = current.next;    
                
        print();    
            
dList = InsertMid();    
    
dList.addNode(15);    
dList.addNode(16);    
     
print("Original list: ");    
dList.display();    
     
 
dList.addInMid(85);    
print( "Updated List: ");    
dList.display();    
     
  
dList.addInMid(25);    
print("Updated List: ");    
dList.display();    
     

dList.addInMid(31);    
print("Updated List: ");    
dList.display();
