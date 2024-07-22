set_A = {10, 20, 30, 40, 50}
set_B = {30, 40, 50, 60, 70}

union_set = set_A.union(set_B)
#sets do not have dupes

print(union_set)

inter_set = set_A.intersection(set_B)
print(inter_set)

diff_set = set_A.difference(set_B)
print(diff_set) #only what is left in set_A

#flipped
diff_set2 = set_B.difference(set_A)
print(diff_set2) #only what is left in set_B

#Items not shared between A and B
symdiff_set = set_A.symmetric_difference(set_B)
print(symdiff_set)
