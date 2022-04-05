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

def Insertion_sort(n: int, numbers: int) -> None:
    """
    Inserion sort to sort an array of numbers in ascending order
    """

    for j in range(1, n):

        key = numbers[j]
        i = j-1

        while i >=0 and numbers[i] > key:
            numbers[i+1] = numbers[i]
            i -= 1
        numbers[i+1] = key
    


if __name__ == "__main__":
    n = int_input()
    numbers = int_list_input()

    Insertion_sort(n, numbers)

    print(numbers)