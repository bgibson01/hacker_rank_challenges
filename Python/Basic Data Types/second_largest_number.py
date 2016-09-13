'''
You are given N numbers. Store them in a list and find the second largest number.

Input Format 
------------
The first line contains N. The second line contains an array A [] of N integers 
each separated by a space.

Constraints 
------------
2 <= N <= 10
-100 <= A[i] <= 100

Output Format
------------
Output the value of the second largest number.

Sample Input
------------
5
2 3 6 6 5

Sample Output
------------
5
'''

n = int(input())
num_lst = [int(x) for x in input().split()]
sorted_num_lst = sorted(num_lst)
for i in range((len(sorted_num_lst) - 1), -1, -1):
    current_num = sorted_num_lst[i]
    next_num = sorted_num_lst[i-1]
    if current_num > next_num:
        print(next_num)
        break
    else:
        pass
