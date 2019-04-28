'''
You are given an integer,N . Your task is to print an alphabet rangoli of size N. (Rangoli is a form of Indian folk art based on creation of patterns.)

Input::
size = 3

Output::
----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

Input::
size = 5

Output::
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
'''
def print_rangoli(size):
    import string
    width = 4 * size - 3
    alpha = string.ascii_lowercase
    for i in list(range(size))[::-1] + list(range(1, size)):
        print('-'.join(alpha[size-1:i:-1] + alpha[i:size]).center(width, '-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
