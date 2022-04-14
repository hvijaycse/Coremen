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

class Stack:

    def __init__(self, n: int) -> None:
        self.top = 0
        self.length = n
        self.stack = [0 for _ in range(n)]
    
    def __len__(self,) -> int:
        return self.length
    
    def is_empty(self, ) -> bool:
        return self.top == 0

    def is_full(self, ) -> bool:
        return self.top == len(self)
    
    def push(self, x: Any):
        
        if not self.is_full():
            self.stack[self.top] = x
            self.top += 1
        else:
            print("Error: Stack overflow")
        return self
    def pop(self, ):
        
        if not self.is_empty():
            item = self.stack[self.top - 1]
            self.top -= 1
            return item
        else:
            print("Error: Stack underflow")
    
    def __str__(self) -> str:
        return str(self.stack[:self.top])



if __name__ == "__main__":
    test_stack = Stack(4)
    
    test_stack.push(1)
    test_stack.push(2)
    test_stack.push(3)
    test_stack.push(4)
    print(test_stack)
    test_stack.pop()
    print(test_stack)
    test_stack.push(6)
    test_stack.push(6)
    print(test_stack)
    test_stack.pop()
    test_stack.pop()
    test_stack.pop()
    test_stack.pop()
    test_stack.pop()
    print(test_stack)