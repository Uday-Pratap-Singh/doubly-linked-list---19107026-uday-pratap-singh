class Node:
  def __init__(self, data):
    self.data = data 
    self.next = None 
    self.prev = None 



class DoublyLinkedList:
  def __init__(self):
    self.head = None 
    self.tail = None
  

  def push_front(self, new_data):
    new_node = Node(new_data)
    new_node.next = self.head

    if self.head != None: 
        self.head.prev = new_node
        self.head = new_node 
        new_node.prev = None
    
    else: 
      self.head = new_node
      self.tail = new_node
      new_node.prev = None 
    

  def push_back(self, new_data): 
      new_node = Node(new_data)
      new_node.prev = self.tail

      if self.tail == None: 
        self.head = new_node 
        self.tail = new_node
        new_node.next = None 
              
      else: 
        self.tail.next = new_node
        new_node.next = None
        self.tail = new_node 
  
  def delete(self,value):
    dele = self.head
    while(dele!=None):
      if(dele.data==value):
        break;
      dele = dele.next;
    if(dele==None):
      print("Node not found");
      return
    if self.head is None or dele is None:
            return
    if self.head == dele:
            self.head = dele.next
    if dele.next is not None:
            dele.next.prev = dele.prev
    if dele.prev is not None:
            dele.prev.next = dele.next

  def display(self):
    current = self.head;
    while(current!=None):
      print(current.data);
      current = current.next


n = int(input("Enter no of elements in Doubly Linked List"))
DLL = DoublyLinkedList()
while n:
  data = int(input("Enter number to insert"))
  DLL.push_back(data)
  n = n-1;
value = int(input("Enter number to delete"))
DLL.delete(value)
DLL.display()