n = int(input())
arr = list(map(int, input().split()))[:n]


def selection_sort():
    global arr, n
    i = 0
    while i < n:
        minIndex = i
        for j in range(i+1, n):
            if arr[j] < arr[minIndex]:
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]
        i += 1

selection_sort()
print(arr)