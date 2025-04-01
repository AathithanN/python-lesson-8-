set1 = {1, 2, 3, 4, 5, 6,7, 7, 8, 8, 9}
print(set1)

set1.add(10)
print(set1)

sa={1, 7, 8, 2, 3}
sb={5, 7, 8, 10, 11}

print(sa.intersection(sb))
print(sa.union(sb))
print(sa.difference(sb))
print(sa.symmetric_difference(sb))