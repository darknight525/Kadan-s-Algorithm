import array as arr

arr = [1,3,-4,5,-6,3,-2,4,6,5,-8]

current_sum = 0
max_sum = arr[0]

for x in arr:
    current_sum += x
    max_sum = max(max_sum , current_sum)

    if current_sum < 0:
        current_sum = 0


print(max_sum)
