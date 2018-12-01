# O(nlog(n))
def mergeSort(l):
    if len(l) <= 1:
        return l
    if len(l) == 2:
        if l[0] > l[1]:
            l[0], l[1] = l[1], l[0]
        return l
    else:
        middle = int(len(l) / 2)
        return merge(mergeSort(l[:middle + 1]), mergeSort(l[middle + 1:]))

def merge(left, right):
    merged = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged += left[i:] + right[j:]
    return merged


print(mergeSort([38, 27, 43, 3, 9, 82, 10]))
