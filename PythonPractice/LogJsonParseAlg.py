# I. Fundamental String Manipulation and Pattern Matching

# Extracting Specific Patterns:
# Problem: Given a string, extract all substrings that match the pattern "ABC[digits]XYZ".
# Example Input: "This is ABC123XYZ and another ABC456XYZ string."
# Expected Output: ["ABC123XYZ", "ABC456XYZ"]

# Parsing Delimited Strings:
# Problem: Given a string with comma-separated values, parse it into a list of individual values.
# Example Input: "apple,banana,orange,grape"
# Expected Output: ["apple", "banana", "orange", "grape"]

# String Validation:
# Problem: Given a string, determine if it is a valid email address (using a simplified validation rule).
# Example Input: "[email address removed]", "invalid-email"
# Expected Output: True, False

# Substring Counting:
# Problem: Given a string and a substring, count the number of occurrences of the substring in the string.
# Example Input: String: "abababa", Substring: "aba"
# Expected Output: 2

# example of permuatation and combination in strings.
# def SubStringOcc_(string, substring):
#     #find aba in aba, find aba two times.
#     # fpointer first location. second pointer first location. look for string.
#     # increment npointer. look for substring - 

#     # all combinations with 'a'. 3 a, ab, aba. 
#     # all possible combination with 'a'
#     # check if a is above. if so increment.
#     counter = 0
#     for p1 in range(0, len(string)):
#         for p2 in range(0, len(string)):
#             if p2 < p1:
#                 continue
#             print(string[p1:p2+1])
#             if substring in string[p1:p2+1]:
#                 counter += 1
#                 print(counter)
#                 break
            #print (f"{p1} {p2}")

# def SubStringOcc(string, substring):
#     for p1 in range(0, len(string)):
#         for p2 in range(p1,len(string)+1,len(substring)):
#             if p2 <= p1:
#                 continue
#             print(f"{p1} {p2}")
#             if substring in string[p1:p2]: print(string[p1 : p2])
#             break
#             # if substring in string[p1 : p2]:
#             #     print(f"{p1} {p2}")
#             #     print(string[p1:p2])
#             #     counter += 1

# SubStringOcc('abababa','a')
# even #odd

# Unique Permutations (Handling Duplicates):
# Problem: Given a string that may contain duplicate characters, generate all unique permutations.
# Example Input: "aab"
# Expected Output: ["aab", "aba", "baa"] (Note: "aba" appears only once)
# Hint: Use sets to remove duplicate permutations.

# How did you find the solution. Start with knowing its a permutation problem.
# I used to find what permutations is allowed according to problem. Then wrote
# solution according to indeces. printed them and then replaced them with strings.
# instead of directly working with strings.
# print ("****StringPerm*********")
# def StrPermu(string):
#     #012,021,102,120,201,210
#     #000e,010e,012,020e,021,022 # generate all possible combinations using for loop.
#     out = []
#     for i in range(0,len(string)):
#         for j in range(0,len(string)):
#             for k in range(0,len(string)):
#                 li = i, j, k
#                 if len(set(li)) == len(string):
#                     out.append(string[i]+string[j]+string[k])
#     print(set(out))

# StrPermu("aab")


#TODO@vgankidi, need to write them with out for loop or dynamic since we cant have more
# for loops.
# Finding all anagrams of a word within a string:
# Finding anagram in string
# Problem: Given a word and a string, find all starting indices where the word's anagrams appear in the string.
# Example Input: word = "abc", string = "abcbacabc" -- Find if the letters of the word are insided the given string.
# Expected Output: [0,3,6]
#TODO @vgankidi.


# def FindAnagram(string):
#     FindAnagram
#     pass

# FindAnagram("abcbacabc")


# Permutations with Constraints:

# Problem: Given a string, generate permutations such that no two adjacent characters are the same.
# Example Input: "abb"
# Possible Valid Output: ["bab"]
# Hint: Generate all permutations, then filter out the invalid ones.



# String Transformation:
# Problem: Given a string, replace all occurrences of a specific character with another character.
# Example Input: String: "hello world", Replace: "l" with "x"
# Expected Output: "hexxo worxd"

# Regex grouping:
# Problem: given the string "IP:192.168.1.1 Date:2025-03-15 Time:12:30:00" create a regex that will extract the IP, Date, and Time into seperate groups.
# Example Input: "IP:192.168.1.1 Date:2025-03-15 Time:12:30:00"
# Expected output: group1: "192.168.1.1", group2: "2025-03-15", group3: "12:30:00"

