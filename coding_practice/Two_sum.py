#two pointers

#loop 
# def twosum(arr, target):
#     for i in range(len(arr)):
#         for j in range(i+1, len(arr)):
#             if arr[i] + arr[j] == target:
#                 return [i,j]
#     return [] #indexes suming the target


#hashmap- dict python 
def twosum(arr, target):
    hashmap = {}
        
    for i in range(len(arr)):
        complement = target - arr[i]
        if complement in hashmap :
            return [i, hashmap[complement]]
        hashmap[arr[i]] = i
    # If no valid pair is found, return an empty list
    return []
arr = list (map(int , input("enter arr ").split()))
target = int(input("enter target "))
print(twosum(arr,target))
