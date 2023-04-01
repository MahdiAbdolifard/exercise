"""
    [1, 2, 3, 4, 5]

        max 3 => [1, 2, 3]
        min 3 => [3, 4, 5]
        max, min 3 => [3]

        whit lambda and list comprehension
"""


def limit (num, max=None, min=None):

    checke_max = lambda i : True if max is None else i <= max
    check_min =  lambda i : True if min is None else i >= min

    list_num = [i for i in num if check_min(i) and checke_max(i)]

    return list_num



# print(limit([1, 2, 3, 4, 5], 3,3))    #[3]