# II. Data Structures and Algorithms for Log Analysis (String/Data Type Focus)
# Counting Element Frequencies:
# Problem: Given a list of strings, count the frequency of each unique string.
# Example Input: ["apple", "banana", "apple", "orange", "banana", "apple"]
# Expected Output: {"apple": 3, "banana": 2, "orange": 1}

# Sorting Strings:
# Problem: Given a list of strings, sort them alphabetically.
# Example Input: ["orange", "apple", "banana", "grape"]
# Expected Output: ["apple", "banana", "grape", "orange"]

# Filtering Strings:
# Problem: Given a list of strings, filter out strings that contain a specific substring.
# Example Input: ["apple", "banana", "orange", "pineapple"], Substring: "apple"
# Expected Output: ["apple", "pineapple"]

# Aggregating Data:
# Problem: Given a list of tuples, where each tuple contains a key (string) and a value (integer), aggregate the values for each key.
# Example Input: [("apple", 10), ("banana", 20), ("apple", 5), ("orange", 15), ("banana", 30)]
# Expected Output: {"apple": 15, "banana": 50, "orange": 15}

# Detecting Repeated Sequences:
# Problem: Given a list of integers, detect if there are any subsequences of a given length that repeat.
# Example Input: [1, 2, 3, 1, 2, 4, 1, 2], Subsequence Length: 2
# Expected Output: True (because [1, 2] repeats)

# State tracking:
# Problem: Given a list of strings representing actions ("start", "pause", "stop"), track the current state and determine if the sequence is valid (e.g., "start" must be followed by "pause" or "stop").
# Example Input: ["start", "pause", "stop", "start", "stop"]
# Expected Output: state transitions where valid. and no invalid transitions.
# These problems are designed to isolate the fundamental concepts, allowing you to focus on the algorithmic logic without the complexities of file I/O.


# Practice Problems (Simulating JSON Log Manipulation):

# Extracting Specific Fields:

# Problem: Given a log entry (dictionary), extract the values of specific keys (e.g., "timestamp", "user_id", "message").
# Example Input: log_entry = {"timestamp": "2023-10-27T10:00:00Z", "user_id": 12345, "message": "User logged in successfully", "severity": "INFO"}
# Expected Output: {"timestamp": "2023-10-27T10:00:00Z", "user_id": 12345, "message": "User logged in successfully"}
# Filtering Log Entries:

# Problem: Given a list of log entries (list of dictionaries), filter out entries based on a specific key and value (e.g., filter for "severity": "ERROR").
# Example Input: log_entries = [{"severity": "INFO", "message": "User login"}, {"severity": "ERROR", "message": "Database connection failed"}, {"severity": "INFO", "message": "Request processed"}]
# Expected Output: [{"severity": "ERROR", "message": "Database connection failed"}]
# Aggregating Data:

# Problem: Given a list of log entries, where each entry has a "user_id" and "action" key, count the number of actions performed by each user.
# Example Input: log_entries = [{"user_id": 1, "action": "login"}, {"user_id": 2, "action": "logout"}, {"user_id": 1, "action": "request"}, {"user_id": 2, "action": "request"}, {"user_id": 1, "action": "logout"}]
# Expected Output: {1: {"login": 1, "request": 1, "logout": 1}, 2: {"logout": 1, "request": 1}}
# Nested Data Extraction (Simulated):

# Problem: Given a log entry with nested data (simulated as a nested dictionary), extract a value from a nested key.
# Example Input: log_entry = {"metadata": {"request": {"ip_address": "192.168.1.100", "user_agent": "Mozilla/5.0"}}, "message": "Request received"}
# Expected Output: "192.168.1.100" (extract the "ip_address")
# Transforming Log Entries:

# Problem: Given a log entry, transform it by adding or modifying keys.
# Example Input: log_entry = {"timestamp": "2023-10-27T10:00:00Z", "user_id": 12345}
# Expected Output: {"timestamp": "2023-10-27T10:00:00Z", "user_id": 12345, "event_type": "user_activity"}
# Simulated Array Operations:

# Problem: Given a log entry with an array (list) as a value, extract the array.
# Example Input: log_entry = {"user": "testUser", "items": ["item1", "item2", "item3"], "action": "viewedItems"}
# Expected Output: ["item1", "item2", "item3"]
# Complex Filtering:

# Problem: given a list of log entries, filter the objects based on multiple conditions.
# Example Input: log_entries = [{"userID":123, "status":"failed", "count": 3},{"userID":123, "status":"success", "count": 10},{"userID":456, "status":"failed", "count": 1},{"userID":456, "status":"success", "count": 20}]
# Expected Output: [{"userID":123, "status":"failed", "count": 3}, {"userID":456, "status":"failed", "count": 1}] (only failed statuses)