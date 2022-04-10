from logging import error
from msilib.schema import Error
from typing import List, Optional, Any, Dict
from Heap import Heap

def int_input()-> int:
    '''used for integer input'''
    return(int(input()))

def list_input( seperator: str = ' ')-> List:
    '''used for list input in a line seperated by seperator'''
    return input().split(seperator)

def int_list_input(seperator: str = ' ') -> List[int]:
    '''Used to get integer list in a line'''
    return list( map(int, list_input(seperator)))

def item_counter(items: List[Any]) -> Dict:
    '''
    used to get the frequency of all the item in a list
    '''
    item_count = {}

    for item in items:
        if item not in item_count:
            item_count[item] = 1
        else:
            item_count[item] += 1
    return item_count

class priority_queue(Heap):
    '''
    This is an implementation of max priority queue.
    Using the implementation of max heap as parent class.
    '''
    def __init__(self, array: List[int]) -> None:
        super().__init__(array)
    
    def maximum(self):
        if self.size > 0:
            return self.array[0]
        else:
            raise error("Heap underflow")
    
    def extract_maximum(self):

        if self.size > 0:
            maximum = self.array[0]
            self.swap(0, self.size - 1 )
            self.size -= 1
            self.max_heapify(self.size - 1)
            return maximum
        else:
            raise Error("Heap underflow")
    
    def heap_increase_key(self, index, key):

        if self.size == 0:
            raise Error("Heap underflow")
        if index >= self.size:
            raise IndexError
        if self.array[index] > key:
            raise Error("Key is smaller than the current key")
        
        while index > 0 and self.array[self.parent(index)] > key:
            self.array[index] = self.array[self.parent(index)]
            index = self.parent(index)

        self.array[index] = key
    
    def max_heap_insert(self, key):
        if self.length == self.size:
            self.array.append(0)
            self.length += 1
        
        self.size += 1
        self.array[self.size - 1] = float('-inf')

        self.heap_increase_key(self.size-1, key)

if __name__ == "__main__":
    '''
    Test case for Heap
    '''
    