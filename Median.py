arr=list(map(int,input().split()))
n=len(arr)
arr.sort()
if n%2==1:
    median= arr[n//2]
else:
    median=(arr[n//2-1]+arr[n//2])/2

print(median)
