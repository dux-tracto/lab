# version code 75eb0ae74c69+
coursera = 1
# Please fill out this stencil and submit using the provided submission script.
def printTaskMarker(taskNum): print("\n**** task: " + str(taskNum) + " ****")	

## 1: (Task 1) Minutes in a Week
printTaskMarker(1)
minutesPerHour = 60
hoursPerDay = 24
daysPerWeek = 7
minutes_in_week = minutesPerHour * hoursPerDay * daysPerWeek
print("minutes_in_week: " + str(minutes_in_week))


## 2: (Task 2) Remainder
#For this task, your expression must use //
printTaskMarker(2)
n = 2304811
d = 47
remainder_without_mod = n - ((n // d) * 47)
print("remainder_without_mod: " + str(remainder_without_mod))



## 3: (Task 3) Divisibility
printTaskMarker(3)
divisible_by_3 = (673 + 909) % 3 == 0
print("divisible_by_3: " + str(divisible_by_3))



## 4: (Task 4) Conditional Expression
printTaskMarker(4)
x = -9
y = 1/2
expression_val = 2**(y+1/2) if x+10<0 else 2**(y-1/2)
print("prediction: 1")
print("expression_val: " + str(expression_val))



## 5: (Task 5) Squares Set Comprehension
printTaskMarker(5)
first_five_squares = { x ** 2 for x in {1,2,3,4,5} }
print("first_five_squares: "  + str(first_five_squares))



## 6: (Task 6) Powers-of-2 Set Comprehension
printTaskMarker(6)
first_five_pows_two = { 2 ** x for x in {0,1,2,3,4} }
print("first_five_pows_two: " + str(first_five_pows_two))

## 7: (Task 7) Double comprehension evaluating to nine-element set
printTaskMarker(7)
# Assign three-element sets to X1 and Y1 so that
# {x*y for x in X1 for y in Y1} evaluates to a nine-element set.
X1 = { 2, 3, 4 }
Y1 = { 5, 6, 7 }
nine_set = {x*y for x in X1 for y in Y1}  
print("nine_set: " + str(nine_set))
print("len(nine_set): " + str(len(nine_set)))

## 8: (Task 8) Double comprehension evaluating to five-element set
printTaskMarker(8)
# Assign disjoint three-element sets to X1 and Y1 so that
# {x*y for x in X1 for y in Y1} evaluates to a five-element set.
X2 = { 0, 1, 2 }
Y2 = { 2, 4, 8 }
five_set = {x*y for x in X2 for y in Y2}  
print("five_set: " + str(five_set))
print("len(five_set): " + str(len(five_set)))



## 9: (Task 9) Set intersection as a comprehension
printTaskMarker(9)
S = {1, 2, 3, 4}
T = {3, 4, 5, 6}
# Replace { ... } with a one-line set comprehension that evaluates to the intersection of S and T
S_intersect_T = { x for x in S for y in T if x in T }
print("S_intersect_T: " + str(S_intersect_T))


## 10: (Task 10) Average
printTaskMarker(10)
list_of_numbers = [20, 10, 15, 75]
# Replace ... with a one-line expression that evaluates to the average of list_of_numbers.
# Your expression should refer to the variable list_of_numbers, and should work
# for a list of any length greater than zero.
list_average = sum(list_of_numbers) / len(list_of_numbers)
print("list_average: " + str(list_average))



## 11: (Task 11) Cartesian-product comprehension
printTaskMarker(11)
# Replace ... with a double list comprehension over ['A','B','C'] and [1,2,3]
cartesian_product = [[x,y] for x in ['A','B','C'] for y in [1,2,3]]
print("cartesian_product: " + str(cartesian_product))


## 12: (Task 12) Sum of numbers in list of list of numbers
printTaskMarker(12)
LofL = [[.25, .75, .1], [-1, 0], [4, 4, 4, 4]]
# Replace ... with a one-line expression of the form sum([sum(...) ... ]) that
# includes a comprehension and evaluates to the sum of all numbers in all the lists.
LofL_sum = sum(sum(x) for x in LofL)
print("LofL_sum: " + str(LofL_sum))



## 13: (Task 13) Three-element tuples summing to zero
printTaskMarker(13)
S = {-4, -2, 1, 2, 5, 0}
# Replace [ ... ] with a one-line list comprehension in which S appears
zero_sum_list = [[x,y,z] for x in S for y in S for z in S if (x+y+z) == 0] 
print("zero_sum_list: " + str(zero_sum_list))



## 14: (Task 14) Nontrivial three-element tuples summing to zero
printTaskMarker(14)
S = {-4, -2, 1, 2, 5, 0}
# Replace [ ... ] with a one-line list comprehension in which S appears
exclude_zero_list = [[x,y,z] for x in S for y in S for z in S if (x+y+z) == 0 and x != 0 and y != 0 and z != 0]
print("exclude_zero_list: " + str(exclude_zero_list))


## 15: (Task 15) One nontrivial three-element tuple summing to zero
printTaskMarker(15)
S = {-4, -2, 1, 2, 5, 0}
# Replace ... with a one-line expression that uses a list comprehension in which S appears
first_of_tuples_list = [[x,y,z] for x in S for y in S for z in S if (x+y+z) == 0 and x != 0 and y != 0 and z != 0][0]
print("first_of_tuples_list: " + str(first_of_tuples_list))



## 16: (Task 16) List and set differ
printTaskMarker(16)
# Assign to example_L a list such that len(example_L) != len(list(set(example_L)))
example_L = [1,2,2]
l1 = len(example_L)
l2 = len(list(set(example_L)))
print("           len(example_L): " + str(l1))
print("len(list(set(example_L))): " + str(l2))

## 17: (Task 17) Odd numbers
printTaskMarker(17)
# Replace {...} with a one-line set comprehension over a range of the form range(n)
odd_num_list_range = [x for x in range(100) if x % 2 == 1]
print("odd_num_list_range: " + str(odd_num_list_range))



## 18: (Task 18) Using range and zip
printTaskMarker(18)
# In the line below, replace ... with an expression that does not include a comprehension.
# Instead, it should use zip and range.
# Note: zip() does not return a list. It returns an 'iterator of tuples'
L = ['A','B','C','D','E']
range_and_zip = list(zip(list(range(5)),L))
print("range_and_zip: " + str(range_and_zip))



## 19: (Task 19) Using zip to find elementwise sums
printTaskMarker(19)
A = [10, 25, 40]
B = [1, 15, 20]
# Replace [...] with a one-line comprehension that uses zip together with the variables A and B.
# The comprehension should evaluate to a list whose ith element is the ith element of
# A plus the ith element of B.
list_sum_zip = [sum(x) for x in zip(A,B)]
print("list_sum_zip: " + str(list_sum_zip))


## 20: (Task 20) Extracting the value corresponding to key k from each dictionary in a list
printTaskMarker(20)
dlist = [{'James':'Sean', 'director':'Terence'}, {'James':'Roger', 'director':'Lewis'}, {'James':'Pierce', 'director':'Roger'}]
k = 'James'
# Replace [...] with a one-line comprehension that uses dlist and k
# and that evaluates to ['Sean','Roger','Pierce']
value_list = [ d['James'] for d in dlist ]
print("value_list: " + str(value_list))


## 21: (Task 21) Extracting the value corresponding to k when it exists
printTaskMarker(21)
dlist = [{'Bilbo':'Ian','Frodo':'Elijah'},{'Bilbo':'Martin','Thorin':'Richard'}]
k = 'Bilbo'
#Replace [...] with a one-line comprehension 
value_list_modified_1 = [ d.get(k,'NOT PRESENT') for d in dlist ]
print("value_list_modified_1: " + str(value_list_modified_1))

k = 'Frodo'
value_list_modified_2 = [ d.get(k,'NOT PRESENT') for d in dlist ]
print("value_list_modified_2: " + str(value_list_modified_2))



## 22: (Task 22) A dictionary mapping integers to their squares
printTaskMarker(22)
# Replace {...} with a one-line dictionary comprehension
square_dict = { key:key * key for key in range(99)}
print("square_dict: " + str(square_dict))



## 23: (Task 23) Making the identity function
printTaskMarker(23)
D = {'red','white','blue'}
# Replace {...} with a one-line dictionary comprehension
identity_dict = { key:val for key in D for val in D if key == val }
print("identity_dict: " + str(identity_dict))



## 24: (Task 24) Mapping integers to their representation over a given base
printTaskMarker(24)
base = 2
digits = list(range(base))
# Replace { ... } with a one-line dictionary comprehension
# Your comprehension should use the variables 'base' and 'digits' so it will work correctly if these
# are assigned different values (e.g. base = 2 and digits = {0,1})
#representation_dict = { x * base ** 2 + y * base ** 1 + z * base ** 0:(x,y,z) for x in range(base) for y in range(base) for z in range(base) }
representation_dict = { str(digits[x]) + str(digits[y]) + str(digits[z]):(x,y,z) for x in range(base) for y in range(base) for z in range(base) }
print("representation_dict: " + str(representation_dict)) 


## 25: (Task 25) A dictionary mapping names to salaries
printTaskMarker(25)
id2salary = {0:1000.0, 1:1200.50, 2:990}
names = ['Larry', 'Curly', 'Moe']
# Replace { ... } with a one-line dictionary comprehension that uses id2salary and names.
listdict2dict = { names[id]:id2salary[id] for id in id2salary.keys() }
print("listdict2dict: " + str(listdict2dict))



## 26: (Task 26) Procedure nextInts
printTaskMarker(26)
# Complete the procedure definition by replacing [ ... ] with a one-line list comprehension
def nextInts(L): return [ x + 1 for x in L ]
print("nextInt([1,3,5]): " + str(nextInts([1,3,5])))


## 27: (Task 27) Procedure cubes
printTaskMarker(27)
# Complete the procedure definition by replacing [ ... ] with a one-line list comprehension
def cubes(L): return [ x ** 3 for x in L ] 
print("cubes([2,3,4]): " + str(cubes([2,3,4])))



## 28: (Task 28) Procedure dict2list
printTaskMarker(28)
# Input: a dictionary dct and a list keylist consisting of the keys of dct
# Output: the list L such that L[i] is the value associated in dct with keylist[i]
# Example: dict2list({'a':'A', 'b':'B', 'c':'C'},['b','c','a']) should equal ['B','C','A']
# Complete the procedure definition by replacing [ ... ] with a one-line list comprehension
def dict2list(dct, keylist): return [ dct[keylist[i-1]] for i in range(len(keylist))]
dct={'a':'A', 'b':'B', 'c':'C'}
keylist=list(dct.keys())
print(str(keylist))
print("dict2list(): " + str(dict2list(dct, keylist)))



## 29: (Task 29) Procedure list2dict
printTaskMarker(29)
# Input: a list L and a list keylist of the same length
# Output: the dictionary that maps keylist[i] to L[i] for i=0,1,...len(L)-1
# Example: list2dict(['A','B','C'],['a','b','c']) should equal {'a':'A', 'b':'B', 'c':'C'}
# Complete the procedure definition by replacing { ... } with a one-line dictionary comprehension
def list2dict(L, keylist): return { keylist[idx - 1]:L[idx - 1] for idx in range(len(keylist)) }
L=['A','B','C']
keylist = ['a','b','c']
print("list2dict(): " + str(list2dict(L, keylist)))
