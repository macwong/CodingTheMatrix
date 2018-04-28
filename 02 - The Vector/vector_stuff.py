from vec import Vec
import triangular

def list2vec(L):
    return Vec(set(range(len(L))), { x:y for x, y in enumerate(L) })

print(list2vec([3,2,1]))


rowlist = [list2vec([2, 3, -4]), list2vec([0, 1, 2]), list2vec([0, 0, 5])]
b = [10, 3, 15]


x = triangular.triangular_solve_n(rowlist, b)
print(x)