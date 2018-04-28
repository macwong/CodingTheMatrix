# Dot products


# Find the closes
a = [1,-1,1,1,1,-1,1,1,1]
b = [1,-1,1,1,-1,1]

#for i in range(len(a) - len(b) + 1):
#    print(sum([x * y for x, y in zip(a[i:len(b) + i], b)]))

def list_dot(a, b):
    return sum([x * y for x, y in zip(a, b)])


def dot_product_list(needle, haystack):
    return [list_dot(needle, haystack[i:len(needle) + i]) for i in range(len(haystack) - len(needle) + 1)]
    
print(dot_product_list(b, a))


