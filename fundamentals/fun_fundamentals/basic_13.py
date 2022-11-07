# print 1 to 255:
def one_to_255(x):
    for x in range(1, 256):
        print(x)


one_to_255(1)


# Find and Print Max
# Given a list of integers, find the highest number and print it


def find_and_print_max(nums):
    max = nums[0]
    for i in range(1, len(nums)):
        if nums[i] > max:
            max = nums[i]
    return max


print(find_and_print_max([5, 7, 4, 3, 6, 8]))
# iterate through all values at nums
# at each value check if that number is greater than max

# Greater than y
# given a list of integers, and a number, y, calculate the number
# of integers in the list that are greater than years


def greater_than_y(nums, y):
    count = 0
    for num in nums:
        if num > y:
            count += 1

    return count


print(greater_than_y([8, 6, 7, 5, 3, 0, 9], 6))


# min/max/avg
def max_min_avg(nums):
    max = nums[0]
    min = nums[0]
    sum = nums[0]

    for i in range(1, len(nums)):
        if nums[i] > max:
            max = nums[i]
        if nums[i] < min:
            min = nums[i]

        sum += nums[i]

    print(f"Max:{max}")
    print(f"Min: {min}")
    print(f"Avg {sum / len(nums)}")


max_min_avg([8, 6, 7, 5, 3, 0, 9])


for i in range(0, 151):
    print(i)

for i in range(5, 1001, 5):
    print(i)

for i in range(1, 101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

sum = 0
for i in range(1, 500001, 2):
    sum += i  # this adds, sum = sum+i, everytime it loops it adds
print(sum)

for i in range(2018, -1, -4):
    print(i)

low = 2
high = 9
mult = 3

for i in range(2, 10):
    if i % 3 == 0:
        print(i)


# functions II
# 1
def countdown(num):
    holder = []
    for i in range(num, -1, -1):
        holder.append(i)
    return holder


print(countdown(5))

# 2


def print_and_return(list):
    print(list[0])
    return list[1]


# 3
print(print_and_return([1, 2]))


def first_plus_length(list):
    return list[0] + len(list)


print(first_plus_length([15, 2, 3, 4, 5]))

# 4


def values_greater_than_second(list):
    if len(list) < 2:
        return False
    new_list = []
    for i in range(0, len(list)):
        if list[i] > list[1]:
            new_list.append(list[i])
    print(len(new_list))
    return new_list

# 5


def length_and_value(size, value):
    new_list = []
    for i in range(0, size):
        new_list.append(value)
    return new_list


print(length_and_value(4, 7))

