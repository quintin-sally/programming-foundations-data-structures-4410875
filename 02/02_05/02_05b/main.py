#nested list
seating_chart = [
    ["Sarah", "Claire", "Ben", "Taylor", "Eva"],
    ["Frankie", "George", "Lindsey", "Izzy", "Jack"],
    ["Katherine", "Lauren", "Mary", "Nathan", "Olive"],
    ["Chad", "April", "Matt", "Thomas", "Penny"]
]

#print(seating_chart[2][1])

#list out all students in each row
for i, row in enumerate(seating_chart):
    print(f"row{i+1}. Students:{row}")

#list out each student in the row number & seat number
for i, row in enumerate(seating_chart):
    for j, student_name in enumerate(row):
        print(f"{student_name} is in row {i+1}, seat {j+1}")

#list out each student in the row number & seat number
for i, row in enumerate(seating_chart):
    for j, student_name in enumerate(row):
        print(f"{student_name} is in row {i+1}, seat {j+1}")