# a queue has a front and back
# used to get things from the front or the back

#Enqueue = adding an item
#Dequeue = removing an item

#Deque: double ended queue that allows storage and the ability to manipulate data as a queue in Python

from collections import deque

printer_queue = deque()
printer_queue.append("TaylorSwiftTickets.pdf")
printer_queue.append("MarketingNotes.docx")
printer_queue.append("Proof.png")

while len(printer_queue) > 0:
  doc = printer_queue.popleft()
  print(f'Printing {doc}')
  