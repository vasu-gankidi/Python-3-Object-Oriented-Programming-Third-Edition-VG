# python program to 
# ignore the spaces in the input text.
# first character of  string is unchanged. The next character
# is compared with the preceding char. If next character is >
# preceding char, convert the next character to upper.  If next character is <
# preceding char, convert the next character to lower. 
# If next character is ==
# preceding char, keep next character as it is. output the modified
# text to the output.

# TODO - vgankidi.

# python to reverse a string in sentence preverse spaces.

# def reverse_string(text):
#     temp=""
#     for i in range(0,len(text)).__reversed__():
#         temp = temp + text[i]
#     return temp + " "

# out = "hello how are you".split(" ")
# output=""    
# for index in range(0,len(out)):
#     output += reverse_string(out[index])
# print(output)

# Find sub string of a string in python.
# str.find(sub[, start[, end]]), str.index(sub[, start[, end]])
# str.endswith(suffix[, start[, end]]), str.find(sub[, start[, end]])

# Longest substring without repeating characters.
# "abcabcaa" - string. 

# def SubString(text):
    # a, ab, abc, b, bc, bca, c, ca, cab. [dictionary keys]
    # 0 : end of str
    # 2 : end of str
    # 3: end of str
    # 4 : end of str , 5, 6, 7.

#StartPoint - Go through the logic agian and explain it to the duck.
# I missed what if p1 not equal to p2. end of string. You directly arrived at incrementing pointer (p1 and p2).
# I didn't think about p1==p2 at begining; do ops; if p1 not equal p2 [position] - what to do.; 

# add exception handling in the below code. (try and except)

# read the code in terms of ALP (but similar to coding execution sequence)
# def SubString(txt):
#     # start pointer p1.
#     # end pointer p2 and 'out' dictionary.
#     # if p1 == p2 and both point to end of string; last element compare with [0:len-1]; if key not present in dictionary, then insert else increment value by 1; exit
#     # start from begining (p1 and p2 pointing same;  if dictinoary is empty add key, else make ditionary empty and add key;  increment p2 continue;
#     # if p1 not equal to p2; if p2 value in 0:p1 variable; if key not present add out to dictionary key and increment value by 1. else increment value by 1; increment p1 && p2 is equal to p1;
#     # if p2 not in 0:p1; increment p2.
#     start,end = (0,0)
#     out_dict = {}
#     # while loop here. How can you debug using print statement? Use debugging to find the issue in this function.
#     # find duplicate code and use different approach.
#     # Use debugger to debug again.
#     while end <= len(txt)-1: # Loop unti we reach end of string
#         #breakpoint()
#         if start == end:
#             if (txt[start] not in out_dict) or (txt[end] not in out_dict):
#                 if start == 0:
#                     out_dict[txt[start]] = len(txt[start]) # store length of string or counter for number of occurences.
#                     end +=1
#                     continue
#                 elif end == len(txt) - 1:
#                     out_dict[txt[end]] = len(txt[end]) # break the loop if we reach the end of the string.
#                     break
#         if start != end:
#             if txt[end] in txt[0:end]: # if length is 0:end is '1'; then we need implement this condition.
#                 print(txt[0:end]) # why I missed [0:start]? - cause you read, but didn't understand in your mind - what it means. That's why.
#                 #if not out_dict[txt[end]]:
#                 out_dict[txt[start:end]] = len(txt[start:end])
#                 #else:
#                 #    pass
#                 start+=1
#                 end=start
#                 continue
#             elif txt[end] not in txt[0:end]:
#                 end +=1
#     return out_dict

# print(SubString("abcabcaa"))

# Check whether the string is Symmetrical or Palindrome - check if reverse of string is true.
# Find length of String - len().
# Reverse words in a given String
# Remove ith character from string
# Avoid Spaces in string length
# Print even length words in a string
# Uppercase Half String
# Capitalize the first and last character of each word in a string
# Check if a string has at least one letter and one number
# Accept the strings which contains all vowels
# Count the Number of matching characters in a pair of string
# Count number of vowels using sets in given string
# Remove all duplicates from a given string
# Least Frequent Character in String
# Maximum frequency character in String
# Odd Frequency Characters
# Specific Characters Frequency in String List
# Frequency of numbers in String
# Program to check if a string contains any special character
# Generating random strings until a given string is generated
# Find words which are greater than given length k
# For removing i-th character from a string
# Split and join a string
# Check if a given string is binary string or not
# Find all close matches of input string from a list
# Find uncommon words from two Strings
# Swap commas and dots in a String
# Permutation of a given string using inbuilt function
# Execute a String of Code
# Print the middle character of a String
# Convert integer to string
# Convert String to Int
# To split string into list of Characters
# To convert a List to String
# To convert String to a list
# How to remove Letters from a String
# Convert a list of Characters into String
# Convert Object to String in Python
# How to sort a list of strings
# To convert tuple to string
# To check if String is Empty or not
# Convert String to Set
# Convert Set to String
# To generate all possible valid IP addresses from given string
# Check and display vowels in a string

# Check for URL in a String //
inp_str = "helohaha www.hello.comsadgl"
left_index = inp_str.find('www')
right_index = inp_str.find('com')
print(right_index)

temp=''
if left_index:
    print("{0}".format({inp_str[left_index:right_index]}).rjust(9,'c'))

# To split string into list of Characters - use string slicing.
#str[i:i+1] where i=0 and <4.
# Func sig - 
# Basic case - 
# Edge case - handle array out of index exception [last index in string, indexing error], empty string.
def String2Char(string):
    out=[]
    for i in range(len(string)) :
        out.append(string[i:i+1])
    print(out)

# string slicing using indexes => Func sig - . 
  # Basic - 0:len[string] [index:] [:index] [start_index: stop_index]
  # Edge case - [high index : low index] [-ve index] [-ve index:] [:-ve index] [-1] [-0] [+0]
  # SampleText="abcdefg"

# str.find,str.rfind,str.join(iterable), str.partition(sep),str.split(sep),str.rpartition(sep)
# str.count, str.endswith

# Swap commas and dots in a String
# str.replace(old, new, count=-1) 
# fun sig
# basic case
# edge case.
def SwapCommaDot(string):
    temp = string.replace('.','-').replace(',','.')
    print(temp.replace('-',','))
SwapCommaDot(".Hello, how, are .you.?")

# implement in another way
def SwapCommaDot2(string):
    # find index and substitue the match with other string.
    
    pass
SwapCommaDot2(".Hello, how, are .you.?")