
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
def main():
    numbers = [3,4,5,6,6,4,8,5,9,1,2,6]
    for i in range(10):
        print(quiclsort(numbers))
if __name__ == '__main__':
    main()