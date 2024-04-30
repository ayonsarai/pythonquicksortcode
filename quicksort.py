# Sarai Ayon
# 4/29/24
# CS240 Data Structures and Algorithms
# QuickSort Algorithm

def quicksort(arr, low, high):
    if low < high:
        # Partition the array and get the pivot index
        pivot_index = partition(arr, low, high)
        
        # Recursively call quicksort on the left and right subarrays
        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)

# Function to partition the array
def partition(arr, low, high):
    # Choose the rightmost element as the pivot
    pivot = arr[high]
    
    # Initialize the pivot index
    pivot_index = low
    
    # Iterate through the array
    for i in range(low, high):
        # If the current element is smaller than or equal to the pivot,
        # swap it with the element at the pivot index and increment the pivot index
        if arr[i] <= pivot:
            arr[i], arr[pivot_index] = arr[pivot_index], arr[i]
            pivot_index += 1
    
    # Swap the pivot element with the element at the pivot index
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    
    # Return the pivot index
    return pivot_index

# Test the QuickSort algorithm
with open('numbers-4.txt', 'r') as file:
    arr = [int(line) for line in file]
    
quicksort(arr, 0, len(arr) - 1)

# Find the position of 90262
position = arr.index(90262)

print(f"The position of 90262 is {position}")