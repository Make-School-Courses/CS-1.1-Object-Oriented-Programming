#This is the function we want to test
def my_sum_function(num_list):
    my_sum = 0
    for num in num_list:
        my_sum += num

        #error
        #my_sum *= num

    return my_sum

#This is the function we have written to automatically test our function
#Notice that our test itself could have errors 
def test_sum():
        #correct data
        example = [([1, 3, 5], 9), ([99, 1], 100), ([-5, 0, -2], -7)]

        #data with an error, the test code itself can have errors!
        #example = [([1, 3, 5], 9), ([99, 1], 100), ([-5, 0, -2], -10)]

        for data in example:
                num_list = data[0]
                expected_value = data[1]
                assert my_sum_function(num_list) == expected_value, "Sum function is not correct"

#This is some example data for testing
test_sum()