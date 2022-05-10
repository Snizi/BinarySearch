def binary_search(list_obj, target_element):
    lower = 0
    high = len(list_obj) - 1
    

    while lower <= high:

        middle = (lower + high) // 2

        guess = list_obj[middle]


        if guess == target_element:
            return guess
        if guess > target_element:
            high = middle + 1
        else:
            lower = middle - 1
    
    return None



my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3))

    