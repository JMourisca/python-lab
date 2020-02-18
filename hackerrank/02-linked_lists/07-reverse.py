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
def reverse(head):
    def insertNodeAtHead(h, data):
        node = SinglyLinkedListNode(data)
        if h is None:
            h = node
        else:            
            node.next = h
        return node    

    invertedList = SinglyLinkedList()
    node = head
    while node:        
        head = insertNodeAtHead(invertedList.head, node.data)
        invertedList.head = head        
        node = node.next
    return invertedList.head

if __name__ == '__main__':
    input = [16,12,4,2,5]

    test_idx = 0
    llist = SinglyLinkedList()
    for data in input:
        llist.insert_node(data)

        # 

        # for _ in range(llist_count):
        #     llist_item = int(input())
        #     llist.insert_node(llist_item)

    llist1 = reverse(llist.head)
    print_singly_linked_list(llist1, ' ')
