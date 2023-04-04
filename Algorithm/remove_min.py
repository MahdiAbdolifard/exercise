"""
remove min 
    [4, 5, 2, 8, -2, 5, 1, 9] => -2
"""

def remove_min(stack:list) ->tuple:
    min_val = stack[0]
    for i in stack:
        if i < min_val:
            min_val = i
    stack.remove(min_val)
    return stack , min_val


# print(remove_min([4, 5, 2, 8, -2]))   #([4, 5, 2, 8], -2)



