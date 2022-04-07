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


def find_middle_continous(start, end, mid, array):

    left_max = float('-inf')
    left_temp = 0
    for i in range(mid, start-1, -1):
        left_temp += array[i]
        left_max = max(left_max, left_temp)

    right_max = float('-inf')
    right_temp = 0
    for i in range(mid+1, end+1):
        right_temp += array[i]
        right_max = max(right_max, right_temp)
    
    return max(
        left_max,
        right_max,
        left_max + right_max
    )

def recursive_maximum_subarray(start, end , array):
    """
    Recursive algorithm to find the maximum sum subarray 
    in a given array.

    Time Complexity: O(nLog(n))
    Space Complexity: O(1)
    """

    if start == end:
        return array[start]
    
    else:
        mid = (start + end) // 2

        left_max = recursive_maximum_subarray(start, mid, array)
        right_max = recursive_maximum_subarray(mid+1, end, array)

        middle_max = find_middle_continous(start, end, mid, array)

        return max(left_max, right_max, middle_max)

def linear_maximum_subarray(array):
    """
    Linear algorithm to find the maximum
    subarray in a given array 

    Time complexity: O(n)
    Space complexity: O(1)

    """

    if not array:
        return 0
    maximum = float('-inf')
    temp = 0 

    for item in array:
        temp += item

        if temp < 0:
            temp = 0
        maximum = max(maximum, temp)
    
    return maximum

if __name__ == "__main__":
    n = int_input()
    array = int_list_input()

    maximum = recursive_maximum_subarray(0, n-1, array)
    maximum = linear_maximum_subarray(array)
    print(maximum) 