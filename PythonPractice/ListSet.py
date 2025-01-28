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

def multiply(*args):
    result = 1
    for item in args:
        result *= item
    return result
#    print(result, end = " ")

print(multiply(2, 3, 4))

#lms. <=> [L]