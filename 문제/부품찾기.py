import sys
N=int(input())
gear=list(map(int,input().split()))
gear.sort()
M=int(input())
x=list(map(int,input().split()))

def binary_search(gear,start,end,target):
    if start>end:
        return None
    mid=(start+end)//2
    if target==gear[mid]:
        return mid
    elif target<gear[mid]:
        return binary_search(gear,start,mid-1,target)
    else:
        return binary_search(gear,mid+1, end, target)
for i in x:
    result = binary_search(gear,0, N-1, i)
    if result!=None:
        print('yes', end=' ')
    else:
        print('no', end=' ')
