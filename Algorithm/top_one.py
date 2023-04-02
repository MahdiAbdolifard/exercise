"""
ورودی تابع یک لیست از المان‌ها است.
تابع تعداد تکرار هر المان در لیست را شمرده و بیشترین تعداد تکرار را برمی‌گرداند.
برای شمردن تعداد تکرار هر المان، از یک دیکشنری استفاده می‌کند.
در نهایت، بیشترین تعداد تکرار را با استفاده از مقدارهای ذخیره شده در دیکشنری محاسبه می‌کند.
"""


def top_one(numbers: list) -> str:
    counts = {}
    for number in numbers:
        if number in counts:
            counts[number] += 1
        else:
            counts[number] = 1
    max_count = 0
    max_number = None
    # print(count.items())
    for number, count in counts.items():
        if count > max_count:
            max_count = count
            max_number = number
    return f'The number {max_number} is the most repeated ({max_count} times).' 



"""
doctest

>>> top_one([1, 2, 3, 2, 2, 3, 4, 5, 5, 5, 2, 2])
"The number 2 is the most repeated (5 times)."
"""

# print(top_one([1, 2, 3, 2, 2, 3, 4, 5, 5, 5, 2]))  # (2, 3)