def maxArea(height):
    left = 0
    right = len(height) -1
    maxVolume = right * min(height[right], height[left])

    while left < right:
        w = right - left 
        h = min(height[right], height[left])

        if w * h > maxVolume:
            maxVolume = w*h
        
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
        
    return maxVolume

print(maxArea([1,8,6,2,5,4,8,3,7]), 49)