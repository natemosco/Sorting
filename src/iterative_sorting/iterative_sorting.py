# TO-DO: Complete the selection_sort() function below

arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]


def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(cur_index, len(arr)):
            if arr[j] <= arr[smallest_index]:
                smallest_index = j
        # TO-DO: swap
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]
    return arr


print(selection_sort(arr1))

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    counter = 0
    is_sorted = len(arr)-1
    end_of_array = len(arr) - 1
    while is_sorted != counter:
                counter = 0
        for i in range(0, end_of_array):
            if arr[i] <= arr[i+1]:
                counter += 1
            elif arr[i] > arr[i+1]:
                arr[i] = arr[i+1]
    return arr


print(bubble_sort(arr1))

# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr
