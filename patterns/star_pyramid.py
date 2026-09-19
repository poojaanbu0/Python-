n = int(input())
# for i in range(n):
#     # This range depends on i. When i=0, range(0) is empty!
#     for j in range(i+1): 
#         print("*",end = " ")
#     print()

#reverse - right - pyramid

# for i in range(n):
#     for j in range(n-i):
#         print("*" , end = " ")
#     print()
# reverse i
# for i in range(n,0, -1):
#     for j in range(i):
#         print("*",end = " ")
#     print()

# left pyramid

# for i in range(1,n+1):
#     print("   "*(n-i) ,end = " ")
    
#     for j in range(i):
#         print("* ",end = " ")
#     print()
# reverse-left pyramid
# for i in range(n,0,-1):
#     print(" "*(n-i) ,end = "")
#     for j in range(i):
#         print("*",end = "")
#     print()