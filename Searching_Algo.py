import random
import time

num_numbers = 50000
with open('random_numbers.txt', 'w') as file:
    for _ in range(num_numbers):
        random_number = random.randint(1, 50000)
        file.write(str(random_number) + '\n')
def linear_search(alist, key):

    for i in range(len(alist)):
        if alist[i] == key:
            return i
    return -1

file_name = 'random_numbers.txt'
with open(file_name, 'r') as file:
    alist = [int(line.strip()) for line in file]

key = int(input('Enter the number to search for: '))

index = linear_search(alist, key)

if index < 0:
    print('{} not found'.format(key))
else:
    print('{} was found at index {}.'.format(key, index))

start_time = time.time()
index = linear_search(alist, key)
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Time taken: {elapsed_time:.6f} seconds")