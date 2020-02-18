#!/bin/python3

import math
import os
import random
import re
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node, sep):
    while node:
        print(node.data)
        node = node.next

# Complete the sortedInsert function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def reverse(head):
    newDL = DoublyLinkedList()    

    node = head
    while node:
        newNode = DoublyLinkedListNode(node.data)        

        # if newDl doesn't have a head, newNode needs to be the head
        if newDL.head is None:
            newDL.head = newNode
        else: # if it has a head, the new node will become the previous node and the head will be the next
            newNode.next = newDL.head
            newDL.head.prev = newNode
            newDL.head = newNode

        node = node.next  

    return newDL.head


if __name__ == '__main__':

    llist = DoublyLinkedList()

    inputarr = [5, 4, 3, 2, 1]

    for i in inputarr:
        llist.insert_node(i)

    llist1 = reverse(llist.head)

    print_doubly_linked_list(llist1, ' ')
