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

def find_max_number(n):   # 给定一个数字，剔除一个后，使得剩下的数字顺序不变的情况下最大
	s = str(n)
	count = 1
	while (count<len(s)):
		if(s[count-1]>=s[count]):
			if(count==len(s)-1):
				s=s[:-1]
				break
			count+=1
		else:
			s=s[0:count-1]+s[count:]
			break
	return int(s)


def main():
	n=input("input a number")
	print(find_max_number(n))




if(__name__=="__main__"):
	main()