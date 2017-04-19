a = list(input())
b = int(input())
lowest = []
if a.count(min(a)) > 1:
    nums = [i for i,  x in enumerate(a) if x == min(a)]
    for i in range(len(nums)):
        if nums[i]+b < len(a):
            lowest.append(''.join(a[nums[i]:nums[i]+b]))
        else:
            break
    lowest.sort()
    print(lowest[0])
else:
    print(''.join(a[a.index(min(a)):a.index(min(a))+b]))
         


    

