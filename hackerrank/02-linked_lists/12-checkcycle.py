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
def has_cycle(head):
    cycle = False
    check = {}
    while head and not cycle:
        if head not in check.keys():
            check[head] = True
        else:
            cycle = True
        head = head.next
    return cycle

if __name__ == '__main__':

    llist = SinglyLinkedList()

    head = SinglyLinkedListNode(1)
    node2 = SinglyLinkedListNode(2)
    node3 = SinglyLinkedListNode(3)

    head.next = node2
    node2.next = node3
    node3.next = node2

    print(has_cycle(head))

    llist = SinglyLinkedList()

    head = SinglyLinkedListNode(1)
    node2 = SinglyLinkedListNode(2)
    node3 = SinglyLinkedListNode(3)

    head.next = node2
    node2.next = node3
    print(has_cycle(head))

    