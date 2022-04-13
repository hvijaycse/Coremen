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

def partition(nums: List[int], low: int, high: int) -> int:

    i = low - 1
    key = nums[high - 1]

    for j in range(low, high - 1):

        if nums[j] <= key:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]

    nums[i +1], nums[high - 1] = nums[high - 1], nums[i + 1]

    return i + 1

def quick_select(low: int, high: int, nums: List[int], i: int) -> int:
    '''
    This method is used to return the iᵗʰ smallest
    number from the array nums.
    It works on the divie and conquer based algorithm.
    '''

    if low == high:
        return nums[low]
    
    pivot = partition(nums, low, high)


    lt_q = pivot - low + 1

    if lt_q == i:
        return nums[pivot]
    elif i < lt_q: 
        # In this case the i is less than total number of item in 
        # left partition so, iᵗʰ smallest item must be in left partition.
        return quick_select(low, pivot, nums, i)
    else:
        # In this case the i is greater than total number of item in 
        # left partition so, iᵗʰ smallest item must be in right partition.
        # and it will be the i-lt_q smallest in the right partition.
        return quick_select(pivot+1, high, nums, i-lt_q)

if __name__ == "__main__":
    
    array = [5,4,3,2,1,32,4,5,6,3,2]

    print(quick_select(0, len(array), array, 10))
    array.sort()
    print(array)