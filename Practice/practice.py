import numpy as np




# numbers_array = np.array([10,9,8,7,6])
# print("List: ", numbers)

# print("Array: ", numbers_array)


# new_list = []
# for x in numbers:
#     new_list.append(x * 2)
# print("List multiplied by 2: ", new_list)


# np_numbers = np.array([1,2,3,4,5])
# result = np_numbers * 2
# print("NumPy array multiplied by 2: ", result)



# data = np.array([70,85,90,60,75])

# print("Mean: ", data.mean())
# print("Sum: ", data.sum())
# print("Max: ", data.max())
# print("Min: ", data.min())
# print("Standard Deviation: ", data.std())


# marks = np.array([70, 85, 90, 60, 75])
# bonus_marks = marks + 5
# print("Marks after eid bonus: ", bonus_marks)








# average = sum(numbers) / len(numbers)

# maximum = max(numbers)

# minimum = min(numbers)

# print("Average is: ", average)

# print("Maximum is: ", maximum)

# print("Minimum is: ", minimum)



# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

import time
size = 10**6
numbers = list(range(size))


# loop sum
start = time.time()
total = 0
for n in numbers:
    total += n
end = time.time()
print("Loop sum: ", total, "Time: ", end - start)


# numpy array sum
numbers_array = np.array(numbers)

start = time.time()
total_np = numbers_array.sum()
end = time.time()
print("NumPy sum: ", total_np, "Time: ", end - start)

# temperature = np.array([])