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
# print("***********BackTracking**************")

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
list1 = [1, 2, 3] , list2 = [4, 5, 6] 
result = list(map(lambda x, y: x + y, list1, list2))
print(result)

d = {x:x[::-1] for x in ["abc","xyx"]}
print(d)