class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.numOfNodes = 0

    def insert_start(self, data):
        self.numOfNodes += 1
        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            new_node.nextNode = self.head
            self.head = new_node

    def insert_end(self, data):
        self.numOfNodes += 1
        new_node = Node(data)
        actual_node = self.head
        while actual_node.nextNode is not None:
            actual_node = actual_node.nextNode

        actual_node.nextNode = new_node

    def remove(self, data):
        if self.head is None:
            return

        actual_node = self.head
        previousNode = None

        while actual_node is not None and actual_node.data != data:
            previousNode = actual_node
            actual_node = actual_node.nextNode

        if actual_node is None:
            return
        self.numOfNodes -= 1
        if previousNode is None:
            self.head = actual_node.nextNode
        else:
            previousNode.nextNode = actual_node.nextNode

    def size_of_LinkedList(self):
        return self.numOfNodes

    def traverse(self):
        actual_node = self.head

        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.nextNode

    def get_middle_node(self):

        fast_pointer = self.head
        slow_pointer = self.head

        while fast_pointer.nextNode and fast_pointer.nextNode.nextNode:
            fast_pointer = fast_pointer.nextNode.nextNode
            slow_pointer = slow_pointer.nextNode

        return slow_pointer


ll = LinkedList()
ll.insert_start(4)
ll.insert_start(3)
ll.insert_start(7)
ll.insert_end(10)
ll.insert_end(120)
ll.insert_end(122)
# ll.traverse()
# ll.remove(10)
ll.traverse()
print(ll.get_middle_node().data)
