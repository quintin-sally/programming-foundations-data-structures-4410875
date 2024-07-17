# Key: State
# Value: Capital

states_to_capitals = {
  "Texas": "Austin",
  "New York": "Albany",
  "Colorado": "Denver"
}

print(states_to_capitals["New York"])

for key in states_to_capitals.keys():
  print(key)

for key, value in states_to_capitals.items():
  print(key + " | " + value)