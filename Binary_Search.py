import random
import time

def binary_search(arr, key):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1

    return -1

file_name = 'random_numbers.txt'
with open(file_name, 'r') as file:
    alist = [int(line.strip()) for line in file]

alist.sort()  # Binary search requires a sorted list.

key = int(input('Enter the number to search for: '))

start_time = time.time()
index = binary_search(alist, key)
end_time = time.time()

if index < 0:
    print('{} not found'.format(key))
else:
    print('{} was found at index {}.'.format(key, index))

elapsed_time = (end_time - start_time) * 1_000_000
print(f"Time taken: {elapsed_time:.2f} seconds")
