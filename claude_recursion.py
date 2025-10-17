# Projection functions - extract specific arguments from a tuple

def projection(i, n):
    """
    Returns a projection function P_i^n that takes n arguments 
    and returns the i-th argument (1-indexed)
    """
    def proj_func(*args):
        if len(args) != n:
            raise ValueError(f"Expected {n} arguments, got {len(args)}")
        if i < 1 or i > n:
            raise ValueError(f"Index {i} out of range for {n} arguments")
        return args[i - 1]  # Convert to 0-indexed for Python
    
    return proj_func

# Create some specific projection functions
P_1_3 = projection(1, 3)  # First of three arguments
P_2_3 = projection(2, 3)  # Second of three arguments  
P_3_3 = projection(3, 3)  # Third of three arguments

P_1_2 = projection(1, 2)  # First of two arguments
P_2_2 = projection(2, 2)  # Second of two arguments

# Examples of using projection functions
print("=== Basic Projection Examples ===")
print(f"P_1^3(7, 42, 15) = {P_1_3(7, 42, 15)}")  # Should be 7
print(f"P_2^3(7, 42, 15) = {P_2_3(7, 42, 15)}")  # Should be 42
print(f"P_3^3(7, 42, 15) = {P_3_3(7, 42, 15)}")  # Should be 15

print(f"P_1^2(100, 200) = {P_1_2(100, 200)}")    # Should be 100
print(f"P_2^2(100, 200) = {P_2_2(100, 200)}")    # Should be 200

# Example: Why projections are useful in function composition
print("\n=== Function Composition Example ===")

def successor(n):
    """Successor function: S(n) = n + 1"""
    return n + 1

def zero():
    """Zero function: returns 0"""
    return 0

# Suppose we want to define a function f(x, y) = S(x) 
# (successor of first argument, ignoring second)
# We compose successor with the first projection:

def f(x, y):
    """f(x, y) = S(P_1^2(x, y)) = S(x) = x + 1"""
    return successor(P_1_2(x, y))

print(f"f(5, 99) = S(P_1^2(5, 99)) = S(5) = {f(5, 99)}")

# Another example: g(x, y, z) = S(P_2^3(x, y, z)) = y + 1
def g(x, y, z):
    """g(x, y, z) = S(P_2^3(x, y, z)) = y + 1"""
    return successor(P_2_3(x, y, z))

print(f"g(10, 7, 30) = S(P_2^3(10, 7, 30)) = S(7) = {g(10, 7, 30)}")

# Example: Using same argument twice
# h(x, y) = x + x (add first argument to itself)
def add(a, b):
    """Simple addition"""
    return a + b

def h(x, y):
    """h(x, y) = P_1^2(x, y) + P_1^2(x, y) = x + x"""
    return add(P_1_2(x, y), P_1_2(x, y))

print(f"h(6, 100) = P_1^2(6, 100) + P_1^2(6, 100) = 6 + 6 = {h(6, 100)}")

print("\n=== Identity Functions using Projections ===")
# Special case: projection functions with n=1 are identity functions
P_1_1 = projection(1, 1)
print(f"P_1^1(42) = {P_1_1(42)} (identity function)")

print("\n=== Practical Analogy ===")
# Think of projections like array/tuple indexing
data = (10, 20, 30)
print(f"data = {data}")
print(f"data[0] is like P_1^3: {data[0]}")
print(f"data[1] is like P_2^3: {data[1]}")  
print(f"data[2] is like P_3^3: {data[2]}")
