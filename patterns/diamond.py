n = int(input())
for i in range(n): 
    print(" "* (n -i) + "* "*i)

for k in range(n,0,-1):
   print(" "* (n-k) + "* "*k)