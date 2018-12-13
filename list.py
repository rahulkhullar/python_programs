'''
#Sum of all elements in a list
def list_sum(input):
    sum = 0
    for i in range(0, len(input)):
        sum += input[i]
    return sum

input = [5,6,6,9,8]
print(list_sum(input))
'''

'''
#to print largest number from the list
def largest(input):
    num_largest = input[0]
    for i in range(0, len(input)):
        if input[i] > num_largest:
            num_largest = input[i]
    return num_largest


input = [5, 6, 6, 9, 8]
print(largest(input))
'''

# Write a Python program to count the number of strings where the string length is 2 or more and
# the first and last character are same from a given list of strings
'''def str_list(input_):

    result_count = 0
    for i in range(0, len(input_)):
        if len(input_[i]) >= 2 and input_[i][0] == input_[i][-1]:
            result_count +=1
    return result_count



input_ = ['abc', 'xyz', 'ab4aaa', '12217']
print(str_list(input_))
'''
'''
def remove_duplicate(input1):
    output = []
    for i in input1:
        if output.__contains__(i):
            pass
        else:
            output.append(i)
    return output

input1 = ['abc', 'bcv', 'abc']
print(remove_duplicate(input1))    
'''
#Sorting list function program
'''
def list_inc(input1):
    output = []
    while input1:
        minimum = input1[0]
        for i in input1:
            if i < minimum:
                minimum = i
        output.append(minimum)
        input1.remove(minimum)
    return output


input1 = [5,8,9,6,23,1]
#input1 = [[2, 5], [1, 2], [4, 4], [2, 3], [2, 1]]
print(list_inc(input1))
'''
#remove duplicates from list

def duplicate(input1):
    output = []
    for i in input1:
        if output.__contains__(i):
            pass
        else:
            output.append(i)
    return output

input1 = [5,8,9,6,23,6,1,5,8]
print(duplicate(input1))