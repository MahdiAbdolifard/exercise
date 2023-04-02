"""
a1z26
    mahdi => [109, 97, 104, 100, 105]
"""

def incode(char:str) ->list:
    list_code = [ord(i) - 98 for i in char]
    return list_code


def dicode(list_code:list) ->str:
    char = "".join(chr(i + 98) for i in list_code)
    return char

# print(incode("ali"))
# print(dicode([11, -1, 6, 2, 7]))


"""
doctest

>>> incode("mahdi")
[11, -1, 6, 2, 7]

>>> dicode([-1, 10, 7])
"ali"
"""