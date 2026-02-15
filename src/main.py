# %%
import time

# %%
def selection_sort(arr):
    # Selection Sort Algorithm
    # The Algorithm divides the input list into two parts
    # 1. A sorted sublist of items which is built up from the left to right
    # 2. A sublist of the remaining unsorted items

    # It works by repeatedly finding the minimum element from the unsorted part
    # and putting it at the beginning


    n = len(arr)

    # Traverse through all array elements
    # We loop up to n-1 because the last element will naturally be sorted
    for i in range(n):
        # Assume the current position is i is the minimum
        min_idx = i

        # Visualize the start of a new pass
        print(f"----- Pass {i +1}-----")
        print(f"Current state: {arr}")
        print(f"Scanning for the smallest element starting from index {i} (value: {arr[i]})")


        # Traverse the unsorted part of the array to find the actual minimum
        for j in range(i + 1, n):
            # Comparison: Is the element at j smaller than our current minimum
            if arr[j] < arr[min_idx]:
                # Update min_idx if a smaller element is found
                min_idx = j
                print(f"New minimum found: {arr[min_idx]} at index {j}")

        # Swap the found minimum element with first element of the unsorted part
        # Only swap if the minimum is not alreay at the current position i
        if min_idx != 1:
            print(f"Swapping index {i} ({arr[i]}) with index {min_idx} ({arr[min_idx]})")
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        else:
            print(f"Index {i} is alredy the minimum for this pass. No swap needed")

        # Show visualization of the current array state
        visualize_array(arr,i)

    return arr

# %%
def visualize_array(arr, sorted_up_to):
    # Creates a bar-chart style visualization in the console
    # "#" represents an element's value
    # "|" marks the boundary of the sorted portion

    print("Visualization")
    max_val = max(arr) if arr else 0
    for val in arr:
        bar = "#" * val
        print(f"{val:2}: {bar}")

    # Print a divider to show what is sorted
    boundary = "---" * (sorted_up_to + 1)
    print(f"Sorted boundary: {boundary} | (elements to the left are sorted)")
    time.sleep(0.5) # Pause briefly for effect

# %%
def run_example():
    # Runs various test cases to demonstrate the algorithm

    print("==========================================")
    print("   SELECTION SORT PYTHON DEMONSTRATION    ")
    print("==========================================")

    # Example 1: Standard Unsorted List
    test_1 = [29,10,24,37,13]
    print("EXAMPLE 1: Standard List")
    print(f"Initial: {test_1}")
    result_1 = selection_sort(test_1)
    print(f"Final Sorted Result: {result_1}")

    # Illustration of Logic for a small set [5, 2, 8]
    # 1. Start: [5, 2, 8]. i=0. Min is 5. Compare with 2. New Min=2. Compare with 8. Swap 5 and 2.
    # 2. State: [2, 5, 8]. i=1. Min is 5. Compare with 8. No swap.
    # 3. State: [2, 5, 8]. i=2. Last element. Done.

    # Example 2: List with duplicates
    test_2 = [3,1,2,1,3]
    print("EXAMPLE 2: List with duplicates")
    result_2 = selection_sort(test_1)
    print(f"Final Sorted Result: {result_2}")

    # Example 3: Already sorted list
    test_3 = [1,2,3,4]
    print("EXAMPLE 3: Already Sorted List")
    result_3 = selection_sort(test_3)
    print(f"Final Sorted List: {result_3}")

# %%
if __name__ == "__main__":
    run_example()


