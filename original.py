'''Question For the integers 1 through 50, find the sum of even numbers MINUS
the sum of numbers that are divisible by 7.''' 

'''
Sub questions
* What are the integers 1 through 50?
* What numbers are divisible by 7 in a certain list?
* What are even numbers in a certain list?
* What is the difference between two numbers?
'''

def get_50_integers():
    '''Get a list of integers from 1 to 50'''
    return list(range(1,51))

def is_divisible(divisible_by,integer_list):
    '''Find all integers in a given list that are divisible by a given number'''
    divisible_list = []
    for number in integer_list:
        if number % divisible_by == 0:
            divisible_list.append(number)
    return divisible_list

def is_even():
    '''Return all even numbers in a given list'''   
    return is_divisible(2, get_50_integers())

def divisible_by_7():
    '''Return all numbers divisible by 7 in a given list''' 
    return is_divisible(7, get_50_integers())

print(sum(is_even())-sum(divisible_by_7()))



    
