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
def sortedInsert(head, data):
    def insertBetweebCurrAndNext(data, current, next):
        newNode = DoublyLinkedListNode(data)
        newNode.next = next
        next.prev = newNode
        newNode.prev = current
        current.next = newNode
        return head         

    node = head
    last = head

    if data <= head.data:
        newNode = DoublyLinkedListNode(data)
        newNode.next = head
        return newNode
    
    while node:
        current = node
        next = node.next
        if current and next and data >= current.data and data <= next.data:            
            return insertBetweebCurrAndNext(data, current, next)
        
        if not next:
            newNode = DoublyLinkedListNode(data)
            node.next = newNode
            newNode.prev = current
            return head

        node = node.next
            
    return head

if __name__ == '__main__':

    llist = DoublyLinkedList()

    inputarr = []

    for i in inputarr:
        llist_item = i
        llist.insert_node(llist_item)

    data = 0

    llist1 = sortedInsert(llist.head, data)

    print_doubly_linked_list(llist1, ' ')
