from cmath import log
from typing import List, Optional, Any, Dict


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

class Heap:
    '''
    Implementation of max heap 
    '''


    def __init__(self, array: List[int] ) -> None:
        
        self.array = array
        self.length = len(array)
        self.build_maxheap()
    
    def left(self, index: int) -> int:
        # return the index of left child in 
        # 0 based indexing.
        return (index << 1) + 1
    
    def right(self, index: int) -> int:
        # Return the index of left child in
        # 0 based indexing.
        return (index + 1) << 1
    
    def max_heapify(self, i: int ) -> None:
        '''
        This method check if the condition 
        of heap is fulfilled at the index i or not
        if not it corrects it.
        '''

        while i < self.length:
            largest = i 
            l_i = self.left(i)
            r_i = self.right(i)

            if l_i < self.length and self.array[l_i] > self.array[largest]:
                largest = l_i

            if r_i < self.length and self.array[r_i] > self.array[largest]:
                largest = r_i
            
            
            if largest != i:
                self.array[i], self.array[largest] = self.array[largest], self.array[i]
                i = largest
            else:
                break
        
    def build_maxheap(self):
        for index in range(self.length-1, -1, -1):
            self.max_heapify(index)
    
    def vis_tree(self) -> None:

        Spaces = self.length // 2

        left = 0 
        element = 1 
        rows = int(log(self.length, 2).real) + 1
        Total_elements = 0
        for r in range(rows):
            print(' '*Spaces, end='')
            for index in range(left, left + element):
                print(f"{self.array[index]:2} ", end=' ')
            print()
            Spaces -= 1
            print(" "*(Spaces+1),end='')
            for _ in range(element):
                print('/\\', end='  ')
            print()
            Spaces -=1 
            Total_elements += element
            element = min(element * 2, self.length-Total_elements)
            left = self.left(left)

if __name__ == "__main__":
    '''
    Test case for Heap
    '''
    Array = list(range(20))

    new_heap = Heap(Array)

    print(new_heap.array)