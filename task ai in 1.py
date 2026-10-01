p = [1, 2, 3,
     4, 0, 6,
     7, 5, 8]

print("Before:")
print(p)

# Swap 0 and 5
p[4], p[7] = p[7], p[4]

# Swap 0 and 8
p[5], p[8] = p[8], p[5]

print("After:")
print(p)
