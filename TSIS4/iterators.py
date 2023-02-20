'''
1. Create a generator that generates the squares of numbers up to some number N.

2. Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.

3. Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.

4. Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.

5. Implement a generator that returns all numbers from (n) down to 0.
'''

#1
def square_power(n):
    for i in range(1, n + 1):
        yield i * i

nums = int(input())
a = square_power(nums)

for i in range(nums):
    print(next(a), end=" ")
print('\n')

#2
def even_numbers(n):
    for i in range(1, n + 1):
        if (i % 2 == 0):
            yield i

second_num = int(input())
for i in even_numbers(second_num):
    print(i, end=" ")
print('\n')

# 3
def three_four(n):
    for i in range(1, n+1):
        if (i % 3 == 0 and i % 4 == 0):
            yield i

for i in three_four(int(input())):
    print(i, end=" ")
print('\n')

# 4
def square(a, b):
    for i in range(a, b + 1):
        yield i * i


first = int(input())
second = int(input())
for i in square(first, second):
    print(i, end=" ")
print('\n')

#5
def reverse(n):
    i = n
    while i != -1:
        yield i
        i -= 1

reverse_num = int(input())
for i in reverse(reverse_num):
    print(i, end=" ")