# Stack: ORDERED serise of objects that pushes objects onto the stack
# and pops objects off of the stack
# essentially a stack of cards
# LIFO (Last In, First Out)

card_stack = []

card_stack.append("jack of hearts")
card_stack.append("2 of diamonds")
card_stack.append("10 of spades")

#front(bottom) ---- back(top)

top_card = card_stack.pop()
print(top_card)
top_card = card_stack[-1]
print(top_card)

if not card_stack:
  print("card stack is empty")
else:
  print(len(card_stack))