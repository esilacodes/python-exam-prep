"""
Question: Print first N(100) Fibonacci numbers
Difficulty: Medium
"""

fibonacci_list=[1,1]

while len(fibonacci_list)<101:
     next=fibonacci_list[-1]+fibonacci_list[-2]
     fibonacci_list.append(next)
    
print(fibonacci_list)



#********************************************************************


"""
Question: Find the index of the first Fibonacci number greater than 1000
Difficulty: Medium-Hard
"""

fibonacci_list=[1,1]

while len(fibonacci_list)<101:
    next=fibonacci_list[-1]+fibonacci_list[-2]
    fibonacci_list.append(next)
    
    if next>1000:
        a=len(fibonacci_list)-1
        print(a)
        break

