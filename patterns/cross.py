n = int(input())

for i in range(n):
    for j in range(n):
        # if i==j or i+j == n-1 :
        #     print("* ",end = " ")
        if i == 0 or i == n-1 or j == 0 or j == n-1 or i==j or i+j == n-1 :
                print("*", end =" ")
        else:
            print(" ",end = " ")
    print()

# for i in range(n):
#     for j in range():
#         if i==j:
#             print("*",end = " ")
#         elif i+j == 4:
#             print("*",end = " ")
#         else:
#             print(" ",end = " ")
#     print()