k = int(input())
arr = []
num = 0
for i in range(k):
	num = int(input())
	if num==0:
		arr.pop()
		continue
	arr.append(num)
ans=0
for i in range(len(arr)):
	ans += arr[i]

print(ans)