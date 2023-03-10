#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time

def iterative_exponent(base, exponent):
    result = 1
    for i in range(exponent):
        result *= base
    return result

def recursive_exponent(base, exponent):
    if exponent == 0:
        return 1
    elif exponent == 1:
        return base
    else:
        return base * recursive_exponent(base, exponent-1)

base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))

# iterative exponent calculation
start_time_iter = time.time()
result_iter = iterative_exponent(base, exponent)
rendering_time_iter = time.time() - start_time_iter

# recursive exponent calculation
start_time_recur = time.time()
result_recur = recursive_exponent(base, exponent)
rendering_time_recur = time.time() - start_time_recur

# print results and rendering times
print(f"Iterative Result: {result_iter}")
print(f"Iterative Rendering time: {rendering_time_iter}")

print(f"Recursive Result: {result_recur}")
print(f"Recursive Rendering time: {rendering_time_recur}")



# In[11]:


# As a result base on the program: The iterative function is faster than the recursive function  the iterative method is faster because it uses a loop to keep multiplying the base by itself until it reaches the exponent. On the other hand, the recursive method makes multiple function calls, and for each call, a new memory space called stack frame is created, which makes it slower and uses more memory compared to the iterative method.


# In[ ]:





# 

# In[ ]:


import time

def iterative_sum_powers(n):
    result = 0
    for i in range(n):
        result +=2 ** i
    return result

def recursive_sum_powers(n):
    if n == 0:
        return 0
    else:
        return 2 ** (n-1) + recursive_sum_powers(n-1)

n = int(input("Enter a value for n: "))

# iterative time calculation
start_time_iterative = time.time()
result_iter = iterative_sum_powers(n)
rendering_time_iterative = time.time() - start_time_iterative

# recursive time calculation
start_time_recursive = time.time()
result_recursive = recursive_sum_powers(n)
rendering_time_recursive = time.time() - start_time_recursive

# print results and  times
print(f"Iterative Result: {result_iter}")
print(f"Iterative Rendering time: {rendering_time_iterative}")

print(f"Recursive Result: {result_recur}")
print(f"Recursive Rendering time: {rendering_time_recursive}")

# still it depends on the value of "n" 
#To put it simply, the iterative function is better for larger values of n because it can calculate the sum with just one loop. On the other hand, the recursive function needs to create many function calls, which can take up more time and memory. For smaller values of n, the difference may not be noticeable. 


# In[ ]:




