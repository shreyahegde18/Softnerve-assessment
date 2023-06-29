def leader(arr):
    leaders = []
    max_element = float('-inf')

    # Iterate through the array from right to left
    for i in range(len(arr)-1, -1, -1):
        if arr[i] > max_element:
            leaders.append(arr[i])
            max_element = arr[i]

    leaders.reverse()  # Reverse the list to restore the original order
    return leaders
# test case
arr = [7, 10, 4, 10, 6, 5, 2]
result = leader(arr)
print(result)  #Output:[10, 6, 5, 2]
