# O(n^2)
def bubble_sort(l):
    while True:
        for i in range(len(l)):
            j = i
            if j < len(l) - 1 and l[j] > l[j + 1]:
                while l[j] > l[j + 1]:
                    l[j], l[j + 1] = l[j + 1], l[j]
                    j += 1
                break
        if i == len(l) - 1:
            break
    return l


print(bubble_sort([5, 1, 4, 2, 8]))
