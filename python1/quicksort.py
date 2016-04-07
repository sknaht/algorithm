
def quicksort(start, end, array):
    if start >= end:
        return
    pivot = array[end]
    s, e = start, end
    while s < e:
        while s < e and array[s] <= pivot:
            s += 1
        if s >= e:
            break
        array[e] = array[s]
        e -= 1
        while s < e and array[e] >= pivot:
            e -= 1
        if s >= e:
            break
        array[s] = array[e]
        s += 1
    array[e] = pivot
    quicksort(start, e -1, array)
    quicksort(e + 1, end, array)


def three_way_quick_sort(a, lo, hi):
    if lo >= hi:
        return
    lt, gt, i, key = lo, hi, lo, a[lo]
    while i <= gt:
        if a[i] < key:
            a[i], a[lt] = a[lt], a[i]
            lt += 1
            i += 1
        elif a[i] > key:
            a[i], a[gt] = a[gt], a[i]
            gt -= 1
        else:
            i += 1
    three_way_quick_sort(a, lo, lt - 1)
    three_way_quick_sort(a, gt + 1, hi)


a = [6, 5, 1, 8, 9, 7, 6, 2, 6, 5, 8, 1, 5, 1, 6]
three_way_quick_sort(a, 0, len(a) - 1)
print a