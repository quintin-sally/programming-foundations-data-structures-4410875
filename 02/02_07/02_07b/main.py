# Linear Search
import random
my_list = []
for i in range(0, 10):
  my_list.append(random.randint(0,10))
print(my_list)
ITEM = random.randint(0, 10)

def search(item, listy):
  for element in listy:
    if element == item:
      return True
  return False

#inelegent and brute force means of searching. SLOW
print(search(ITEM, my_list))

#index f(x): returns the index of the first instance of the variable in a list
#also a linear search
ITEM_INDEX = my_list.index(ITEM)
  #returns a valueError if no element found
