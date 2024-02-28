n = int(input())
arr = list(map(int, input().split()))[:n]


def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        # sorting the first half
        mergeSort(left)
        # sorting the second half
        mergeSort(right)

        i, j, k, ll, rl = 0, 0, 0, len(left), len(right)
        while i < ll and j < rl:
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        # to check out is there any elements missed out in the left array
        while i < ll:
            arr[k] = left[i]
            i += 1
            k += 1
        # to check out is there any elements missed out in the right array
        while j < rl:
            arr[k] = right[j]
            j += 1
            k += 1

        
print("Array Before sorting", arr)
mergeSort(arr)
print("Array After sorting", arr)