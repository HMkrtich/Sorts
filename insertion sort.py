def insertion_sort(a):
    n = len(a)
    for i in range(n):
        t = a[i]
        j = i - 1
        while j >= 0 and a[j] > t:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = t

def selection_sort(a):
    n = len(a)
    for i in range(n - 1):
        min_index = i
        min_val = a[i]
        for j in range(i + 1, n):
            if a[j] < min_val:
                min_val = a[j]
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]

def bubble_sort(a):
    n = len(a)
    for i in range(n - 1, 0, -1):   # n - 1 .. 1
        for j in range(i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]


def merge(a, b, c):
    i = j = 0  # index into a, b

    for k in range(len(c)):
        if j == len(b):  # no more elements available from b
            c[k] = a[i]  # so we take a[i]
            i += 1
        elif i == len(a):  # no more elements available from a
            c[k] = b[j]  # so we take b[j]
            j += 1
        elif a[i] < b[j]:
            c[k] = a[i]  # take a[i]
            i += 1
        else:
            c[k] = b[j]  # take b[j]
            j += 1


def merge_sort(a):
    if len(a) < 2:
        return

    mid = len(a) // 2

    left = a[:mid]  # copy of left half of array
    right = a[mid:]  # copy of right half

    merge_sort(left)
    merge_sort(right)

    merge(left, right, a)

def partition(a, lo, hi):
    pivot = a[hi - 1]
    k = lo
    for i in range(lo, hi):
        if a[i] <= pivot:     # a[i] belongs in the left partition
            a[k], a[i] = a[i], a[k]
            k += 1
    k -= 1
    return k

# Sort the elements a[lo:hi].
def quicksort(a, lo, hi):
    if hi - lo <= 1:
        return

    k = partition(a, lo, hi)
    quicksort(a, lo, k)  # a[lo], a[lo + 1] ... a[k - 1]
    quicksort(a, k + 1, hi)
