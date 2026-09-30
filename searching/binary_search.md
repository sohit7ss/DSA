# Binary Search — Complete DSA Notes

> Binary Search is an efficient searching algorithm that repeatedly divides a sorted or monotonic search space into two halves.

---

# Table of Contents

- [1. Introduction](#1-introduction)
- [2. Why Binary Search?](#2-why-binary-search)
- [3. Requirement](#3-requirement)
- [4. Core Idea](#4-core-idea)
- [5. How Binary Search Works](#5-how-binary-search-works)
- [6. Low, Mid, High](#6-low-mid-high)
- [7. Standard Algorithm](#7-standard-algorithm)
- [8. Basic Implementation](#8-basic-implementation)
- [9. Dry Run](#9-dry-run)
- [10. Complexity](#10-complexity)
- [11. Why O(log n)?](#11-why-olog-n)
- [12. Iterative Binary Search](#12-iterative-binary-search)
- [13. Recursive Binary Search](#13-recursive-binary-search)
- [14. Iterative vs Recursive](#14-iterative-vs-recursive)
- [15. Mid Calculation](#15-mid-calculation)
- [16. Boundary Conditions](#16-boundary-conditions)
- [17. First Occurrence](#17-first-occurrence)
- [18. Last Occurrence](#18-last-occurrence)
- [19. Count Occurrences](#19-count-occurrences)
- [20. Lower Bound](#20-lower-bound)
- [21. Upper Bound](#21-upper-bound)
- [22. Search Insert Position](#22-search-insert-position)
- [23. Floor](#23-floor)
- [24. Ceil](#24-ceil)
- [25. Descending Array](#25-descending-array)
- [26. Order-Agnostic Search](#26-order-agnostic-search)
- [27. Rotated Sorted Array](#27-rotated-sorted-array)
- [28. Rotated Array with Duplicates](#28-rotated-array-with-duplicates)
- [29. Find Minimum in Rotated Array](#29-find-minimum-in-rotated-array)
- [30. Find Peak Element](#30-find-peak-element)
- [31. Mountain Array](#31-mountain-array)
- [32. Binary Search on Answer](#32-binary-search-on-answer)
- [33. Monotonic Predicate](#33-monotonic-predicate)
- [34. First True](#34-first-true)
- [35. Last True](#35-last-true)
- [36. Python bisect Module](#36-python-bisect-module)
- [37. Common Mistakes](#37-common-mistakes)
- [38. How to Identify Binary Search Problems](#38-how-to-identify-binary-search-problems)
- [39. Problem-Solving Checklist](#39-problem-solving-checklist)
- [40. Important Templates](#40-important-templates)
- [41. Practice Problems](#41-practice-problems)
- [42. Quick Revision](#42-quick-revision)
- [43. Final Cheat Sheet](#43-final-cheat-sheet)

---

# 1. Introduction

## What is Binary Search?

**Binary Search** is a searching algorithm used to find an element efficiently in a **sorted search space**.

Instead of checking every element one by one, Binary Search repeatedly divides the search space into two halves.

The basic process is:

1. Find the middle element.
2. Compare the middle element with the target.
3. If the middle element is the target, return it.
4. If the target is greater, search the right half.
5. If the target is smaller, search the left half.
6. Repeat until the target is found or the search space becomes empty.

---

## Simple Example

Consider:

```text
arr = [10, 20, 30, 40, 50, 60, 70]
target = 60
```

The middle element is:

```text
40
```

Since:

```text
40 < 60
```

we know that `60` must be on the right side.

So we discard:

```text
[10, 20, 30, 40]
```

and search:

```text
[50, 60, 70]
```

Again, find the middle:

```text
60
```

Since:

```text
60 == 60
```

the target is found.

---

# 2. Why Binary Search?

Suppose we have:

```text
[1, 2, 3, 4, 5, 6, 7, 8, ..., 1,000,000]
```

## Linear Search

Linear Search may check:

```text
1 → 2 → 3 → 4 → 5 → ... → 1,000,000
```

Worst-case complexity:

```text
O(n)
```

---

## Binary Search

Binary Search reduces the search space:

```text
1,000,000
     ↓
500,000
     ↓
250,000
     ↓
125,000
     ↓
...
```

Approximately:

```text
log₂(1,000,000) ≈ 20
```

operations are required.

Therefore:

```text
Linear Search  → O(n)
Binary Search  → O(log n)
```

---

# 3. Requirement

Standard Binary Search requires the search space to be **sorted**.

## Ascending Order

```python
arr = [10, 20, 30, 40, 50]
```

## Descending Order

```python
arr = [50, 40, 30, 20, 10]
```

Binary Search can work with both, but the comparison logic must be different.

---

## Unsorted Array

This array is not suitable for standard Binary Search:

```python
arr = [30, 10, 50, 20, 40]
```

Why?

Because we cannot determine which half can be discarded based on the middle element.

---

# 4. Core Idea

The most important idea of Binary Search is:

> **Eliminate half of the search space at every step.**

Suppose:

```text
[10, 20, 30, 40, 50, 60, 70]
```

Target:

```text
60
```

Initially:

```text
low = 0
high = 6
```

Middle:

```text
mid = 3
```

Value:

```text
arr[mid] = 40
```

Since:

```text
40 < 60
```

we know:

```text
target is somewhere to the right
```

Therefore:

```python
low = mid + 1
```

The new search space becomes:

```text
[50, 60, 70]
```

---

# 5. How Binary Search Works

Binary Search uses three main variables:

```text
low
mid
high
```

Consider:

```text
[10, 20, 30, 40, 50, 60, 70]
```

Visual representation:

```text
low                    high
 ↓                       ↓
[10, 20, 30, 40, 50, 60, 70]
            ↑
           mid
```

---

## Case 1: Target Found

If:

```python
arr[mid] == target
```

then:

```python
return mid
```

---

## Case 2: Target is Greater

If:

```python
arr[mid] < target
```

then the target must be on the right.

Therefore:

```python
low = mid + 1
```

---

## Case 3: Target is Smaller

If:

```python
arr[mid] > target
```

then the target must be on the left.

Therefore:

```python
high = mid - 1
```

---

# 6. Low, Mid, High

## `low`

`low` represents the first possible index of the current search space.

```python
low = 0
```

---

## `high`

`high` represents the last possible index of the current search space.

```python
high = len(arr) - 1
```

---

## `mid`

`mid` represents the middle index.

```python
mid = low + (high - low) // 2
```

---

## Example

```text
arr = [10, 20, 30, 40, 50, 60, 70]

index:
        0   1   2   3   4   5   6
value:
       10  20  30  40  50  60  70

low = 0
high = 6

mid = 3
```

Therefore:

```text
arr[mid] = arr[3] = 40
```

---

# 7. Standard Algorithm

```text
1. Set low = 0.
2. Set high = n - 1.
3. Repeat while low <= high:
   a. Calculate mid.
   b. If arr[mid] == target:
      return mid.
   c. If arr[mid] < target:
      search right half.
   d. Otherwise:
      search left half.
4. If the loop ends:
   return -1.
```

---

# 8. Basic Implementation

```python
def binary_search(arr, target):

    low = 0
    high = len(arr) - 1

    while low <= high:

        mid = low + (high - low) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1
```

---

## Example

```python
arr = [10, 20, 30, 40, 50, 60, 70]

target = 50

result = binary_search(arr, target)

print(result)
```

Output:

```text
4
```

Because:

```text
arr[4] = 50
```

---

# 9. Dry Run

Consider:

```text
arr = [10, 20, 30, 40, 50, 60, 70]
target = 60
```

---

## Iteration 1

Initial:

```text
low = 0
high = 6
```

Calculate:

```text
mid = 0 + (6 - 0) // 2
mid = 3
```

Therefore:

```text
arr[mid] = arr[3] = 40
```

Comparison:

```text
40 < 60
```

Therefore:

```python
low = mid + 1
```

New values:

```text
low = 4
high = 6
```

---

## Iteration 2

Calculate:

```text
mid = 4 + (6 - 4) // 2
mid = 5
```

Therefore:

```text
arr[5] = 60
```

Comparison:

```text
60 == 60
```

Target found.

Answer:

```text
5
```

---

## Visual Dry Run

```text
Initial:

[10, 20, 30, 40, 50, 60, 70]
 ↑           ↑                 ↑
low         mid               high

40 < 60

Search right:

[50, 60, 70]
 ↑    ↑    ↑
low  mid  high

60 == 60

FOUND
```

---

# 10. Complexity

## Time Complexity

Binary Search eliminates approximately half of the search space in every iteration.

Therefore:

```text
O(log n)
```

---

## Space Complexity

### Iterative

```text
O(1)
```

### Recursive

```text
O(log n)
```

because recursive calls are stored on the call stack.

---

## Complexity Table

| Case | Time Complexity |
|---|---:|
| Best Case | O(1) |
| Average Case | O(log n) |
| Worst Case | O(log n) |

---

# 11. Why O(log n)?

Suppose the array contains `n` elements.

After each iteration:

```text
n
n/2
n/4
n/8
n/16
...
```

After `k` iterations:

```text
n / 2^k = 1
```

Therefore:

```text
n = 2^k
```

Taking logarithm:

```text
k = log₂(n)
```

Therefore:

```text
Binary Search = O(log n)
```

---

# 12. Iterative Binary Search

The iterative approach uses a `while` loop.

```python
def binary_search(arr, target):

    low = 0
    high = len(arr) - 1

    while low <= high:

        mid = low + (high - low) // 2

        if arr[mid] == target:
            return mid

        if arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1
```

Complexity:

```text
Time  = O(log n)
Space = O(1)
```

---

# 13. Recursive Binary Search

Binary Search can also be implemented recursively.

```python
def binary_search(arr, low, high, target):

    if low > high:
        return -1

    mid = low + (high - low) // 2

    if arr[mid] == target:
        return mid

    elif arr[mid] < target:

        return binary_search(
            arr,
            mid + 1,
            high,
            target
        )

    else:

        return binary_search(
            arr,
            low,
            mid - 1,
            target
        )
```

---

## Usage

```python
arr = [10, 20, 30, 40, 50]

result = binary_search(
    arr,
    0,
    len(arr) - 1,
    40
)

print(result)
```

Output:

```text
3
```

---

# 14. Iterative vs Recursive

| Feature | Iterative | Recursive |
|---|---|---|
| Time | O(log n) | O(log n) |
| Space | O(1) | O(log n) |
| Stack | No | Yes |
| Performance | Better | Slight overhead |
| Code | Simple | Elegant |

For competitive programming and interviews, the **iterative approach is usually preferred**.

---

# 15. Mid Calculation

Two common formulas are:

```python
mid = (low + high) // 2
```

and:

```python
mid = low + (high - low) // 2
```

The second formula is generally preferred:

```python
mid = low + (high - low) // 2
```

In languages with fixed-size integers such as C++ and Java, this avoids potential overflow from:

```python
low + high
```

In Python, integer overflow is not normally an issue, but using the safer formula is a good habit.

---

# 16. Boundary Conditions

For standard exact Binary Search:

```python
while low <= high:
```

is normally used.

---

## Why `<=`?

Suppose:

```text
arr = [10, 20, 30]
```

and:

```text
low = 2
high = 2
```

There is still one element to check:

```text
arr[2] = 30
```

Therefore:

```python
while low <= high:
```

must allow the case:

```text
low == high
```

---

## Common Mistake

Using:

```python
while low < high:
```

for the standard exact-search template can cause the final candidate to be skipped.

Note that `<` is correct for many **boundary-search** templates such as Lower Bound, so the loop condition depends on the problem.

---

# 17. First Occurrence

Suppose:

```text
arr = [1, 2, 2, 2, 3, 4]
target = 2
```

We have:

```text
index:  0  1  2  3  4  5
value:  1  2  2  2  3  4
           ↑
       first occurrence
```

Answer:

```text
1
```

---

## Idea

When we find the target:

```python
arr[mid] == target
```

do not stop.

Instead:

```python
ans = mid
high = mid - 1
```

Continue searching to the left.

---

## Code

```python
def first_occurrence(arr, target):

    low = 0
    high = len(arr) - 1

    ans = -1

    while low <= high:

        mid = low + (high - low) // 2

        if arr[mid] == target:

            ans = mid
            high = mid - 1

        elif arr[mid] < target:

            low = mid + 1

        else:

            high = mid - 1

    return ans
```

---

# 18. Last Occurrence

Consider:

```text
arr = [1, 2, 2, 2, 3, 4]
target = 2
```

Last occurrence:

```text
3
```

---

## Idea

When the target is found:

```python
ans = mid
```

continue searching to the right:

```python
low = mid + 1
```

---

## Code

```python
def last_occurrence(arr, target):

    low = 0
    high = len(arr) - 1

    ans = -1

    while low <= high:

        mid = low + (high - low) // 2

        if arr[mid] == target:

            ans = mid
            low = mid + 1

        elif arr[mid] < target:

            low = mid + 1

        else:

            high = mid - 1

    return ans
```

---

# 19. Count Occurrences

If:

```text
first occurrence = 1
last occurrence = 3
```

then:

```text
count = last - first + 1
```

---

## Code

```python
def count_occurrences(arr, target):

    first = first_occurrence(arr, target)

    if first == -1:
        return 0

    last = last_occurrence(arr, target)

    return last - first + 1
```

Example:

```python
arr = [1, 2, 2, 2, 3, 4]

print(count_occurrences(arr, 2))
```

Output:

```text
3
```

Complexity:

```text
Time  = O(log n)
Space = O(1)
```

---

# 20. Lower Bound

## Definition

**Lower Bound** means:

> Find the first index where `arr[index] >= target`.

---

## Example

```text
arr = [1, 2, 4, 4, 5, 7]
target = 4
```

Answer:

```text
2
```

because:

```text
arr[2] = 4
```

and it is the first value satisfying:

```text
value >= 4
```

---

## Another Example

```text
arr = [1, 2, 4, 4, 5, 7]
target = 3
```

Answer:

```text
2
```

because:

```text
arr[2] = 4
```

and:

```text
4 >= 3
```

---

## Code

```python
def lower_bound(arr, target):

    low = 0
    high = len(arr)

    while low < high:

        mid = low + (high - low) // 2

        if arr[mid] >= target:

            high = mid

        else:

            low = mid + 1

    return low
```

---

## Important

Notice:

```python
high = len(arr)
```

instead of:

```python
high = len(arr) - 1
```

because the answer can be equal to `len(arr)`.

Example:

```text
arr = [1, 2, 3]
target = 10
```

There is no element `>= 10`.

The insertion position is:

```text
3
```

---

# 21. Upper Bound

## Definition

**Upper Bound** means:

> Find the first index where `arr[index] > target`.

---

## Example

```text
arr = [1, 2, 4, 4, 5, 7]
target = 4
```

Answer:

```text
4
```

because:

```text
arr[4] = 5
```

and:

```text
5 > 4
```

---

## Code

```python
def upper_bound(arr, target):

    low = 0
    high = len(arr)

    while low < high:

        mid = low + (high - low) // 2

        if arr[mid] > target:

            high = mid

        else:

            low = mid + 1

    return low
```

---

# 22. Search Insert Position

Given:

```text
arr = [1, 3, 5, 6]
```

Find where `target` should be inserted while maintaining sorted order.

---

## Example 1

```text
target = 5
```

Answer:

```text
2
```

---

## Example 2

```text
target = 2
```

Answer:

```text
1
```

---

## Example 3

```text
target = 7
```

Answer:

```text
4
```

---

## Solution

Search Insert Position is essentially a **Lower Bound** problem.

```python
def search_insert(arr, target):

    low = 0
    high = len(arr)

    while low < high:

        mid = low + (high - low) // 2

        if arr[mid] >= target:

            high = mid

        else:

            low = mid + 1

    return low
```

---

# 23. Floor

## Definition

The **floor** of `x` is the largest value:

```text
<= x
```

---

## Example

```text
arr = [1, 3, 5, 7, 9]
x = 6
```

The values less than or equal to `6` are:

```text
1, 3, 5
```

Therefore:

```text
floor = 5
```

---

## Code

```python
def floor_value(arr, x):

    low = 0
    high = len(arr) - 1

    ans = None

    while low <= high:

        mid = low + (high - low) // 2

        if arr[mid] <= x:

            ans = arr[mid]
            low = mid + 1

        else:

            high = mid - 1

    return ans
```

---

# 24. Ceil

## Definition

The **ceil** of `x` is the smallest value:

```text
>= x
```

---

## Example

```text
arr = [1, 3, 5, 7, 9]
x = 6
```

Values greater than or equal to `6` are:

```text
7, 9
```

Therefore:

```text
ceil = 7
```

---

## Code

```python
def ceil_value(arr, x):

    low = 0
    high = len(arr) - 1

    ans = None

    while low <= high:

        mid = low + (high - low) // 2

        if arr[mid] >= x:

            ans = arr[mid]
            high = mid - 1

        else:

            low = mid + 1

    return ans
```

---

# 25. Descending Array

Binary Search can also work on a descending array.

Example:

```text
arr = [90, 80, 70, 60, 50, 40, 30]
```

Suppose:

```text
target = 50
```

---

## Important Difference

For ascending arrays:

```python
if arr[mid] < target:
    low = mid + 1
```

For descending arrays:

```python
if arr[mid] > target:
    low = mid + 1
```

The direction changes because the array is reversed.

---

## Code

```python
def binary_search_desc(arr, target):

    low = 0
    high = len(arr) - 1

    while low <= high:

        mid = low + (high - low) // 2

        if arr[mid] == target:

            return mid

        elif arr[mid] > target:

            low = mid + 1

        else:

            high = mid - 1

    return -1
```

---

# 26. Order-Agnostic Search

Sometimes the array can be either:

```text
Ascending
```

or:

```text
Descending
```

We can determine the order first.

---

## Example

Ascending:

```text
[1, 3, 5, 7, 9]
```

Descending:

```text
[9, 7, 5, 3, 1]
```

---

## Code

```python
def order_agnostic_search(arr, target):

    if not arr:
        return -1

    low = 0
    high = len(arr) - 1

    ascending = arr[low] <= arr[high]

    while low <= high:

        mid = low + (high - low) // 2

        if arr[mid] == target:
            return mid

        if ascending:

            if arr[mid] < target:

                low = mid + 1

            else:

                high = mid - 1

        else:

            if arr[mid] > target:

                low = mid + 1

            else:

                high = mid - 1

    return -1
```

---

# 27. Rotated Sorted Array

Consider:

```text
[4, 5, 6, 7, 0, 1, 2]
```

This is a rotated version of:

```text
[0, 1, 2, 4, 5, 6, 7]
```

---

## Key Observation

In a rotated sorted array, at least one half is normally sorted.

Example:

```text
[4, 5, 6, 7, 0, 1, 2]
 ↑        ↑        ↑
low      mid      high
```

Left half:

```text
[4, 5, 6, 7]
```

is sorted.

We can determine which half is sorted and check whether the target belongs to that half.

---

## Code

```python
def search_rotated(arr, target):

    low = 0
    high = len(arr) - 1

    while low <= high:

        mid = low + (high - low) // 2

        if arr[mid] == target:
            return mid

        # Left half is sorted
        if arr[low] <= arr[mid]:

            if arr[low] <= target < arr[mid]:

                high = mid - 1

            else:

                low = mid + 1

        # Right half is sorted
        else:

            if arr[mid] < target <= arr[high]:

                low = mid + 1

            else:

                high = mid - 1

    return -1
```

---

# 28. Rotated Array with Duplicates

Consider:

```text
[2, 5, 6, 0, 0, 1, 2]
```

Duplicates make it harder to determine which half is sorted.

For example:

```text
arr[low] == arr[mid] == arr[high]
```

In this situation, we cannot reliably determine the sorted half.

We can shrink the search space:

```python
low += 1
high -= 1
```

---

## Code

```python
def search_rotated_duplicates(arr, target):

    low = 0
    high = len(arr) - 1

    while low <= high:

        mid = low + (high - low) // 2

        if arr[mid] == target:
            return True

        # Ambiguous case
        if arr[low] == arr[mid] == arr[high]:

            low += 1
            high -= 1

            continue

        # Left half is sorted
        if arr[low] <= arr[mid]:

            if arr[low] <= target < arr[mid]:

                high = mid - 1

            else:

                low = mid + 1

        # Right half is sorted
        else:

            if arr[mid] < target <= arr[high]:

                low = mid + 1

            else:

                high = mid - 1

    return False
```

---

## Complexity

Average:

```text
O(log n)
```

Worst case with many duplicates:

```text
O(n)
```

---

# 29. Find Minimum in Rotated Array

Example:

```text
arr = [4, 5, 6, 7, 0, 1, 2]
```

Minimum:

```text
0
```

---

## Idea

Compare:

```python
arr[mid]
```

with:

```python
arr[high]
```

If:

```python
arr[mid] > arr[high]
```

the minimum must be to the right.

Therefore:

```python
low = mid + 1
```

Otherwise:

```python
high = mid
```

---

## Code

```python
def find_min(arr):

    low = 0
    high = len(arr) - 1

    while low < high:

        mid = low + (high - low) // 2

        if arr[mid] > arr[high]:

            low = mid + 1

        else:

            high = mid

    return arr[low]
```

Complexity:

```text
Time  = O(log n)
Space = O(1)
```

---

# 30. Find Peak Element

A peak element is an element that is greater than its neighboring elements.

Example:

```text
[1, 2, 3, 4, 2, 1]
```

Peak:

```text
4
```

---

## Idea

Compare:

```python
arr[mid]
```

with:

```python
arr[mid + 1]
```

If:

```python
arr[mid] < arr[mid + 1]
```

we are on an increasing slope.

Therefore, a peak exists to the right:

```python
low = mid + 1
```

Otherwise:

```python
high = mid
```

---

## Code

```python
def find_peak(arr):

    low = 0
    high = len(arr) - 1

    while low < high:

        mid = low + (high - low) // 2

        if arr[mid] < arr[mid + 1]:

            low = mid + 1

        else:

            high = mid

    return low
```

The returned value is the peak index.

Complexity:

```text
Time  = O(log n)
Space = O(1)
```

---

# 31. Mountain Array

A Mountain Array has the pattern:

```text
increasing → peak → decreasing
```

Example:

```text
[1, 3, 5, 7, 6, 4, 2]
```

Visual:

```text
1 → 3 → 5 → 7
             ↓
             6
             ↓
             4
             ↓
             2
```

Peak:

```text
7
```

---

## Finding the Peak

```python
def peak_index(arr):

    low = 0
    high = len(arr) - 1

    while low < high:

        mid = low + (high - low) // 2

        if arr[mid] < arr[mid + 1]:

            low = mid + 1

        else:

            high = mid

    return low
```

After finding the peak:

```text
left side  → ascending
right side → descending
```

We can perform Binary Search on both sides.

---

# 32. Binary Search on Answer

This is one of the most important advanced applications of Binary Search.

Binary Search does not always search an array.

It can search a **range of possible answers**.

---

## Example

Suppose a problem asks:

> Find the minimum capacity required to complete a task.

Possible answers:

```text
1, 2, 3, 4, 5, ..., 100
```

Suppose we have a function:

```python
is_possible(x)
```

that tells us whether answer `x` works.

Imagine:

```text
1  → False
2  → False
3  → False
4  → False
5  → True
6  → True
7  → True
8  → True
```

This is:

```text
False False False False True True True True
                         ↑
                    first valid answer
```

We can use Binary Search to find `5`.

---

# 33. Monotonic Predicate

A predicate is **monotonic** when its result changes in only one direction.

Example:

```text
False False False False True True True True
```

Once it becomes `True`, it stays `True`.

This allows us to use Binary Search.

---

## Another Pattern

We may have:

```text
True True True True False False False
```

Once it becomes `False`, it remains `False`.

We can search for the last `True`.

---

## Key Concept

The search space does not necessarily need to be a sorted array.

It only needs to have a property that allows us to safely eliminate half of the possible answers.

---

# 34. First True

Suppose:

```text
False False False True True True
                  ↑
              first True
```

We want the first position where the condition becomes `True`.

---

## Template

```python
def first_true(low, high):

    while low < high:

        mid = low + (high - low) // 2

        if is_possible(mid):

            high = mid

        else:

            low = mid + 1

    return low
```

---

# 35. Last True

Suppose:

```text
True True True False False False
         ↑
      last True
```

We want the last position where the condition is `True`.

---

## Template

```python
def last_true(low, high):

    ans = -1

    while low <= high:

        mid = low + (high - low) // 2

        if is_possible(mid):

            ans = mid
            low = mid + 1

        else:

            high = mid - 1

    return ans
```

---

# 36. Python `bisect` Module

Python provides the `bisect` module for binary-search-related operations.

```python
from bisect import bisect_left, bisect_right
```

---

## `bisect_left`

`bisect_left()` returns the first position where the target can be inserted while keeping the array sorted.

Example:

```python
from bisect import bisect_left

arr = [1, 2, 2, 2, 4]

print(bisect_left(arr, 2))
```

Output:

```text
1
```

This corresponds to:

```text
Lower Bound
```

---

## `bisect_right`

`bisect_right()` returns the position after the last occurrence of the target.

Example:

```python
from bisect import bisect_right

arr = [1, 2, 2, 2, 4]

print(bisect_right(arr, 2))
```

Output:

```text
4
```

This corresponds to:

```text
Upper Bound
```

---

# 37. Common Mistakes

## Mistake 1 — Forgetting Sorting

Standard Binary Search requires a sorted search space.

Wrong:

```python
arr = [5, 1, 8, 2, 9]
```

Correct:

```python
arr = [1, 2, 5, 8, 9]
```

---

## Mistake 2 — Wrong Loop Condition

Standard exact search generally uses:

```python
while low <= high:
```

---

## Mistake 3 — Wrong Boundary Update

Avoid:

```python
low = mid
```

and:

```python
high = mid
```

in the standard exact-search template.

Use:

```python
low = mid + 1
```

and:

```python
high = mid - 1
```

---

## Mistake 4 — Infinite Loop

Consider:

```text
low = 0
high = 1
mid = 0
```

If we write:

```python
low = mid
```

then:

```text
low = 0
high = 1
```

Nothing changes.

The loop may run forever.

Correct:

```python
low = mid + 1
```

---

## Mistake 5 — Wrong Comparison Direction

Ascending:

```python
if arr[mid] < target:
    low = mid + 1
```

Descending:

```python
if arr[mid] > target:
    low = mid + 1
```

---

## Mistake 6 — Stopping at the First Duplicate

For:

```text
[1, 2, 2, 2, 3]
```

normal Binary Search may return any `2`.

If you need the first:

```python
ans = mid
high = mid - 1
```

If you need the last:

```python
ans = mid
low = mid + 1
```

---

## Mistake 7 — Wrong Search Space

Exact Search:

```python
low = 0
high = len(arr) - 1
```

Lower/Upper Bound:

```python
low = 0
high = len(arr)
```

Binary Search on Answer:

```python
low = minimum_possible_answer
high = maximum_possible_answer
```

---

# 38. How to Identify Binary Search Problems

When reading a problem, look for specific clues.

---

## Clue 1 — Sorted Array

Words such as:

```text
sorted
increasing
decreasing
ascending
descending
```

Think:

```text
Binary Search
```

---

## Clue 2 — Searching for an Element

Words such as:

```text
find target
search target
find index
check if element exists
```

Think:

```text
Standard Binary Search
```

---

## Clue 3 — Duplicates

Words such as:

```text
first occurrence
last occurrence
number of occurrences
frequency
lower bound
upper bound
```

Think:

```text
Boundary Binary Search
```

---

## Clue 4 — Rotated Array

Words such as:

```text
rotated sorted array
sorted array rotated
```

Think:

```text
Rotated Binary Search
```

---

## Clue 5 — Optimization

Words such as:

```text
minimum possible
maximum possible
minimum capacity
minimum speed
minimum time
maximum distance
maximize minimum
minimize maximum
```

Think:

```text
Binary Search on Answer
```

---

# 39. Problem-Solving Checklist

Before implementing Binary Search, ask these questions.

---

## Step 1 — Is the search space sorted?

```text
Yes → Standard Binary Search may work.
No  → Look for a monotonic property.
```

---

## Step 2 — What am I searching for?

```text
Exact value?
First occurrence?
Last occurrence?
Lower Bound?
Upper Bound?
Minimum answer?
Maximum answer?
```

---

## Step 3 — What happens when `arr[mid]` is compared with the target?

Determine which half can safely be discarded.

---

## Step 4 — What is my search interval?

Common intervals:

```text
[low, high]
```

or:

```text
[low, high)
```

Be consistent.

---

## Step 5 — Does every iteration reduce the search space?

If not, the algorithm may enter an infinite loop.

---

## Step 6 — What should happen when I find a valid answer?

For exact search:

```python
return mid
```

For first occurrence:

```python
ans = mid
high = mid - 1
```

For last occurrence:

```python
ans = mid
low = mid + 1
```

For minimum valid answer:

```python
high = mid
```

For maximum valid answer:

```python
low = mid + 1
```

---

# 40. Important Templates

## Template 1 — Exact Search

```python
def binary_search(arr, target):

    low = 0
    high = len(arr) - 1

    while low <= high:

        mid = low + (high - low) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1
```

---

## Template 2 — First Occurrence

```python
def first_occurrence(arr, target):

    low = 0
    high = len(arr) - 1

    ans = -1

    while low <= high:

        mid = low + (high - low) // 2

        if arr[mid] == target:

            ans = mid
            high = mid - 1

        elif arr[mid] < target:

            low = mid + 1

        else:

            high = mid - 1

    return ans
```

---

## Template 3 — Last Occurrence

```python
def last_occurrence(arr, target):

    low = 0
    high = len(arr) - 1

    ans = -1

    while low <= high:

        mid = low + (high - low) // 2

        if arr[mid] == target:

            ans = mid
            low = mid + 1

        elif arr[mid] < target:

            low = mid + 1

        else:

            high = mid - 1

    return ans
```

---

## Template 4 — Lower Bound

```python
def lower_bound(arr, target):

    low = 0
    high = len(arr)

    while low < high:

        mid = low + (high - low) // 2

        if arr[mid] >= target:

            high = mid

        else:

            low = mid + 1

    return low
```

---

## Template 5 — Upper Bound

```python
def upper_bound(arr, target):

    low = 0
    high = len(arr)

    while low < high:

        mid = low + (high - low) // 2

        if arr[mid] > target:

            high = mid

        else:

            low = mid + 1

    return low
```

---

## Template 6 — First True

```python
def first_true(low, high):

    while low < high:

        mid = low + (high - low) // 2

        if is_possible(mid):

            high = mid

        else:

            low = mid + 1

    return low
```

---

## Template 7 — Last True

```python
def last_true(low, high):

    ans = -1

    while low <= high:

        mid = low + (high - low) // 2

        if is_possible(mid):

            ans = mid
            low = mid + 1

        else:

            high = mid - 1

    return ans
```

---

# 41. Practice Problems

A good progression for learning Binary Search is:

## Level 1 — Basic

1. Binary Search
2. Search Insert Position
3. Search in Sorted Array
4. Find Target in Array

---

## Level 2 — Duplicates and Boundaries

5. First Occurrence
6. Last Occurrence
7. Count Occurrences
8. Lower Bound
9. Upper Bound
10. Floor and Ceil

---

## Level 3 — Variations

11. Search in Descending Array
12. Order-Agnostic Binary Search
13. Find Peak Element
14. Find Minimum in Rotated Sorted Array
15. Search in Rotated Sorted Array

---

## Level 4 — Advanced

16. Search in Rotated Array with Duplicates
17. Find Peak in Mountain Array
18. Koko Eating Bananas
19. Capacity to Ship Packages
20. Allocate Minimum Pages
21. Aggressive Cows
22. Painter's Partition
23. Split Array Largest Sum
24. Minimize Maximum
25. Maximize Minimum

---

# 42. Quick Revision

## Standard Binary Search

```python
low = 0
high = len(arr) - 1

while low <= high:

    mid = low + (high - low) // 2

    if arr[mid] == target:
        return mid

    elif arr[mid] < target:
        low = mid + 1

    else:
        high = mid - 1

return -1
```

---

## First Occurrence

```python
if arr[mid] == target:
    ans = mid
    high = mid - 1
```

Search left.

---

## Last Occurrence

```python
if arr[mid] == target:
    ans = mid
    low = mid + 1
```

Search right.

---

## Lower Bound

```text
First index where:

arr[index] >= target
```

---

## Upper Bound

```text
First index where:

arr[index] > target
```

---

## Floor

```text
Largest value <= target
```

---

## Ceil

```text
Smallest value >= target
```

---

## Rotated Array

Remember:

```text
At least one half is sorted.
```

---

## Binary Search on Answer

Remember:

```text
Minimum/Maximum
+
Monotonic condition
=
Binary Search on Answer
```

---

# 43. Final Cheat Sheet

```text
                         BINARY SEARCH
                              |
              +---------------+---------------+
              |                               |
          SEARCH ARRAY                    SEARCH ANSWER
              |                               |
       +------+-------+                Monotonic Condition
       |              |                       |
    Exact          Boundary            +------+------+
    Search          Search             |             |
       |              |             First True    Last True
       |        +-----+-----+
       |        |           |
       |      First       Last
       |   Occurrence   Occurrence
       |        |           |
       |    high=mid-1   low=mid+1
       |
       +-----------------------------+
       |                             |
 Rotated Array                   Peak Element
       |
 Find Minimum
```

---

# Golden Rules

## Rule 1

```text
Sorted array → Think Binary Search
```

---

## Rule 2

```text
Every iteration must reduce the search space.
```

---

## Rule 3

For standard exact search:

```python
while low <= high:
```

---

## Rule 4

For standard ascending search:

```python
if arr[mid] < target:
    low = mid + 1
```

---

## Rule 5

For standard ascending search:

```python
if arr[mid] > target:
    high = mid - 1
```

---

## Rule 6

For first occurrence:

```python
ans = mid
high = mid - 1
```

---

## Rule 7

For last occurrence:

```python
ans = mid
low = mid + 1
```

---

## Rule 8

Lower Bound:

```text
First position where:

value >= target
```

---

## Rule 9

Upper Bound:

```text
First position where:

value > target
```

---

## Rule 10

For optimization problems:

```text
Minimum/Maximum
+
Monotonic condition
→
Binary Search on Answer
```

---

## Rule 11

Always ask:

```text
"What half can I safely eliminate?"
```

That is the fundamental question behind Binary Search.

---

# One-Line Definition

> **Binary Search repeatedly divides a sorted or monotonic search space into halves to efficiently find a target or boundary, typically in O(log n) time.**

---

# Final Complexity Summary

| Problem | Time | Extra Space |
|---|---:|---:|
| Standard Binary Search | O(log n) | O(1) |
| Recursive Binary Search | O(log n) | O(log n) |
| First Occurrence | O(log n) | O(1) |
| Last Occurrence | O(log n) | O(1) |
| Lower Bound | O(log n) | O(1) |
| Upper Bound | O(log n) | O(1) |
| Search Insert Position | O(log n) | O(1) |
| Floor | O(log n) | O(1) |
| Ceil | O(log n) | O(1) |
| Rotated Sorted Array | O(log n) | O(1) |
| Rotated Array with Duplicates | O(n) worst case | O(1) |
| Find Minimum in Rotated Array | O(log n) | O(1) |
| Find Peak Element | O(log n) | O(1) |
| Binary Search on Answer | O(log(range) × check) | Usually O(1) |

---

# End of Binary Search Notes