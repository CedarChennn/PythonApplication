n = int(input())
li = {}

for i in range(n):
    m = int(input())
    for ii in range(m):
        number = int(input())
        if number in li.keys():
            li[number] += 1
        else:
            li[number] = 1
num_count = sorted(list(li.values()),reverse=False)
def rm(num_count):
    for i in range(len(num_count)):
        if i == len(num_count) - 2:
            break
        for ii in range(i+1,len(num_count)):
            if((num_count[i] + num_count[ii] in num_count) ):
                num_count.remove(num_count.index(num_count[i] + num_count[ii]))
                rm(num_count)
            if i == len(num_count) - 2:
                break
                
        
num_count = rm(num_count)
if len(num_count) == 0:
    print("YES")
else:
    print("NO")

