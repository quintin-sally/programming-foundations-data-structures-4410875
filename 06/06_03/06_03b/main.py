from collections import deque

history_stack = deque()

history_stack.append("https//google.com")
history_stack.append("https//linkedin.com")
history_stack.append("https//stackoverflow.com")

#implementing a back button functionality
print(history_stack[-1]) #views
print(history_stack.pop()) #views and removes
