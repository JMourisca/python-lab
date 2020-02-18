#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep):
    while node:
        print(node.data, end='')

        node = node.next

        if node:
            print(sep, end='')

# Complete the reversePrint function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def getNode(head, positionFromTail):
    # values = []
    node = head
    result = head

    i = 0
    while node:
        # values.append(node.data)
        if i + 1 > positionFromTail:
            result = node        
        node = node.next
        i += 1
    
    return result.data # values[-1 * (positionFromTail+1)]


if __name__ == '__main__':
    input1 = [1, 2, 3, 4, 5]

    position = 1
    llist = SinglyLinkedList()

    for data in input1:
        llist.insert_node(data)


    result = getNode(llist.head, position)

    print(result)