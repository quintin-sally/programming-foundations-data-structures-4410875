def has_unique_characters(data):
    s = set()
    for a in data:
        if a in s:
            return False
        else:
            s.add(a)
    return True

print(has_unique_characters('sample'))
print(has_unique_characters('hello world'))
print(has_unique_characters('linkedin'))
print(has_unique_characters('python'))

