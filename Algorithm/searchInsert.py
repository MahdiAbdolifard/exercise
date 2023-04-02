"""
search & insert 

        [1, 3, 5, 6], 3 => 1
        [1, 3, 5, 6], 4 => 2
        [1, 3, 5, 6], 7 => 4
        [1, 3, 5, 6], 0 => 0
"""



"""
whit index and while #amir_big
"""
def search_insert(numbers:list, num:int)-> int:
    index_low = 0
    index_high = len(numbers) - 1
    index_mid = index_high // 2

    while index_low <= index_high:
        if num > numbers[index_mid]:
            index_mid += 1
            index_low = index_mid
        else:
            index_mid -= 1
            index_high = index_mid
    return index_low

# print( search_insert([1, 3, 5, 6], 4))

"""
    doctest

>>> search_insert([1, 3, 5, 6], 4)
2
>>> search_insert([1, 3, 5, 6], 3)
1

"""


"""
whit append and sort #mahdi_abdolifard
"""
def search_insert_2(numbers:list, num:int)-> int:
    numbers.append(num)
    sort_numbers = sorted(numbers)
    index_result = sort_numbers.index(num)
    return index_result


"""
    doctest

>>> search_insert_2([1, 3, 5, 6], 4)
2
>>> search_insert_2([1, 3, 5, 6], 5)
0

"""

# print( search_insert_2([1, 3, 5, 6], 0))