def sorted_list(input_list):
    result = []
    while input_list:
        min_value = input_list[0]
        for x in input_list:
            if x < min_value:
                min_value = x
        result.append(min_value)
        input_list.remove(min_value)
    return result



print(sorted_list([-15, -26, 15, 1, 23, -64, 23, 76]))