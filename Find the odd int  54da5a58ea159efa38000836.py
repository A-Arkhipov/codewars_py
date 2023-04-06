# Find the odd int 
# https://www.codewars.com/kata/54da5a58ea159efa38000836/python

#DESCRIPTION:
#Given an array of integers, find the one that appears an odd number of times.

#There will always be only one integer that appears an odd number of times.

#Examples
#[7] should return 7, because it occurs 1 time (which is odd).
#[0] should return 0, because it occurs 1 time (which is odd).
#[1,1,2] should return 2, because it occurs 1 time (which is odd).
#[0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
#[1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).

from functools import reduce

my_list = [1, 1, 2]
my_set = set(my_list)

#for el in my_set:
    #if my_list.count(el) % 2 == 1:
        #print(el)
        #break
    
# print(list(el for el in my_set if (my_list.count(el) % 2 == 1))[0])


print(reduce(lambda x, y: x^y, my_list))
    