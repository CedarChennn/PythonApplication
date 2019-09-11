import random

def quiclsort(numbers):
    if len(numbers) <= 1:
           return numbers
    left,mid,right = [],[],[]
    num = random.choice(numbers)
    for li in numbers:
        if li == num:
            mid.append(li)
        elif li < num:
            left.append(li)
        else:
            right.append(li)
    return quiclsort(left) + mid + quiclsort(right)