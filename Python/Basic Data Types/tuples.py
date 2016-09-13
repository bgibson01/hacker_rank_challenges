'''
Task 
------------
Given an integer, n, and n space-separated integers as input, create a tuple, t, 
    of those  integers. Then compute and print the result of .

Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.

Input Format
------------
The first line contains an integer, , denoting the number of elements in the tuple. 
The second line contains  space-separated integers describing the elements in tuple .

Output Format
------------
Print the result of .

Sample Input
------------
2
1 2

Sample Output
------------
3713081631934410656
'''

n = int(input())
input_list = input().split()                # tuple input to list               
list_to_int = [int(x) for x in input_list]  # changes list from str to int
print(int_list)