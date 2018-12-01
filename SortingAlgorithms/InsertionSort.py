# O(n^2)
def insertionSort(l):
    i = 0
    while i < len(l):
        j = i
        while j > 0 and l[j - 1] > j[j]:
            l[j - 1], l[j] = l[j], l[j - 1]
            j -= 1
        i += 1

print(insertionSort([6, 5, 3, 1, 8, 7, 2, 4]))
