from ast import NamedExpr
from operator import index
from re import M
from typing import List, Optional


def int_input()-> int:
    '''used for integer input'''
    return(int(input()))

def list_input( seperator: str = ' ')-> List:
    '''used for list input in a line seperated by seperator'''
    return input().split(seperator)

def int_list_input(seperator: str = ' ') -> List[int]:
    '''Used to get integer list in a line'''
    return list( map(int, list_input(seperator)))

def merge(first, second):

    f_len = len(first)
    s_len = len(second)

    new_array = [0]*(f_len + s_len)

    index = 0 
    f_index = s_index = 0

    while f_index < f_len and s_index <  s_len:

        if first[f_index] < second[s_index]:
            new_array[index] = first[f_index]
            f_index += 1
        else:
            new_array[index] = second[s_index]
            s_index += 1
        index += 1
    
    while f_index < f_len:
        new_array[index] = first[f_index]
        index += 1
        f_index += 1
    while s_index < s_len:
        new_array[index] = second[s_index]
        index += 1
        s_index += 1
    
    return new_array


def mergeSort(nums: List[int]) -> List[int]:
    length = len(nums)

    if length <= 1:
        return nums
    else:
        mid = length // 2

        first = mergeSort(nums[:mid])
        second = mergeSort(nums[mid:])

        return merge(first, second)
    
if __name__ == "__main__":
    n = int_input()
    array = int_list_input()
    print("Sorted array")
    array = mergeSort(array) 
    print(array)