def merge_sort(A):
    n = len(A)
    if n < 2:
        return
    mid = n/2
    left, right = A[0:mid], A[mid:n] 
    merge_sort(left)
    merge_sort(right)
    merge(A, left, right)

def merge(A, left, right):
    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            A[k] = left[i]
            i += 1
        else:
            A[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        A[k] = left[i]
        k += 1
        i += 1
    while j < len(right):
        A[k] = right[j]
        j += 1
        k += 1

if __name__ == '__main__':
    A = [4, 3, 1, 2, -4, 0, 0, 19, 10]
    merge_sort(A)
    print(A)