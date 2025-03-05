""" MERGE SORT 
EVENTUALLY SPLITS THE ARRAY INTO TWO PARTS AND AT THE SAME TIME INDEX ARE ACCESSED ON BOTH THE ELEMENTS. COMPARED AND THE LEAST VALUE IS STORES IN THE RESULTANT ARRAY AFTER A COMPARISON
IT IS ALSO CALLED THE DIVIDE AND CONQUER TECHNIQUE 
IT CAN BE BROADLY CLASSIFIED INTO THREE STEPS :
    1. SPLIT FIRST HALF ARRAY
    2. SPLIT SECONF HALF ARRAY
    3. MERGE THE TWO ARRAY
"""
def mergeSort(arr):
    print("[173] Array : ", arr)
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    leftHalf = arr[:mid]
    print("[179] Left half : ", leftHalf)
    rightHalf = arr[mid:]
    print("[181] Right Half : ", rightHalf)
    sortedLeft = mergeSort(leftHalf)
    print("[183] Left Array : ", sortedLeft)
    sortedRight = mergeSort(rightHalf)
    print("[185] Right Array : ", sortedRight)
    ArrReturn = merge(sortedLeft, sortedRight)
    print("[187] merged Array : ", ArrReturn)
    return ArrReturn

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

unsortedArr = [3, 7, 6, -10, 15, 23.5, 55, -13, 0]
sortedArr = mergeSort(unsortedArr)
print("Sorted array :", sortedArr)
