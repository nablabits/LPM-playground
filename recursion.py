g = lambda x: 1
h = lambda x: 2

zero = lambda :0
successor = lambda x: x + 1
# projection = lambda x: 

one = successor(zero())
two = successor(one)
print(one, two)

def sum(m, n):
    # we will define a for operator later but for the time being:
    for _ in range(n):
        m = successor(m)
    return m

print(sum(5, 5))

def mul(m, n):
    k = zero()
    for _ in range(n):
        k = sum(k, m)
    return k

print(mul(5, 6))




# def and_(r):
#     pass

# def conditional(r):
#     return bool(r) and g or bool(not r) and h
#     return g and bool(r) or h and bool(not r)

# r = input("Introduce the value of r: ")
# result = conditional(r)
# print(result)
