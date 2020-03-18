# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    for i in range(0, elements):
        if len(arrA) == 0:
            merged_arr[i] = arrB[0]
            del arrB[0]
        elif len(arrB) == 0:
            merged_arr[i] = arrA[0]
            del arrA[0]
        elif arrA[0] < arrB[0]:
            merged_arr[i] = arrA[0]
            del arrA[0]
        else:
            merged_arr[i] = arrB[0]
            del arrB[0]

    return merged_arr


arr1 = [1, 5, 8, 9, 11, 12, 13, 17]
arr2 = []
arr3 = [2]
arr4 = [0, 1, 2, 3, 4, 5, 20]

print(merge(arr1[:], arr4[:]), "merge1")
print(merge(arr1[:], arr2[:]), "merge2")
print(merge(arr1[:], arr3[:]), "merge3")
print(merge(arr1[:], arr1[:]), "merge4")

# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):    # TO-DO
   # CHECK IF ARRAY HAS MORE THAN ONE ELEMENT INSIDE
    if len(arr) > 1:
        # SPLIT THE ARRAY
        split = len(arr) // 2
        first_half = arr[:split]
        second_half = arr[split:]
        # RECURSIVELY CONTINUE TO SPLIT THE ARRAY
        # MERGE ALL SPLIT ARRAYS BACK AS SORTED
        arr = merge(merge_sort(first_half), merge_sort(second_half))

    return arr


print(merge_sort([2, 9, 5, 4]))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
