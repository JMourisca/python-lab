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
def mergeLists(head1, head2):
    node1 = head1
    node2 = head2
    nlist = SinglyLinkedList()
    same = True
    while node1 or node2:
        if node1 and node2:
            if node1.data <= node2.data:
                nlist.insert_node(node1.data)        
                node1 = node1.next
            else:
                nlist.insert_node(node2.data)
                node2 = node2.next
        else:
            if node1 and not node2:
                nlist.insert_node(node1.data)        
                node1 = node1.next
            else:
                nlist.insert_node(node2.data)
                node2 = node2.next
        
    return nlist.head


if __name__ == '__main__':
    input1 = [1, 2, 3]
    input2 = [3, 4]

    test_idx = 0
    llist = SinglyLinkedList()
    llist2 = SinglyLinkedList()
    for data in input1:
        llist.insert_node(data)

    for data in input2:
        llist2.insert_node(data)

    llist3 = mergeLists(llist.head, llist2.head)

    print_singly_linked_list(llist3, ' ')