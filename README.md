<h1 align="center">Bubble Sort</h1>

## Overview

**Bubble Sort** is one of the simplest sorting algorithms.
It repeatedly compares adjacent elements and swaps them if they are in the wrong order.

With each pass through the list, the largest unsorted element “bubbles up” to its correct position at the end.

It is known for being:

* ✅ Very easy to understand and implement
* ✅ Useful for teaching sorting concepts
* ❌ Inefficient for large datasets
* ❌ Slow compared to modern algorithms

<a href="/src/main.py">Check out for source code</a>

---

## ⚙️ How Bubble Sort Works

1. Start from the beginning of the list
2. Compare each pair of adjacent elements
3. Swap them if they are out of order
4. Continue until the end of the list
5. Repeat passes until no swaps occur

---

### Example Walkthrough

Sort this list:

```
[5, 3, 8, 4, 2]
```

**Pass 1**

```
[5, 3, 8, 4, 2]
→ swap 5 & 3 → [3, 5, 8, 4, 2]
→ swap 8 & 4 → [3, 5, 4, 8, 2]
→ swap 8 & 2 → [3, 5, 4, 2, 8]
```

**Pass 2**

```
[3, 5, 4, 2, 8]
→ swap 5 & 4 → [3, 4, 5, 2, 8]
→ swap 5 & 2 → [3, 4, 2, 5, 8]
```

**Pass 3**

```
[3, 4, 2, 5, 8]
→ swap 4 & 2 → [3, 2, 4, 5, 8]
```

**Pass 4**

```
[3, 2, 4, 5, 8]
→ swap 3 & 2 → [2, 3, 4, 5, 8]
```

Sorted result:

```
[2, 3, 4, 5, 8]
```

---

## ⏱️ Time & Space Complexity

| Case                       | Time Complexity |
| -------------------------- | --------------- |
| Best Case (already sorted) | O(n)            |
| Average Case               | O(n²)           |
| Worst Case                 | O(n²)           |

**Space Complexity:** O(1) (in-place)

---

## 🧠 Python Implementation

```python
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # Stop early if no swaps happened
        if not swapped:
            break

    return arr


# Example usage
numbers = [5, 3, 8, 4, 2]
print(bubble_sort(numbers))
# Output: [2, 3, 4, 5, 8]
```

---

## 🧪 Example Runs

### Example 1

Input:

```
[9, 1, 6, 7, 3]
```

Output:

```
[1, 3, 6, 7, 9]
```

### Example 2

Input:

```
[4, 2, 2, 8, 1]
```

Output:

```
[1, 2, 2, 4, 8]
```

---

## 👍 Advantages

* Extremely simple to implement
* Requires no extra memory
* Detects already sorted arrays quickly (with optimization)
* Useful for educational purposes

---

## 👎 Disadvantages

* Very slow for large datasets
* Performs many unnecessary comparisons
* Inefficient compared to O(n log n) algorithms

---

## 📌 When to Use Bubble Sort

Use Bubble Sort when:

* Teaching sorting fundamentals
* Working with very small lists
* Simplicity matters more than performance

---

## 🏁 Summary

Bubble Sort is one of the most basic sorting algorithms. While it is rarely used in production systems due to its inefficiency, it remains valuable for learning how sorting works and understanding algorithm complexity.
