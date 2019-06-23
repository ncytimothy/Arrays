# Max-Sum-Subarray

def max_sum_subarray(arr):
    largest_sum = 0
    current_sum  = 0
    for number in arr:
        current_sum = max(number, current_sum + number)
        largest_sum = max(current_sum, largest_sum)
    return largest_sum


# arr = [1, 2, -5, -4, 1, 6]
# print(max_sum_subarray(arr))

def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]

    output = max_sum_subarray(arr)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


# arr_1= [1, 2, 3, -4, 6]
# solution= 8 # sum of array
#
# test_case = [arr_1, solution]
# test_function(test_case)
#
# arr_2= [1, 2, -5, -4, 1, 6]
# solution = 7   # sum of last two elements
#
# test_case = [arr, solution]
# test_function(test_case)
#
arr_3= [-12, 15, -13, 14, -1, 2, 1, -5, 4]
# solution = 18  # sum of subarray = [15, -13, 14, -1, 2, 1]

print(max_sum_subarray(arr_3))

# test_case = [arr, solution]
# test_function(test_case)
