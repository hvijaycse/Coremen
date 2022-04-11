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

def radixSort(nums: List[int]) -> List[int]:
    
    max_digits = len(str(max(nums)))

    for digit in range(1, max_digits + 1):
        nums.sort(key = lambda x: x % 10**digit)


if __name__ == "__main__":
    array = [329, 457,657,839,436,720,355]
    print(array)
    radixSort(array)
    print(array)
