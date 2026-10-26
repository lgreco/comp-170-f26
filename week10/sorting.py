arr = [9,8,6,4,5]
n = len(arr)

print(f"\nArray before sorting: {arr}")

# Look at progressively smaller slices
for i in range(n):
    # Find the smallest number in the slide
    # from i to the end of the array. Assume
    # that the first element of the slice is
    # the smallest
    smallest_idx = i  # beginning of slice
    for j in range(i+1,n):
        if arr[j] < arr[smallest_idx]:
            smallest_idx = j
    # Now smallest_idx points to the smallest element of
    # the slide arr[i:n]. Bring it to the front of that
    # slide -- the front is at [i]
    temporary = arr[smallest_idx]
    arr[smallest_idx] = arr[i]
    arr[i] = temporary

print(f"Array after sorting: {arr}\n")
