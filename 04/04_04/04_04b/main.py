primary_colors = frozenset(["red", "blue", "yellow"])

if "blue" in primary_colors:
  print("blue is in the set!")

#primary_colors.add("green") #returns an error because the set is inmuteable

test = "sample"
s = set()
for a in test:
  print(a)
  s.add(a)
print(s)