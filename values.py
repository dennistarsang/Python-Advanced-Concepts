"""Comprehensions"""


values = [x / (x - y) 
        for x in range(100) 
        if x > 50 
        for y in range(100) 
        if x - y != 0]

values = []
for x in range(100):
    if x > 50:
        for y in range(100):
            if x - y != 0:
                values.append(x / (x - y))


result = [(x, y) for x in range(10) for y in range(x)]

result = []
for x in range(10):
    for y in range(x):
        result.append((x, y))


"""Nested comprehensions"""
vals = [[y * 3 for y in range(x)] for x in range(10)]

outer = []
for x in range(10):
    inner = []
    for y in range(x):
        inner.append(y * 3)
    outer.append(inner)