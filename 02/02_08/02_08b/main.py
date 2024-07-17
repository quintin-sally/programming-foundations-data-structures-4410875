my_list = [1, 7, 3]
print(sorted(my_list))

print(sorted(my_list, reverse=True))

student_grades = [('Sarah', 89), ('Rebecca', 82), ('Matt', 91)]

#prints list sorted based of the thing in index 0 of the first value. 
#So strings in the first value of the tuple
print(sorted(student_grades))

#sorts based off the grades in descending order
#lambda function looks in the item and picks the value at index 1
#reverse variable then sorts it in reverese order
print(sorted(student_grades, key = lambda x:x[1], reverse=True))