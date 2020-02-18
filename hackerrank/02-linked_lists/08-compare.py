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
def compare_lists(llist1, llist2):
    node1 = llist1
    node2 = llist2
    same = True
    while node1 or node2:
        if node1 and node2:
            same = same and (node1.data == node2.data)
        elif (node1 and not node2) or (node2 and not node1):
            return False
            
        node1 = node1.next
        node2 = node2.next
        
    return same


if __name__ == '__main__':
    input1 = [16,12,4,2,5]
    input2 = [16,12,4,2,5]

    test_idx = 0
    llist = SinglyLinkedList()
    llist2 = SinglyLinkedList()
    for data in input1:
        llist.insert_node(data)

    for data in input2:
        llist2.insert_node(data)

    print(compare_lists(llist.head, llist2.head))