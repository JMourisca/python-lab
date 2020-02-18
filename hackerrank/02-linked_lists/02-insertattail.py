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

def print_singly_linked_list(node, sep):
    while node:
        print(node.data)

        node = node.next

# Complete the insertNodeAtTail function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtTail(head, data):
    tail = SinglyLinkedListNode(data)
    if head is None:
        head = tail
    else:
        node = head
        while node.next is not None:
            node = node.next
        node.next = tail    
    return head

if __name__ == '__main__':

    data = [43, 23, 54, 78, 12, 3, 5]
    llist = SinglyLinkedList()

    for i in data:
        llist_item = i
        llist_head = insertNodeAtTail(llist.head, llist_item)
        llist.head = llist_head

    print_singly_linked_list(llist.head, '\n')

