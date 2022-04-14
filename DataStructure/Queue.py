from operator import ne
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

class Queue:
    '''
    This is implementation of an queue using array
    having n-1 elements at most.
    '''

    def __init__(self, n: int) -> None:
        self.queue = [0 for _ in range(n)]
        self.head = 0 
        self.tail = 0 
        self.length = n

    def __len__(self,) -> int:
        return self.length
    
    def is_empty(self,) -> bool:
        return self.head == self.tail
    
    def is_full(self,) -> bool:
        return (self.head == 0 and self.tail == self.length -1 )or (self.tail + 1 == self.head )
    
    def enqueue(self, x: Any):
        if not self.is_full():
            self.queue[self.tail] = x
            self.tail += 1
            if self.tail == self.length:
                self.tail = 0
    
    def dequeue(self,) -> Any:
        if not self.is_empty():
            item = self.queue[self.head]
            self.head +=1

            if self.head == self.length:
                self.head == 0
    
    def __str__(self, ) -> str:
        if self.head <= self.tail:
            return str(self.queue[self.head: self.tail])
        
        else:
            return str( self.queue[self.head:] + self.queue[:self.tail])

    

if __name__ == "__main__":
    n_que = Queue(4)
    n_que.enqueue(1)
    n_que.enqueue(2)
    n_que.enqueue(3)
    n_que.enqueue(4)
    print(n_que)
    n_que.dequeue()
    print(n_que)
    n_que.dequeue()
    print(n_que)
    n_que.dequeue()
    n_que.dequeue()
    n_que.enqueue(4)
    print(n_que)
