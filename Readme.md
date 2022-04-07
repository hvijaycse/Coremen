# 1. **Table of Content**


- [1. **Table of Content**](#1-table-of-content)
- [2. **Algorithms List**](#2-algorithms-list)
- [3. **Learning from Coremen book.**](#3-learning-from-coremen-book)
  - [3.1. **Day 1 [04/04/2022]**](#31-day-1-04042022)
    - [3.1.1. **Learned why algorithms are technology.**](#311-learned-why-algorithms-are-technology)
    - [3.1.2. **Revised Insertion Sort**](#312-revised-insertion-sort)
  - [3.2. **Day 2[05/04/2022]**](#32-day-205042022)
    - [3.2.1. **Revised how prove the completness of an algorithm**](#321-revised-how-prove-the-completness-of-an-algorithm)
    - [3.2.2. **Revised Merge sort**](#322-revised-merge-sort)
    - [3.2.3. **Revised Divide and Conqure paradigm.**](#323-revised-divide-and-conqure-paradigm)
  - [3.3. **Day 3 [06/04/2021]**](#33-day-3-06042021)
    - [3.3.1. **Revised Asymtotic Notation**](#331-revised-asymtotic-notation)
      - [**Theta Notation (Θ-notation)**](#theta-notation-θ-notation)
      - [**Big Oh Notation (O-notation)**](#big-oh-notation-o-notation)
      - [**Omega Notation (Ω-notation)**](#omega-notation-ω-notation)
    - [3.3.2 **Divide and Conquer.**](#332-divide-and-conquer)
    - [3.2.3. **Maximum subarray problems**](#323-maximum-subarray-problems)
  - [3.4. **Day 4 [07/04/2021]**](#34-day-4-07042021)
    - [3.4.1. **Straseen's Matrix**](#341-straseens-matrix)
    - [3.4.1. **How to solve recursion and find complexity**](#341-how-to-solve-recursion-and-find-complexity)
      - [**Substitution Method**](#substitution-method)
      - [**Tree Method**](#tree-method)
      - [**Master Theorem**](#master-theorem)
  

# 2. **Algorithms List**

| Name  |Time Complexity   |Space Complexity   |Link   | Day|
|---|---|---|---|---|
| Insertion Sort | O(n^2)   |O(1)   | [Inserion Sort](./Algos/InsertionSort.py)  |Day1|
| Merge Sort | O(n^2)   |O(n)   | [Merge Sort](./Algos/MergeSort.py)  |Day2|
| Maximum Subarray Recusive | O(nlog(n))   |O(1)   | [Maximum Subarray](./Algos/MaximumSubarray.py)  |Day3|
| Maximum Subarray Linear | O(n)   |O(1)   | [Maximum Subarray](./Algos/MaximumSubarray.py)  |Day3|

# 3. **Learning from Coremen book.**

## 3.1. **Day 1 [04/04/2022]**
Started Coremen from begining.

### 3.1.1. **Learned why algorithms are technology.**
Alogrithm are technology becuase just like using the right technology can save a lot of effort, time and resources. Using the right algorithm help us achive the same. As technology grows and evolve so does Algorihtms.

### 3.1.2. **Revised Insertion Sort**
Insertion sort is one of the most basic sorting algorithm. This is a incremental based algorithm.

In this the key A[n] is inserted in the already sorted array A[1..n-1] so that the array A[1..n] is sorted.


## 3.2. **Day 2[05/04/2022]**
### 3.2.1. **Revised how prove the completness of an algorithm**

Following three needs to be insured to prove completness of a algorithm 
1. Initialization
2. Maintenance
3. Termination
   
### 3.2.2. **Revised Merge sort**
Merge sort is an divied and conqure based sorting algorithm, which has time complexity of O(nlog(n)) and space complexity of O(n).

### 3.2.3. **Revised Divide and Conqure paradigm.**
Divide and conqure is one of the most used paradigm to solve problems in programming.<br>
It relies on the recursion to divide the problem into subsets, solve them and combine the result of all the subset to provide the solution of the problem.<br>
Recursion time complexity is solved using the Master theorem or Tree method, I  prefer the Tree method.


## 3.3. **Day 3 [06/04/2021]**

### 3.3.1. **Revised Asymtotic Notation**

In real world the exact precision of what is the runtime of an algorithms are not required.<br>
Rather we use we express the effeciency or runtime of an algorithm based on the suffecient large number of input sizes to make only the growth of runtime relevant. We study the asymtotic efficiency of the algorithm. 

We mostly use 3 type of notations to express algorithm.

####  **Theta Notation (Θ-notation)**

For a function f(n) its time complexity is Θ(g(n))<br>
If and only if there exist two values c1 and c2 for all values of n greater than n' such that:<br>
c1*g(n) <= f(n) <= c2*g(n),  Where n >= n' <br>

This basically means that the function f is sandwiched between function g for suffeciently large n. Refer below image for more clear explanation.

![Theta Notaion](images/Theta.png "Theta notation visualised")

####  **Big Oh Notation (O-notation)**

For a function f(n) its time complexity is O(g(n))<br>
If and only if there exist one value c1 for all values of n greater than n' such that:<br>
f(n) <= c1*g(n),  Where n >= n' <br>

This basically means that the function f is lower than g for suffeciently large n.

> Note: This means a function f(n) = n have O(n^2) complexity

Negative potential consequences of an action
Refer below image for more clear explanation.

![Big Oh Notation](images/BigO.png) 

####  **Omega Notation (Ω-notation)**

For a function f(n) its time complexity is O(g(n))<br>
If and only if there exist one value c1 for all values of n greater than n' such that:<br>
c1*g(n) <= f(n)  ,  Where n >= n' <br>

> Note: This means a function f(n) = n^2 have Ω(n) complexity

This basically means that the function f is greater than g for suffeciently large n. Refer below image for more clear explanation.

![Big Oh Notation](images/Omega.png) 


### 3.3.2 **Divide and Conquer.**
Revied the divide and conque paradigm in chapter 4.

Divide and conquer have mainly 3 parts. 
1. Divide: the problem into a number of subproblems that are smaller instances of the same problem.
2. Conquer: the subproblems by solving them reccursively. If the subproblem sizes are small enough then just solve the subproblems in a straightforward manner.
3. Combine: the solutions to the subproblems into the solution for the original problem.
   
### 3.2.3. **Maximum subarray problems**
Revised the maximum subarray problem and learned the three ways to solve it.
1. Brute force method having O(n^2) complexity
2. Divide and Conquer method having O(nlogn) complexity
3. Incremental method having O(n) complexity 

## 3.4. **Day 4 [07/04/2021]**

### 3.4.1. **Straseen's Matrix**
This is a matrix multiplication algorithm which is based on divide and conqure paradigm, In this the original matrix is divide into 4 equall parts and then the resulting matrix is calulated using some formulas.

But rather than having 8 n*n multiplications it only does 7 and hence get an time compleity of O(n^ln(7)) lesser then O(n^3).

I dont understand it properly and will come back to it again if required.

### 3.4.1. **How to solve recursion and find complexity**

There are three method to solve recursions.

#### **Substitution Method**
In this we first guess what might be the complexity of the algorithm and based on that we prove that it might be right using mathematical induction.

#### **Tree Method**
This is not exacly a method to find the complexity of the algorithm but it help us at guessing what it might be. This is a visual way in which we represent the recurssion in the form of a tree.

For example:

> For a recurssion  T(n) = a*T(n/b) + f(n)
> 
> In the tree representation the root node is  the extra complexity attached with the i.e f(n) 
>
> The leaf nodes represent the base case generally a contant time complexity o(1) 
>
>And there are total ln(b) levels
>
> See image below for better understanding. 
![Tree Recursion](images/tree_recursion.png)

We sum the cost of all the levels which is then proper guess at the time complexity of algoritm

#### **Master Theorem**

This method is used to calculate the time complexity of a recursion in for of:<br>
>T(n) = a*T(n/b) + f(n)

It have three rules.

First make another function G(n) such that:<br>
> g(n) = n^ (logb(a))  [log a to the base b]

Now Compare g(n) and f(n)

1. If f(n) > g(n), Then the complexity if O(f(n))
2. If g(n) > f(n), Then the complexity is O(g(n))
3. Otherwise Both are same time, Then the complexity is O( log(n) * f(n) )
 