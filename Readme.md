# 1. **Table of Content**


- [1. **Table of Content**](#1-table-of-content)
- [2. **Algorithms List**](#2-algorithms-list)
- [3. **Learning from Coremen book.**](#3-learning-from-coremen-book)
  - [3.1. **Day 1 [04/04/2022]**](#31-day-1-04042022)
    - [3.1.1 **Learned why algorithms are technology.**](#311-learned-why-algorithms-are-technology)
    - [3.1.2. **Revised Insertion Sort**](#312-revised-insertion-sort)
  - [3.2. **Day 2[05/04/2022]**](#32-day-205042022)
    - [3.2.1. **Revised how prove the completness of an algorithm**](#321-revised-how-prove-the-completness-of-an-algorithm)
    - [3.2.2. **Revised Merge sort**](#322-revised-merge-sort)
    - [3.2.3. **Revised Divide and Conqure paradigm.**](#323-revised-divide-and-conqure-paradigm)
  

# 2. **Algorithms List**

| Name  |Time Complexity   |Space Complexity   |Link   | Day|
|---|---|---|---|---|
| Insertion Sort | O(n^2)   |O(1)   | [Inserion Sort](./Algos/InsertionSort.py)  |Day1|
| Merge Sort | O(n^2)   |O(n)   | [Merge Sort](./Algos/MergeSort.py)  |Day2|

# 3. **Learning from Coremen book.**

## 3.1. **Day 1 [04/04/2022]**
Started Coremen from begining.

### 3.1.1 **Learned why algorithms are technology.**
Alogrithm are technology becuase just like using the right technology can save a lot of effort, time and resources. Using the right algorithm help us achive the same. As technology grows and evolve so does Algorihtms.

### 3.1.2. **Revised Insertion Sort**
Insertion sort is one of the most basic sorting algorithm. This is a incremental based algorithm.

In this the key A[n] is inserted in the already sorted array A[1..n-1] so that the array A[1..n] is sorted.


## 3.2. **Day 2[05/04/2022]**
### 3.2.1. **Revised how prove the completness of an algorithm**

Following three needs to be insured that and algorithm is complete
1. Initialization
2. Maintenance
3. Termination
   
### 3.2.2. **Revised Merge sort**
Merge sort is an divied and conqure based sorting algorithm, which has time complexity of O(nlog(n)) and space complexity of O(n).

### 3.2.3. **Revised Divide and Conqure paradigm.**
Divide and conqure is one of the most used paradigm to solve problems in programming.<br>
It relies on the recursion to divide the problem into subsets, solve them and combine the result of all the subset to provide the solution of the problem.<br>
Recursion time complexity is solved using the Master theorem or Tree method, I  prefer the Tree method.
