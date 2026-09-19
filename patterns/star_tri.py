n = int(input())
# for i in range(1,n+1):
#     print(" "* (n -i),end=" ")
#     for j in range(1, i+1):
#         print("*",end= " ")
#     print()
    
# HOLLOW TRIANGLE REVERSE
# for i in range(n,0,-1):
#     for j in range(i,n):
#         print(" ",end = "")
#     for k in range(1,2*i):
#         if (k==1 or k== 2*i-1 or i ==n):
#             print("*",end = "")
#         else:
#             print(" ",end = "")
#     print()

# HOLLOW DIAMOND
# for i in range(1,n+1):
#     for j in range(i,n):
#         print(" ",end = "")
#     for k in range(1,2*i):
#         if (k==1 or k== 2*i-1 ):
#             print("*",end = "")
#         else:
#             print(" ",end = "")
#     print()
# for i in range(n-1,0,-1):
#     for j in range(i,n):
#         print(" ",end = "")
#     for k in range(1,2*i):
#         if (k==1 or k== 2*i-1 ):
#             print("*",end = "")
#         else:
#             print(" ",end = "")
#     print()

# HOLLOW HOURGLASS
# for i in range(1,n+1):
#     for j in range(1,i):
#         print(" ",end = "")
#     for k in range(i,n+1):
#         if (i==1 or k==n or k ==i):
#             print("* ",end = "")
#         else:
#             print(" ",end = " ")
#     print()
# for i in range(n-1,0,-1):
#     for j in range(1,i):
#         print(" ",end = "")
#     for k in range(i,n+1):
#         if (i==1 or k==n or k ==i):
#             print("* ",end = "")
#         else:
#             print(" ",end = " ")
#     print()

# K SHAPE
for i in range(n):
    for j in range(n-i):
        print("*" , end = " ")
    print()
# reverse i
for i in range(n-1,-1,-1):
    for j in range(n-i):
        print("*",end = " ")
    print()