class Node:
 def __init__(self, cargo=None, next=None):
  self.cargo = cargo
  self.next = next
 def __str__(self):
  return str(self.cargo)

node = Node("test")
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

def print_list(node):
 while (not node==None):
  print(node, end = " ")
  node = node.next
 print()
node1.next = node2
node2.next = node3
print(node1.next)
print_list(node1)	
