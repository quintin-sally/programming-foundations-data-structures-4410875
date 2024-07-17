''' 
Problem Statement: Compute the average number of pets each student 
has in a given class. 
'''
from statistics import mean
from random import randint

student_pet_count_list = []

for i in range(0,20):
  student_pet_count_list.append(randint(0, 4))
print(student_pet_count_list)

print(mean(student_pet_count_list));

s = 0
t = 0
for i in student_pet_count_list:
  t = t + i
print(t/len(student_pet_count_list)+1)
