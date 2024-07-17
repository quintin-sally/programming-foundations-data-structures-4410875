def find_second_smallest(my_list):
   #print(len(my_list))
   if len(my_list) <= 1:
    return None
   else:
     s = sorted(my_list)
     return s[1]
#print(find_second_smallest([0,1]))

print(find_second_smallest([5, 8, 3, 2, 6]))
