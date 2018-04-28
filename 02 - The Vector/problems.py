from plotting import plot
import vec
from vec import Vec

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


#class Vec():
#    def __init__(self, domain, function):
#        self.D = domain
#        self.f = function
        

v = Vec({'A', 'B', 'C'}, {'A':1})

#for d in v.D:
#    print(v.f[d] if d in v.f else 'None')
    
def zero_vec(D):
    return Vec(D, { d:0 for d in D })

#zv = zero_vec({'A', 'B', 'C', 'D'})
#print(zv.f)




D = {'radio', 'sensor', 'memory', 'CPU'}

dur0 = Vec(D, {'radio':1.0, 'sensor':1.0, 'memory':0, 'CPU':0}) #1.5
dur1 = Vec(D, {'radio':2.0, 'sensor':1.0, 'memory':0, 'CPU':0}) #2.5
dur2 = Vec(D, {'radio':0, 'sensor':0, 'memory':1.0, 'CPU':1.0}) #1.5
dur3 = Vec(D, {'radio':0, 'sensor':0, 'memory':0, 'CPU':1.0})   #1

#dur0 * r = 1.5
#r = 1.5 / dur0

rate0 = Vec(D, {'radio':1.5, 'sensor':1.5, 'memory':0, 'CPU':0}) #1.5
rate1 = Vec(D, {'radio':1.25, 'sensor':2.5, 'memory':0, 'CPU':0}) #2.5
rate2 = Vec(D, {'radio':0, 'sensor':0, 'memory':1.5, 'CPU':1.5}) #1.5
rate3 = Vec(D, {'radio':0, 'sensor':0, 'memory':0, 'CPU':1.0})   #1

def calc_watts(key, dur0, dur1, dur2, dur3, rate0, rate1, rate2, rate3):
    radio_dur = [dur0.f[key], dur1.f[key], dur2.f[key], dur3.f[key]]
    radio_rate = [rate0.f[key], rate1.f[key], rate2.f[key], rate3.f[key]]
    
#    print(sum([x * y for x, y in zip(radio_dur, radio_rate)]) / len(radio_dur))
    
calc_watts('radio', dur0, dur1, dur2, dur3, rate0, rate1, rate2, rate3)
calc_watts('sensor', dur0, dur1, dur2, dur3, rate0, rate1, rate2, rate3)
calc_watts('memory', dur0, dur1, dur2, dur3, rate0, rate1, rate2, rate3)
calc_watts('CPU', dur0, dur1, dur2, dur3, rate0, rate1, rate2, rate3)


#D = {'radio', 'sensor', 'memory', 'CPU'}
#rate = Vec(D,{'memory' :0.06, 'radio' :0.1, 'sensor' :0.004, 'CPU' :0.0025}) 
#
#dur0 = Vec(D, {'radio':1.0, 'sensor':1.0, 'memory':0, 'CPU':0}) 
#dur1 = Vec(D, {'radio':2.0, 'sensor':1.0, 'memory':0, 'CPU':0}) 
#dur2 = Vec(D, {'radio':0, 'sensor':0, 'memory':1.0, 'CPU':1.0}) 
#dur3 = Vec(D, {'radio':0, 'sensor':0, 'memory':0, 'CPU':1.0}) 
#
#durations = [dur0.f, dur1.f, dur2.f, dur3.f]
#
#
#radio = [x['radio'] * rate['radio'] for x in durations]
#print(radio)
#print(rate * dur0)
#print(rate * dur1)
#print(rate * dur2)
#print(rate * dur3)

#rate = Vec(D, {'memory':0.06, 'radio':0.1, 'sensor':0.004, 'CPU':0.0025})
#duration = Vec(D, {'memory':1.0, 'radio':0.2, 'sensor':0.5, 'CPU':1.0})
#print(rate*duration)















