# # try:
# #     x = 10 // 2
# # except:
# #     print("Error")
# # else:
# #     print("Answer =", x)

# # with open("data.txt") as f:
# #     print(f.read())

# line = [
#     "APple",
#     "\nbanana",
#     "\nmango"
# ]
# with open("data.txt","w") as f:
#     print(f.writelines(line))

# with open('data.txt','a') as f:
#     f.write('\nMango')
# with open("data.txt") as f:
#     print(f.read())
# # with open

def find_user():
    return None

user = find_user()
# Error: 'NoneType' object has no attribute 'name'
print(user.name)  
