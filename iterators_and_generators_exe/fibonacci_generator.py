def fibonacci():
    x = 0
    y = 1
    yield x
    yield y

    while True:
        next = x + y
        yield next
        x, y = y, next



generator = fibonacci()
for i in range(5):
    print(next(generator))