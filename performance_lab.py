# 🔍 Problem 1: Find Most Frequent Element

def most_frequent(numbers):
    from collections import Counter
    count = Counter(numbers)
    return max(count, key=count.get)

# Test cases
print(most_frequent([1, 3, 2, 3, 4, 1, 3]))  # → 3
print(most_frequent([5, 5, 6, 6]))          # → 5 or 6

"""
Time and Space Analysis for problem 1:
- Best-case: O(n)
- Worst-case: O(n)
- Average-case: O(n)
- Space complexity: O(n)
- Why this approach? Makes it easier and quicker. 
- Could it be optimized? If there wasn't anything to import, 
then using a regular directory would work. It's about the same. 
"""


# 🔍 Problem 2: Remove Duplicates While Preserving Order

def remove_duplicates(nums):
    seen = set()
    result = []
    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result

# Test cases
print(remove_duplicates([4, 5, 4, 6, 5, 7]))  # → [4, 5, 6, 7]

"""
Time and Space Analysis for problem 2:
- Best-case: O(n)
- Worst-case: O(n)
- Average-case: O(n)
- Space complexity: O(n)
- Why this approach? If something is seen then it makes seeing it 
simple and fast. 
- Could it be optimized? No it's good as is. 
"""


# 🔍 Problem 3: Return All Pairs That Sum to Target

def find_pairs(nums, target):
    seen = set()
    pairs = set()
    for num in nums:
        complement = target - num
        if complement in seen:
            pairs.add(tuple(sorted((num, complement))))
        seen.add(num)
    return list(pairs)

# Test cases
print(find_pairs([1, 2, 3, 4], 5))  # → [(1, 4), (2, 3)]

"""
Time and Space Analysis for problem 3:
- Best-case: O(n)
- Worst-case: O(n)
- Average-case: O(n)
- Space complexity: O(n)
- Why this approach? It quickly avoids nested loops. 
- Could it be optimized? If you wanted a different pair 
format, then take out the sorting step. 
"""


# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)

def add_n_items(n):
    capacity = 1
    size = 0
    data = [None] * capacity
    for i in range(n):
        if size == capacity:
            print(f"Resizing from {capacity} to {capacity * 2}")
            capacity *= 2
            new_data = [None] * capacity
            for j in range(size):
                new_data[j] = data[j]
            data = new_data
        data[size] = i
        size += 1
    print("Final list:", data[:size])

# Test case
add_n_items(6)

"""
Time and Space Analysis for problem 4:
- When do resizes happen? When size == capacity.
- Worst-case for a single append: O(n) during resize.
- Amortized time per append: O(1)
- Space complexity: O(n)
- Why does doubling reduce the cost overall? Copying steps 
takes time and it spreads it out more evenly so that they don't happen as often. 
"""


# 🔍 Problem 5: Compute Running Totals

def running_total(nums):
    result = []
    total = 0
    for num in nums:
        total += num
        result.append(total)
    return result

# Test cases
print(running_total([1, 2, 3, 4]))  # → [1, 3, 6, 10]

"""
Time and Space Analysis for problem 5:
- Best-case: O(n)
- Worst-case: O(n)
- Average-case: O(n)
- Space complexity: O(n)
- Why this approach? It's simple and straightforward. 
- Could it be optimized? No it's good as is.
"""

