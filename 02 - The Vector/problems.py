from plotting import plot

L = [[2, 2], [3, 2], [1.75, 1], [2, 1], [2.25, 1], [2.5, 1], [2.75, 1], [3, 1], [3.25, 1]]

#plot(L, 5)

def add2(v, w):
    return (v[0] + w[0], v[1] + w[1])

#plot([add2(v, [1,2]) for v in L], 8)

def addn(v, w):
    return [ add2(x, y) for (x, y) in zip(v, w) ]

#plot(addn(L, L), 8)


def scalar_vector_multiply(alpha, v):
    return [ [alpha * x, alpha * y] for (x, y) in v ]

#svm = scalar_vector_multiply(0.5, L)
#plot(svm)

#svm = scalar_vector_multiply(-0.5, L)
#plot(svm)


def segment(pt1, pt2):
    neg_x = pt2[0] - pt1[0]
    neg_y = pt2[1] - pt1[1]
            
    return [ [pt1[0] + (neg_x * (i/100.)), pt1[1] + (neg_y * (i/100.))] for i in range(101) ]

#seg = segment([3.5, 3], [0.5, 1])
#plot(seg, 4)


class Vec():
    def __init__(self, domain, function):
        self.D = domain
        self.f = function
        

v = Vec({'A', 'B', 'C'}, {'A':1})

for d in v.D:
    print(v.f[d] if d in v.f else 'None')
    
def zero_vec(D):
    return Vec(D, { d:0 for d in D })

zv = zero_vec({'A', 'B', 'C', 'D'})
print(zv.f)



























