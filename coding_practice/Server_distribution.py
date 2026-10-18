
def server_dist(process, servers):
    # server_arr = [0] * servers
    # print(server_arr)

    serv = [0 for _ in range(servers)]
    
    for i in range(len(process)):
        small = serv[0]
        index = 0
        for j in range(len(serv)):
            if serv[j] < small:
                index = j
                small = serv[j]
        serv[index] += process[i]
    print(serv)

process = list(map(int, input("enter the processes ").split()))
servers = int(input("enter the number of servers "))
server_dist(process, servers)


