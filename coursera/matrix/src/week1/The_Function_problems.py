# version code 3e169d60c2de+
coursera = 1
def printTaskMarker(taskNum): print("\n**** task: " + str(taskNum) + " ****")	
# Please fill out this stencil and submit using the provided submission script.





## 1: (Problem 0.8.3) Tuple Sum
printTaskMarker(1)
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
    '''
    if len(A) == len(B):
        result = list()
        for idx in range(len(A)):
            (a1,a2) = A[idx]
            (b1,b2) = B[idx]
            r1 = a1 + b1
            r2 = a2 + b2
            result.append((r1,r2))
        return result
    else:
        print("A and B were not the same size")
        return None

A = [(1,2), (3,4)]
B = [(5,6), (7,8)]
print("tuple_sum(): "  + str(tuple_sum(A, B)))


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
    r = dict()
    for key in d.keys():
        #print(str(key) + " => " + str(d.get(key)))
        r[d.get(key)] = key
    return r

d = {'foo': 1, 'bar': 2, 'baz': 3}
r = inv_dict(d)
print(str(r))


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
    return [p+x for x in range(n)]

r = row(10, 4)
print("row(10,4): " + str(r))

comprehension_with_row = ...

comprehension_without_row = ...



## 4: (Problem 0.8.10) Probability Exercise 1
Pr_f_is_even = ...
Pr_f_is_odd  = ...



## 5: (Problem 0.8.11) Probability Exercise 2
Pr_g_is_1    = ...
Pr_g_is_0or2 = ...

