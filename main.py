# Write a Python function called max_num()to find the maximum of three numbers.

def maxNum(a, b, c):
    values = [a, b, c]
    return max(values)

print(maxNum(7, 10, 2))
print(maxNum(6, 3, 1))

# Write a Python function called mult_list() to multiply all the numbers in a list.

def mult_list(list):
    res =1 
    for i in list:
        res = res * i
    return res 

test = [3,1,4]
print(mult_list([1,4,10]))
print(mult_list(test))

# Write a Python function called rev_string() to reverse a string.

def rev_string(str):
    if str == '':
        return 'Error'
    else:
        res = str[::-1]
        return res

print(rev_string('sopa'))
print(rev_string(''))

# Write a Python function called num_within() to check whether a number falls in a given range.
# The function accepts the number, beginning of range, and end of range (inclusive) as arguments.

def num_within(x, a, b):
    for i in range(a, b+1):
        if x == i:
            return True
    return False
#function is used with b+1 because the upper limit of the range is inclusive.

print(num_within(2,1,5))
print(num_within(6,1,5))

# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
# The function accepts the number n, the number of rows to print
# Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. Each number is the two numbers above it added together.

def pascal(n):
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        # ForLoop over the previous row 
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    for row in triangle:
        print(row)

pascal(3)
pascal(5)
