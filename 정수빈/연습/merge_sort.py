def count_anti_inversions(arr):
    # implement this
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    left_merge, left_count = count_anti_inversions(left)
    right_merge, right_count = count_anti_inversions(right)
    r, c = merge_count_anti_inversions(left_merge, right_merge)
    
    return r, c + left_count + right_count

def merge_count_anti_inversions(left, right):
    i, j = 0, 0
    count = 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(right[j])
            count += len(left) - i
            j += 1
        else:
            result.append(left[i])
            i += 1
    
    result.extend(right[j:])
    result.extend(left[i:])
    
    return result, count

# Testing the function
test_array = [2, 4, 1, 3, 5]
sorted_l, inv_count = count_anti_inversions(test_array)
print("sorted ", sorted_l)
print(f'Number of anti-inversions in {test_array} is {inv_count}')  # Expected Output: 7