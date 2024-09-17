'''
In solving a linked list, your first have to declare a class
that sets the head/current-node and the next intended node
'''

class node:
    def __init__(self, data=None):
        self.data = data #this is the current node data (where we are).
        self.next = None #this is the next node.

'''
Then you create your linked_list class.
This class  would define the function of;
1. what the head node will be
2. Adding newly found nodes to the linked_list
3. Finding the lenght 
'''
class linked_list:
    def __init__(self):
        self.head = node() #head node will not be indexable. it is just a standing point to help us get to the next node.

# '''
# in the append function, we would be creating arg=self and kwarg to be the data we want to work with.
# variables in the append function would include, a new_node newly taken data or first indices,
# current node, which will be the starting point self.head or if there exists a next node, the next node becomes current node
# '''

    def append(self, data):
        new_node = node(data) #newly taken in data
        cur = self.head #define the head as current/first position.
        while cur != None: #if there exists a next node after the head node, use a while loop to traverse through
            cur = cur.next #if you find the next node, make it the current node
