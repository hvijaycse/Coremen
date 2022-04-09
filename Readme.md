# 1. **Introduction to Coremen**
Hi Everyone, I am Harsh Vijay.

This is my attempt to learn and improve my Data Structures and Algorithms. I am learning from book which is considered to be the Geeta for DSA and computer science **Introduction to Algorithm**.

This is a really great book and also one of the most recommended, I have tried earlier to learn from this got partial success but was not able to complete it fully, hence attempting this again. 

This time I am maintaining this repo, this is serve multiple purposes, some of them are.

- This serve are a record in which I can track my daily progress, my aim is to never miss reading the book on any day, but if that ever come I will record that too.
- This will come useful in future for revision purposes. A small simple explanation with implementaton and images if suitable, I think this is will be enough.
- This help me motivate to learn everyday. In the morning after I read the next concepts from the book, it takes me 15~20 minutes to udpate this repo and I like regularly updating my progress and see myself grow. This is my reward for learning daily. I learned this technique from the book **Atomic habit** and aimimng to get better 1% everyday with this.
- In case I get success, I will share this method/technique with other and utilize it more for myself.

 
# 2. **Table of Content**

- [1. **Introduction to Coremen**](#1-introduction-to-coremen)
- [2. **Table of Content**](#2-table-of-content)
- [3. **Algorithms**](#3-algorithms)
- [4. **Data Strucutres**](#4-data-strucutres)
- [5. **Learning from Coremen book.**](#5-learning-from-coremen-book)
  - [5.1. **Day 1 [04/04/2022]**](#51-day-1-04042022)
    - [5.1.1. **Learned why algorithms are technology.**](#511-learned-why-algorithms-are-technology)
    - [5.1.2. **Revised Insertion Sort**](#512-revised-insertion-sort)
  - [5.2. **Day 2[05/04/2022]**](#52-day-205042022)
    - [5.2.1. **Revised how prove the completness of an algorithm**](#521-revised-how-prove-the-completness-of-an-algorithm)
    - [5.2.2. **Revised Merge sort**](#522-revised-merge-sort)
    - [5.2.3. **Revised Divide and Conqure paradigm.**](#523-revised-divide-and-conqure-paradigm)
  - [5.3. **Day 3 [06/04/2021]**](#53-day-3-06042021)
    - [5.3.1. **Revised Asymtotic Notation**](#531-revised-asymtotic-notation)
      - [5.3.1.1. **Theta Notation (Θ-notation)**](#5311-theta-notation-θ-notation)
      - [5.3.1.2. **Big Oh Notation (O-notation)**](#5312-big-oh-notation-o-notation)
      - [5.3.1.3. **Omega Notation (Ω-notation)**](#5313-omega-notation-ω-notation)
    - [5.3.2. **Divide and Conquer.**](#532-divide-and-conquer)
    - [5.3.3. **Maximum subarray problems**](#533-maximum-subarray-problems)
  - [5.4. **Day 4 [07/04/2021]**](#54-day-4-07042021)
    - [5.4.1. **Straseen's Matrix**](#541-straseens-matrix)
    - [5.4.2. **How to solve recursion and find complexity**](#542-how-to-solve-recursion-and-find-complexity)
      - [5.4.2.1. **Substitution Method**](#5421-substitution-method)
      - [5.4.2.2. **Tree Method**](#5422-tree-method)
      - [5.4.2.3. **Master Theorem**](#5423-master-theorem)
  - [5.5. **Day5 [08/04/2020]**](#55-day5-08042020)
    - [5.5.1. **Heap**](#551-heap)
      - [5.5.1.1. **Max Heap**](#5511-max-heap)
      - [5.5.1.2. **Min Heap**](#5512-min-heap)
    - [5.5.2. **Methods of a Heap**](#552-methods-of-a-heap)
      - [5.5.2.1. **Max-heapify(A, i)**](#5521-max-heapifya-i)
      - [5.5.2.2. **Build-Max-heap(A)**](#5522-build-max-heapa)
    - [5.5.3. **Sorting using heap**](#553-sorting-using-heap)
  - [5.6. **Day 6 [09/04/2022]**](#56-day-6-09042022)
    - [5.6.1. **Priority Queue**](#561-priority-queue)
    - [5.6.2. **Methods of Max_heap**](#562-methods-of-max_heap)
      - [5.6.2.1. **Heap_maximum**](#5621-heap_maximum)
      - [5.6.2.2. **Heap_extract_max**](#5622-heap_extract_max)
      - [5.6.2.3. **Heap_increase_key**](#5623-heap_increase_key)
      - [5.6.2.4. **Max_heap_insert**](#5624-max_heap_insert)
  

# 3. **Algorithms**

| Name  |Time Complexity   |Space Complexity   |Link   | Day|
|---|---|---|---|---|
| Insertion Sort | O(n^2)   |O(1)   | [Inserion Sort](./Algos/InsertionSort.py)  |Day1|
| Merge Sort | O(n^2)   |O(n)   | [Merge Sort](./Algos/MergeSort.py)  |Day2|
| Maximum Subarray Recusive | O(nlog(n))   |O(1)   | [Maximum Subarray](./Algos/MaximumSubarray.py)  |Day3|
| Maximum Subarray Linear | O(n)   |O(1)   | [Maximum Subarray](./Algos/MaximumSubarray.py)  |Day3|

# 4. **Data Strucutres**


|Name  |Link  |Day |
|---------|---------|---------|
|Heap     | [max heap](DataStructure/Heap.py)       | Day 5        |
|Priority Queue     | [max priority queue](DataStructure/PriorityQueue.py)       | Day 6        |

# 5. **Learning from Coremen book.**

## 5.1. **Day 1 [04/04/2022]**
Started Coremen from begining.

### 5.1.1. **Learned why algorithms are technology.**
Alogrithm are technology becuase just like using the right technology can save a lot of effort, time and resources. Using the right algorithm help us achive the same. As technology grows and evolve so does Algorihtms.

### 5.1.2. **Revised Insertion Sort**
Insertion sort is one of the most basic sorting algorithm. This is a incremental based algorithm.

In this the key A[n] is inserted in the already sorted array A[1..n-1] so that the array A[1..n] is sorted.


## 5.2. **Day 2[05/04/2022]**
### 5.2.1. **Revised how prove the completness of an algorithm**

Following three needs to be insured to prove completness of a algorithm 
1. Initialization
2. Maintenance
3. Termination
   
### 5.2.2. **Revised Merge sort**
Merge sort is an divied and conqure based sorting algorithm, which has time complexity of O(nlog(n)) and space complexity of O(n).

### 5.2.3. **Revised Divide and Conqure paradigm.**
Divide and conqure is one of the most used paradigm to solve problems in programming.<br>
It relies on the recursion to divide the problem into subsets, solve them and combine the result of all the subset to provide the solution of the problem.<br>
Recursion time complexity is solved using the Master theorem or Tree method, I  prefer the Tree method.


## 5.3. **Day 3 [06/04/2021]**

### 5.3.1. **Revised Asymtotic Notation**

In real world the exact precision of what is the runtime of an algorithms are not required.<br>
Rather we use we express the effeciency or runtime of an algorithm based on the suffecient large number of input sizes to make only the growth of runtime relevant. We study the asymtotic efficiency of the algorithm. 

We mostly use 3 type of notations to express algorithm.

####  5.3.1.1. **Theta Notation (Θ-notation)**

For a function f(n) its time complexity is Θ(g(n))<br>
If and only if there exist two values c1 and c2 for all values of n greater than n' such that:<br>
c1*g(n) <= f(n) <= c2*g(n),  Where n >= n' <br>

This basically means that the function f is sandwiched between function g for suffeciently large n. Refer below image for more clear explanation.

![Theta Notaion](images/Theta.png "Theta notation visualised")

####  5.3.1.2. **Big Oh Notation (O-notation)**

For a function f(n) its time complexity is O(g(n))<br>
If and only if there exist one value c1 for all values of n greater than n' such that:<br>
f(n) <= c1*g(n),  Where n >= n' <br>

This basically means that the function f is lower than g for suffeciently large n.

> Note: This means a function f(n) = n have O(n^2) complexity

Negative potential consequences of an action
Refer below image for more clear explanation.

![Big Oh Notation](images/BigO.png) 

####  5.3.1.3. **Omega Notation (Ω-notation)**

For a function f(n) its time complexity is O(g(n))<br>
If and only if there exist one value c1 for all values of n greater than n' such that:<br>
c1*g(n) <= f(n)  ,  Where n >= n' <br>

> Note: This means a function f(n) = n^2 have Ω(n) complexity

This basically means that the function f is greater than g for suffeciently large n. Refer below image for more clear explanation.

![Big Oh Notation](images/Omega.png)    


### 5.3.2. **Divide and Conquer.**
Revied the divide and conque paradigm in chapter 4.

Divide and conquer have mainly 3 parts. 
1. Divide: the problem into a number of subproblems that are smaller instances of the same problem.
2. Conquer: the subproblems by solving them reccursively. If the subproblem sizes are small enough then just solve the subproblems in a straightforward manner.
3. Combine: the solutions to the subproblems into the solution for the original problem.
   
### 5.3.3. **Maximum subarray problems**
Revised the maximum subarray problem and learned the three ways to solve it.
1. Brute force method having O(n^2) complexity
2. Divide and Conquer method having O(nlogn) complexity
3. Incremental method having O(n) complexity 

## 5.4. **Day 4 [07/04/2021]**

### 5.4.1. **Straseen's Matrix**
This is a matrix multiplication algorithm which is based on divide and conqure paradigm, In this the original matrix is divide into 4 equall parts and then the resulting matrix is calulated using some formulas.

But rather than having 8 n*n multiplications it only does 7 and hence get an time compleity of O(n^ln(7)) lesser then O(n^3).

I dont understand it properly and will come back to it again if required.

### 5.4.2. **How to solve recursion and find complexity**

There are three method to solve recursions.

#### 5.4.2.1. **Substitution Method**
In this we first guess what might be the complexity of the algorithm and based on that we prove that it might be right using mathematical induction.

#### 5.4.2.2. **Tree Method**
This is not exacly a method to find the complexity of the algorithm but it help us at guessing what it might be. This is a visual way in which we represent the recurssion in the form of a tree.

For example:

> For a recurssion  T(n) = a*T(n/b) + f(n)
> 
> In the tree representation the root node is  the extra complexity attached with the i.e f(n) 
>
> The leaf nodes represent the base case generally a contant time complexity o(1) 
>
>And there are total ln(b) + 1 levels
>
> See image below for better understanding. 
![Tree Recursion](images/tree_recursion.png)

We sum the cost of all the levels which is then proper guess at the time complexity of algoritm

#### 5.4.2.3. **Master Theorem**

This method is used to calculate the time complexity of a recursion in for of:<br>
>T(n) = a*T(n/b) + f(n)

It have three rules.

First make another function G(n) such that:<br>
> g(n) = n^ (logb(a))  [log a to the base b]

Now Compare g(n) and f(n)

1. If f(n) > g(n), Then the complexity if O(f(n))
2. If g(n) > f(n), Then the complexity is O(g(n))
3. Otherwise Both are same time, Then the complexity is O( log(n) * f(n) )
 

## 5.5. **Day5 [08/04/2020]**
Today I skipped chapter 5th from the book.<br>
Started Sorting and order statistics.
### 5.5.1. **Heap**
Heap is the data structure which when visualised like a balanced binary tree.

> Note: All the subtree in a heap are also a heap

There are two type of heap: Max heap and Min heap.

Heap uses three methods: Left, Right, Parent.
Each of which take an index and return the index of left node, right node and parent node correspondingly.

#### 5.5.1.1. **Max Heap**

For all the elements in the heap A, max heap insured the following property:

The A[i] >= A[left(i)] and A[i] >= A[right(i)]

Hence the maximum element in a max heap is present at the root node. 
> Note: A reverse sorted list is also and max heap


#### 5.5.1.2. **Min Heap**

For all the elements in the heap A, min heap insured the following property:

The A[i] <= A[left(i)] and A[i] <= A[right(i)]

Hence the minimum element in a min heap is present at the root node. 
> Note: A sorted list is also and max heap


### 5.5.2. **Methods of a Heap**
> Notes:
> >Here I am only mentioning method for Max heap same methods also exists for min heap as well.
>  
> >All the algorithms mentioned for heap in this are based on 1 indexing and are implemented for 0 based indexing in the DataStructure directory.

#### 5.5.2.1. **Max-heapify(A, i)**
This method asumme that the Left(i) and Right(i) subtree are also heap but the condition:

A[i] >= A[ Left(i) ] and A[i] >= A[ Right(i) ]

But be failing at index i hence the heap is not max heap.<br>
So to solve this it check the condition if it it fulfilled it does nothing otherwise get the index largest element from left or right let it be j, then swap the A[i] with A[j] and recursively call the Max-heapify index j.<br>
Algorithm for this.
```
max_heapify(array, index) ->
  largest_index = index
  left_index = left(index)
  right_index = right(index)

  if left_index <= array.size and array[left_index] > array[largest_index]:
    largest_index = left_index
  
  if right_index <= array.size and array[right_index] > array[largest_index]:
    largest_index = right_index
  
  if largest_index != index:
    swap(index, largest_index)
    max_heapify(largest_index)
```

It ensure that the condition is meet at index i.

#### 5.5.2.2. **Build-Max-heap(A)**
This method is used to create the heap meaning the condition is fulfilled at every index in the heap.

It procedure is:
```
build_max_heap(array) ->
  length = array.size
  for index from length//2 to 1:
    max_heapify(array, index)
```
This start from bottom toward up because MAx-heapify assume that the Left and Right subtree are also max-heap which will be False if we go to top to bottom.

### 5.5.3. **Sorting using heap**
Heap Structure can be for sorting as well.<br>
Logic used in this process is that:

```
heap_sort(array) -> 
  array = build_max_heap(array)
  for i from array.length to 2:
    swap(array[1], array[i])
    array.size -= 1
    max_heapify(array, 1)
```
Heap sort has time complexity of O(nlog(n)) but a better implementation of qiuck sort has lower constant coeffecient hence resulting in faster performance.<br>

## 5.6. **Day 6 [09/04/2022]**

### 5.6.1. **Priority Queue**
Heap is an amazing data structure and can also be used to implement priority queue which have many use cases such as job scheduling based on priorty, etc.

Same as heap priorty queue is also of 2 types:
1. Max priority queue
2. Min priority queue
   
Here I am only explaining max priority but on similar basis min prority can also be implemented.

### 5.6.2. **Methods of Max_heap**
> Note:
> > The algos shown in the document are based on 1 based indexing and are implemented on 0 based indexing in the DataStructure directory.

#### 5.6.2.1. **Heap_maximum**
This method return the maximum priority item in the queue.

Algo:
```
heap_max(a) -> 
  return a[1]
```

#### 5.6.2.2. **Heap_extract_max**
This method pop the maximum priority item in the queue and also remove it from the queue.

Algo:
```
heap_extract_maximum(a) ->
  maximum = a[1]
  swap(a[1], a[a.size])
  a.size -= 1
  max_heapify(a, 1)
  return max
```

#### 5.6.2.3. **Heap_increase_key**
This method increase the key of an item at index.

Algo:
```
heap_increase_key(a, i, k):
  if k < a[i]:
    Error "Key is smaller can't insert"
    exit

  while i > 1 and a[parent(i)] < k:
    a[i] = a[parent(i)]
    i = parent(i)
  a[i] = k
```

#### 5.6.2.4. **Max_heap_insert**
This method is used to insert a new item in the heap.

Algo:
```
max_heap_insert(a, key):
  a.size += 1
  a[a.size] = -inf
  heap_increase_key(a, a.size, key)
```