N = int(input())

def solution():
    string = input()
    k = int(input())
    conversion = []
    for i in range(k):
        dist = input()
        conversion.append((dist[0], dist[1]))

    for i in range(k):
        for j in range(i, k):
            print(j)
            for m in range(i, j):
                print()
    return 

for t in range(N):
    print("Case #{}:".format(t+1), solution())