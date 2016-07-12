'''Question For the integers 1 through 50, find the sum of even numbers MINUS
the sum of numbers that are divisible by 7.''' 

'''
Sub questions
* What are the integers 1 through 50?
* What numbers are divisible by 7?
* What are the sum of a list of numbers?
* What is the difference between two numbers?
'''

def get_50_integers():
    '''Get a list of integers from 1 to 50'''
    return list(range(1,51))

def is_divisible(divisible_by,integer_list):
    divisible_list = []
    for number in integer_list:
        if number % divisible_by == 0:
            divisible_list.append(number)
    return divisible_list

def is_even():
    return is_divisible(2, get_50_integers())

def divisible_by_7():
    return is_divisible(7, get_50_integers())

print(is_even())

    
