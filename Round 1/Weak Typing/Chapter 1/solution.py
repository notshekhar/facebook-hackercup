T = int(input())


def solution():
    N = int(input())
    string = input()
    counter = -1
    recent = ""
    for i in range(N):
        s = string[i]
        if(s == "O" or s == "X"):
            if(not recent == s):
                recent = s
                counter += 1

    if(counter == -1):
        counter = 0

    return counter


for t in range(T):
    print("Case #{}".format(t+1), solution())
