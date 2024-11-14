import random
import string

# TODO: Define a merge_sort function that takes data to sort and returns the sorted data

def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]
    left_merge = merge_sort(left)
    right_merge = merge_sort(right)
    
    return merge(left_merge, right_merge)
    

    # TODO: If the alphanumeric array has one or no elements, it is already sorted. So, return the array immediately.

    # TODO: Next, divide the array into two equal parts.

    # TODO: Sort the left and right parts of the array with the merge_sort function.

    # TODO: After sorting both halves of the array, combine them together using the merge function.

# TODO: In the merge function, take two sorted arrays as inputs

    # TODO: While both arrays have elements in them, compare the first element of each.
    # If the first element of the left array is smaller, add it to the result array and remove it from the left array.
    # Otherwise, do the same with the right array.

    # TODO: If the left or right array still has elements, add them to the result array.
def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result
# TODO: Generate some random data to sort
random_data = [random.choice(string.ascii_letters) for _ in range(20)]
# TODO: Print the original data
print(random_data)
# TODO: Use your merge_sort function to sort the data
print(merge_sort(random_data))
# TODO: Print the sorted data