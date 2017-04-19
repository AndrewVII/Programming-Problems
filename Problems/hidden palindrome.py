a = input()
longest = [1]

for i in range(len(a)):
    for ii in range(i,len(a)):
        print(a[i:ii+1])
        print(a[i:ii+1][::-1])
        if (list(a[i:ii+1]) == list(a[i:ii+1])[::-1]):
            longest.append(len(a[i:ii+1]))
print(max(longest))
        
