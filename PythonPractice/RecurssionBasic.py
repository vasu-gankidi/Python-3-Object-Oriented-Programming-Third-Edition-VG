#sum of 1 to N numbers.
# base condition. n=0 we return/exit.  
# sub problems [repetitive state] - 

from argparse import _CountAction


def Addnum(n):
    if n == 0:
        return 0
    return n + Addnum(n-1)

print(Addnum(5))

# print 1 to N number
# base condition = n=0 we return. 
# simple task/break down [repetitive]
def PnNum(n):
    if n == 0:
        return
    PnNum(n-1)
    print(n)
    return

PnNum(5)

# print N to 1
# base condition = n=0 we return. 
# simple task/break down [repetitive]
def PnNum(n):
    if n == 0:
        return
    print(n)
    PnNum(n-1)
    return
    
PnNum(5)

print("***PrintSumOfElementsInArray***")
# sum of array elements using recurssion.
# base condition - if List is empy return
# simple task/break down (proof) - li[n] + li[n-1]

# its not the right way of understanding it. - use visual diagram
# to understand.

count=0
def LiSum(Li):
    if len(Li) == 1:
        return Li[0]
    #breakpoint()
    global count
    count += 1
    sum =  Li[len(Li)-1] + LiSum(Li[0:len(Li)-1])
    print(sum)
    return sum   #print(sum)

LiSum([1,2,3,4])

print("*********RecursiveStringReverse***********")
# Reverse of string Recurssion.
# base condition - If string length is 1.
# simple task/break down (proof) - string[n] + string[n-1]
# Debug execution. Understand how it works when debug.
# we can extend this to pallindrome. compare original to result.
def RecStringReverse(string):
    if len(string) == 1:
        return string[0]
    result = string[len(string)-1] + RecStringReverse(string[0:len(string)-1])
    return result

print(RecStringReverse("hello"))

print("*********RecursiveDecimalToBinary************")
