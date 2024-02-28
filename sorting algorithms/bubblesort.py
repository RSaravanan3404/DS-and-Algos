n = int(input())
arr = list(map(int, input().split()))[:n]

def bubble_sort() -> None:
    global arr, n
    comparisons, total_swaps = 0, 0
    for i in range(n):
        swaps = 0
        for j in range(0, n-i-1):
            comparisons += 1
            if arr[j] > arr[j+1]:
                swaps += 1
                arr[j+1], arr[j] = arr[j], arr[j+1]
        if swaps:
            total_swaps += swaps
        else:
            break

    print("No of comparisons, ", comparisons)
    print("No of swaps, ", total_swaps)
    print(arr)

bubble_sort()


"""
arr = 5 6 4 3 2 7

i = 0, 
    j = 0 , j + 1 
        5 6 4 3 2 7
    j = 1
        5 4 6 3 2 7
    ...
        5 4 3 2 6 7
i = 1
    j loop
        5 3 4 2 6 7
        5 3 2 4 6 7
i = 2
    j loop 
        3 5 4 2 6 7
        3 4 5 2 6 7
        3 4 2 5 6 7
i = 3
    j loop
        3 4 5 2 6 7
        3 4 2 5 6 7
i = 4
    j loop 
        3 2 4 5 6 7 
i = 5
    j loop
        2 3 4 5 6 7 

"""

