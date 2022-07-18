def sum_of_numbers(num_list):
    # sourcery skip: inline-immediately-returned-variable, simplify-generator, sum-comprehension
    # without recursion
    result = 0
    for num in num_list:
        result += num
    return result


print(sum_of_numbers([1,3,5,7,9]))


def sum_of_numbers(numList):
    # using recursion
   if len(numList) == 1:
        return numList[0]
   else:
        return numList[0] + sum_of_numbers(numList[1:])

print(sum_of_numbers([1,3,5,7,9]))
