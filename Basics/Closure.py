def outer():
    n = 5

    def inner():
        nonlocal n
        n += 1
        print(n)

    return inner


fn = outer()

fn()
fn()
fn()

print("---")


def multiply(n):
    def inner(m): return n * m
    return inner


fn = multiply(5)
print(fn(1))
print(fn(2))
print(fn(3))