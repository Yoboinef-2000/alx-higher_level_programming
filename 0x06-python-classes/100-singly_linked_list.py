#!/usr/bin/python3

class Node:
    """
    This class defines a node of a singly linked list.
    
    Attributes:
    - __data (int): Private instance attribute representing the data of the node.
    - __next_node (Node): Private instance attribute representing the next node in the linked list.
    """

    def __init__(self, data, next_node=None):
        """
        Initialize a new instance of the Node class.

        Parameters:
        - data (int): Data of the node.
        - next_node (Node): Next node in the linked list. Defaults to None.

        Raises:
        - TypeError: If data is not an integer or next_node is not a Node object.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter for the data attribute."""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter for the data attribute."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter for the next_node attribute."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter for the next_node attribute."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    This class defines a singly linked list.

    Attributes:
    - head: Private instance attribute representing the head of the linked list.
    """

    def __init__(self):
        """Initialize an empty singly linked list."""
        self.head = None

    def sorted_insert(self, value):
        """
        Insert a new Node into the correct sorted position in the list (increasing order).

        Parameters:
        - value (int): Value to be inserted.
        """
        new_node = Node(value)

        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node

            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Print the entire list in stdout, one node number by line."""
        result = ""
        current = self.head
        while current:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.strip()
