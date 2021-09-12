T = int(input())

def count_switch(string):
    N = len(string)
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

def solution():
    N = int(input())
    string = input()
    sum = 0
    for i in range(N):
        for j in range(i, N):
            str = ""
            for k in range(i, j+1):
                str += string[k]
            sum += count_switch(str)
    return sum 

for t in range(T):
    print("Case #{}".format(t+1), solution())
