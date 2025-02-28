# # Example of how python dictionary/set works (i.e. hashing mechanism).
# numbers = [1,2,2,3,4,4,5]
# print(set(numbers))
# unique = list(set(numbers))
# print(unique)

#https://www.youtube.com/watch?v=C4Kc8xzcA68

# nums=[1,2,3]
# result=all(nums)
# print(result)

# else block is for 'for loop' and not part of if structure. 
# if the for loop execution completes successfully then else block is executed.
# since there is a break statement and for loop is exited, the else block is 
# not executed here.

# for i in range(3):
#     if i == 2:
#         break
# else:
#      print("Else executed")

# def multiply(*args):
#     result = 1
#     for item in args:
#         result *= item
#     return result
# #    print(result, end = " ")

# print(multiply(2, 3, 4))

#from curses.ascii import isdigit
#from re import I


#from curses.ascii import isdigit


print("**********SortingAlgorithm***********")
# sort elements in an array.
# Logic/ breakdown to small problem - 
# relate to code.
# write and test (read code in debug terms) - in small chunks, if problem is big.
# execute
# permutation - with this we found 'min' element of array, 2min, 3min and moved to resp place.
def SortArrayBruteFrce(List):
    n=len(List)
    for i in range(n):
        for j in range(i+1,n):
            if List[i] > List[j]:
#                breakpoint()
                List[i], List[j] = List[j],List[i]
    print(List)
    
SortArrayBruteFrce([5,4,3,2,1])

# # All possible permutation of given string.
print("***********BackTracking**************")
#TODO vgankidi - write a prototype for recursion and back tracking algo.
# once understood, try with this problem set.
# def recurPermute(index, s, ans):

#     # Base Case
#     if index == len(s):
#         ans.append("".join(s))
#         return

#     # Swap the current index with all
#     # possible indices and recur
#     for i in range(index, len(s)):
#         s[index], s[i] =  

#     recurPermute(index + 1, s, ans)
# #         s[index], s[i] = s[i], s[index]

# ans = []
# recurPermute(0, list("ABC"), ans)

# # Function to find all unique permutations
# def findPermutation(s):

#     # Stores the final answer
#     ans = []

#     recurPermute(0, list(s), ans)

#     # sort the resultant list
#     ans.sort()

#     return ans

# if __name__ == "__main__":
#     s = "ABC"
#     res = findPermutation(s)
#     for x in res:
#         print(x, end=" ") 



print("*************LinkedList**************")
#
#
#


print("*************Dictonary***************")
#
#
#



print("************BinaryTree****************")
#
#
#


print("**********IPAddressCheck*************")
# x1.x2.x3.x4 - check if this is valid.  0<=x<=255. Detect trail zeros
# and 01, 0, @, x, a, 1938
# that x >= 0 and <=255.
# validation check - > is digit &&  >=0 and <255 
# no it misses 000, 00 => 
# Find trailing zero in string - 

# base case - simple case.
# positive case - if positive case - return True.
# negative case - if negative case - return False.

# In the below I mixed positive and negative. //
# what is improvement in the below case - since there are no. of possibilties of 
# truth. we only define code/constraints for failing cases. And for passing cases
# we use failing check pass. TODO@vgankidi - rewrite this again.

def IsValid(IP):
    if IP.isdigit() and 0 <=int(IP) <=255 and len(IP) <=3:
        if IP[0] =='0' and len(IP) !=1:
            return False
        return True
    return False

def ValidIp(inp):
    IpNum = inp.split('.')
    for item in IpNum:
        if IsValid(item) : 
            continue
        print("Not Valid Ipv4")
        return
    print("Valid Ipv4")

InList=["192.168.0.1", "192.168.0.00", "192.168.A.1", "192.168.0.1234","192.168.0.01" ]
ValidIp("192.168.0.1")
for item in InList:
    ValidIp(item)

# Existence proof. 
# 0<=x<=255 - This is claim (x1.x2.x3.x4). structure of claim
# 192.168.0.1 -example. [proof] 
# 192.01.00.1 - claim is false. All examples. 

# What's the output of this snippet?
# https://www.freecodecamp.org/news/python-lambda-function-explained/
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = list(map(lambda x, y: x + y, list1, list2))
# If we assign a function to a variable either a anonymos function
# or function defined using def keyword. We can use that variable
# to pass function as an arugment to another functions. This makes
# code more readable?.
alist1= (lambda x,y : x.append(y)) # append the list2 to list1.

alist1(list1,list2) # here we can use the lamdba implementation as a function.
print(result)  # prints 5,7,6
print(alist1) # prints [1,2,3,4,5,6]


# List in Python Elements of expressions.
# extended BNF notation <-> describe syntax.
# walrus operator ":". And slicing start, stop, step.
# Assign the variable after evaluating expression. useful in condition
# checking, list comprehension.
d = {x:x[::-1] for x in ["abc","xyx"]}
print(d)

# List comprehension -
# use it to filter, format, modify, or do other small tasks on 
# existing iterables such as strings, tuples, sets, dataframes, array lists.

# Simple list comprehension****
# List comprehension with single and nested if conditions****
# List comprehension with single and multiple if and else conditions****
# List comprehension with nested for loops****
lst=[0,2,3,4,5,6,8,10]
['Two' if x%2 == 0 else "Three" if x%3 == 0 else 'not 2 & 3' for x in lst]
['Two' if x%2 == 0 else "Three" if x%3 == 0 else 'not 2 & 3' for x in lst if x > 8]

# FizzBuzz with List comprehension
#What is the Python Fizzbuzz?
#Assume we have a number n. Then we have to display all numbers ranging from 1 to n in string representation, but there are few restrictions on how we can show those numbers.

#If the number is divisible by three, substitute Fizz for the number.
#If the number is divisible by 5, substitute Buzz for the number.
#If the number is divisible by 3 and 5, substitute FizzBuzz for the integer.
def Fizzbuzz(n):
    out=[]
    for i in range(1,n+1):
        if i % 3 and i % 5 == 0:
            out.append("FizzBuzz")
        elif i % 5 == 0:
            out.append("Buzz")
        elif i % 3 == 0:
            out.append("Fizz")
        else:
            out.append(str(i))
    return "".join(out) # str="" , return str.join(out)


if __name__ == "__main__":
    print(Fizzbuzz(5))

# Use List comprehension - FizzBuzz Challenge 1 line
# walk through like a debugger line by line.
out = ["FizzBuzz" if i%3==0 and i%5==0 else "Buzz" if i%5 == 0 else "Fizz" if i% 3 == 0 else str(i) for i in range(1,6)]
print("".join(out))

# TODO@vgankidi - use lambda function and walrus operator with List comprehensions

# List comprehension with nested for loops****
Li=[1,2]
PosPerm = [(x,y) for x in Li for y in Li]
print(PosPerm)