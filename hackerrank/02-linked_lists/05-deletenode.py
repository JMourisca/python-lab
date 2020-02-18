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

# Complete the deleteNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def deleteNode(head, position):
    if position < 0:
        return head

    node = head
    if position == 0:
        newHead = node.next
        node.next = None
        return newHead

    index = 0
    while index < position:
        prev = node
        if node.next is None:
            return head
        node = node.next        
        index += 1
    
    newNext = None
    if node.next is not None:
        newNext = node.next

    prev.next = newNext
    node.next = None
    
    return head

if __name__ == '__main__':
    input = [8,20,6,2,19,7,4,15,9,-7]

    llist_count = input[0]

    llist = SinglyLinkedList()

    for i in input[1:llist_count+1]:
        llist_item = i
        llist.insert_node(llist_item)

    position = input[-1]

    llist1 = deleteNode(llist.head, position)

    print_singly_linked_list(llist1, ' ')
