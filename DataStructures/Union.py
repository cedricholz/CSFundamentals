def find_set(x):
    for sub in sets:
        if x in sub:
            return sub


def union(i, j):
    subset_i = find_set(i)
    subset_j = find_set(j)
    if subset_i != subset_j:
        sets.add(frozenset.union(subset_i, subset_j))
        sets.remove(subset_i)
        sets.remove(subset_j)


M = [[1, 1, 0],
     [1, 1, 1],
     [0, 1, 1]]

sets = set([frozenset([x]) for x in range(max(len(M), len(M[0])))])

for i in range(len(M)):
    for j in range(len(M[0])):
        if i > j and M[i][j] == 1:
            union(i, j)

print(len(sets))