from re import L
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

def swap(nums: List[int], i: int, j:int ) -> None:
    '''
    method to inplace swap item at index i and j of an list
    '''
    length = len(nums)
    if i >= length or j>= length:
        raise IndexError
    nums[i], nums[j] = nums[j], nums[i]
    return

def partition(nums: List[int], p: int, q: int) -> int:
    '''
    This method find the pivot element in the list
    nums[p..q] q not inclusive. 
    '''
    key = nums[q-1]
    i = p-1
    
    for j in range(p, q-1):

        if nums[j] <= key:
            i += 1
            swap(nums, i, j)
    
    swap(nums, i+1, q-1)

    return i + 1

def quickSort(
        nums: List[int], 
        start: int = None, 
        end:int = None
        ) -> None:
    '''
    This is the implementation of quick sort algoritm.
    both  start and end are inclusive in the array index.
    '''
    if start is None:
        start = 0
    if end is None:
        end = len(nums)

    if start < end:

        q = partition(nums, start, end)
        quickSort(nums, start, q)
        quickSort(nums, q+1, end)

if __name__ == "__main__":
    nums = [5,4,3,2,1]
    quickSort(nums)
    print(nums)