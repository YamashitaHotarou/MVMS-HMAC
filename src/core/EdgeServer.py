import random
class EdgeServer:
    def __init__(self, esID, replicas):
        self.esID=esID
        self.replicas=replicas #这是一个字典，索引为avID
        self.reliableScore = 0


def partition(arr, left, right, pivot_index):
    pivot = arr[pivot_index]
    # Change pivot element with the last one.
    arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
    store_index = left

    for i in range(left, right):
        if arr[i].reliableScore < pivot.reliableScore:
            arr[store_index], arr[i] = arr[i], arr[store_index]
            store_index += 1

    # Put the pivot element to the final position.
    arr[right], arr[store_index] = arr[store_index], arr[right]
    return store_index

def quickSelect(arr, left, right, k):
    if left == right:
        return arr[left]

    pivot = random.randint(left, right)
    pivot_index = partition(arr, left, right, pivot)

    # According to returned pivot_index
    if pivot_index == k:
        return arr[k]
    elif pivot_index > k:
        return quickSelect(arr, left, pivot_index-1, k)
    else:
        return quickSelect(arr, pivot_index+1, right, k)


def getMinNRS(RS, n):
    if n > len(RS) or n < 1:
        return []
    quickSelect(RS, 0, len(RS)-1, n-1)
    return RS[:n]

def getMaxNRS(RS, n):
    if n > len(RS) or n < 1:
        return []
    quickSelect(RS, 0, len(RS) - 1, len(RS) - n)
    return RS[-n:]