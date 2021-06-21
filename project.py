def bin_search(list1,n):
    low=0
    high=len(list1)-1
    mid=0
    while low<=high:
        mid=(high+low)//2
        if list1[mid] < n:
            low=mid+1
        elif list1[mid] > n:
            high=mid-1
        else:
            return mid
    return -1
list1=[10,56,7,8,45,34,23]
n=34
result=bin_search(list1,n)
if result!=-1:
    print("element is present at index",str(result))
else:
    print("element is not present")