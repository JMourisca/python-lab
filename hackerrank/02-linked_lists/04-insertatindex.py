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
        print(node.data)

        node = node.next

# Complete the insertNodeAtPosition function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtPosition(head, data, position):
    node = head
    index = 0
    newNode = SinglyLinkedListNode(data)
    if position == 0:
        newNode.next = head
        head = newNode
    else:
        while index < position - 1:
            node = node.next
            index += 1    
        if node == None:
            return head
        nextNode = node.next
        newNode.next = nextNode
        node.next = newNode
    return head

if __name__ == '__main__':
    input = [5,16,13,7, 3, 4, 10000, 5]

    llist_count = input[0]

    llist = SinglyLinkedList()

    for i in input[1:llist_count+1]:
        llist_item = i
        llist.insert_node(llist_item)

    data = input[llist_count+1]

    position = input[-1]

    llist_head = insertNodeAtPosition(llist.head, data, position)

    print_singly_linked_list(llist_head, ' ')

