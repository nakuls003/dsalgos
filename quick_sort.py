import random

def quicksort(A, start, end):
    if start < end:
        p_index = randomized_partition(A, start, end)
        quicksort(A, start, p_index-1)
        quicksort(A, p_index+1, end)

def randomized_partition(A, start, end):
    p_index = random.randint(start, end)
    A[p_index], A[end] = A[end], A[p_index]
    return partition(A, start, end)

def partition(A, start, end):
    pivot = A[end]
    p_index = start
    for i in range(start, end):
        if A[i] <= pivot:
            A[i], A[p_index] = A[p_index], A[i]
            p_index += 1
    A[p_index], A[end] = A[end], A[p_index]
    return p_index

if __name__ == '__main__':
    A = [-1, -4, 3, 0, 5, 8, 8, 2, 1, 1, 10]
    # A = [1, 1]
    quicksort(A, 0, len(A)-1)
    print(A)