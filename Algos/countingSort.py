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

def countingSort(nums: List[int]) -> List[int]:
    '''
    Implementation of counting sort
    Time complexity: O(n)
    Space complexity: O(n)
    
    '''
    C = [0 for _ in range(max(nums))]
    B = [0 for _ in range(len(nums))]

    for num in nums:
        C[num-1] += 1
    
    for i in range(1, len(nums)):
        C[i] += C[i-1]
    
    for i in range(len(nums)-1, -1, -1):

        B[C[nums[i]-1]-1] = nums[i]
        C[nums[i]-1] -= 1
    
    return B

if __name__ == "__main__":
    array = [9,8,7,6,5,4,3,2,1]
    print(array)
    print(countingSort(array))
    