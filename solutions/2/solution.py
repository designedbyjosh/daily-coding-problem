def solve(x, y, b):
    b = -b;
    return (x & b) | (y & ~b)