# version code 80e56511a793+
# Please fill out this stencil and submit using the provided submission script.





## 1: (Problem 0.8.3) Tuple Sum
def tuple_sum(A, B):
    '''
    Input:
      -A: a list of tuples
      -B: a list of tuples
    Output:
      -list of pairs (x,y) in which the first element of the
      ith pair is the sum of the first element of the ith pair in
      A and the first element of the ith pair in B
    Examples:
    >>> tuple_sum([(1,2), (10,20)],[(3,4), (30,40)])
    [(4, 6), (40, 60)]
    >>> tuple_sum([(0,1),(-1,0),(2,2)], [(3,4),(5,6),(7,8)])
    [(3, 5), (4, 6), (9, 10)]
    '''
    return_tuple = []

    for ind in range(len(A)):
        return_tuple.append(tuple(map(sum, list(zip(A[ind], B[ind])))))

    return return_tuple

## 2: (Problem 0.8.4) Inverse Dictionary
def inv_dict(d):
    '''
    Input:
      -d: dictionary representing an invertible function f
    Output:
      -dictionary representing the inverse of f, the returned dictionary's
       keys are the values of d and its values are the keys of d
    Example:
    >>> inv_dict({'goodbye':  'au revoir', 'thank you': 'merci'}) == {'merci':'thank you', 'au revoir':'goodbye'}
    '''
    return { v:k for k, v in d.items() }



## 3: (Problem 0.8.5) Nested Comprehension
def row(p, n):
    '''
    Input:
      -p: a number
      -n: a number
    Output:
      - n-element list such that element i is p+i
    Examples:
    >>> row(10,4)
    [10, 11, 12, 13]
    '''
    return [p + i for i in range(n)]

comprehension_with_row = [row(p, 20) for p in range(15)]

comprehension_without_row = [[p + i for i in range(20)] for p in range(15)]



## 4: (Problem 0.8.10) Probability Exercise 1

def is_even_func(x, condition):
    if x % 2 == condition:
        return True
    
    return False

def prob1(condition):    
    domain = { 1, 2, 3, 5, 6 }
    codomain = { 2, 3, 4, 6, 7 }
    probabilities = [ 0.5, 0.2, 0.1, 0.1, 0.1 ]
    
    probs = [z for x, y, z in zip(domain, codomain, probabilities) if is_even_func(y, condition) ]
    
    return sum(probs)
    
Pr_f_is_even = prob1(0)
Pr_f_is_odd  = prob1(1)



## 5: (Problem 0.8.11) Probability Exercise 2

def outputs_one(val):
    return val == 1

def outputs_zero_or_two(val):
    return val == 0 or val == 2

def prob2(method):
    domain = { 1, 2, 3, 4, 5, 6, 7 }
    codomain = { 0, 1, 2 }
    probabilities = [ 0.2, 0.2, 0.2, 0.1, 0.1, 0.1, 0.1 ]

    codomain = [ x % 3 for x in domain ]
    
    probs = [z for x, y, z in zip(domain, codomain, probabilities) if method(y) ]

    return sum(probs)

Pr_g_is_1    = prob2(outputs_one)
Pr_g_is_0or2 = prob2(outputs_zero_or_two)

