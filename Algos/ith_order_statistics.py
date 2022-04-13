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

def select(nums: List[int], i : int ) -> int:
    '''
    This method return the iᵗʰ smallest
    number in the array.
    '''

    nums.sort()

    try:
        return nums[i-1]
    except IndexError:
        print("i is greater than the legnth of array.")
    

if __name__ == "__main__":
    pass