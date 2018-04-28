# Dot products

# Find the closes
a = [1,-1,1,1,1,-1,1,1,1]
b = [1,-1,1,1,-1,1]

for i in range(len(a) - len(b) + 1):
    print(sum([x * y for x, y in zip(a[i:len(b) + i], b)]))





