n = int(input("Arr size: "))
arr = sorted(list(map(int, input().split()))[:n])
k = int(input("Search Element: "))
mid = n // 2

def binary_search(low, mid, high, k):
    global arr
    while low < high:
        mid = (low + high) // 2

        if arr[mid] == k:
             return mid
        elif arr[mid] < k:
            low = mid + 1
        else:
            high = mid - 1

    return -1

ind = binary_search(0, mid, n, k)
if ind > -1:
    print(k, "is fond in the index ", ind)
else:
    print(k, " not found in the array.")