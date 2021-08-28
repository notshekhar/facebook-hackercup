N = int(input())

def solution():
    string = input()
    str_len = len(string)
    vowels = set(("A", "E", "I", "O", "U"))

    n_vowels = 0 
    n_consonants = 0
    set_vowel = set()
    set_consonants = set()
    total_vowels = 0
    total_consonants = 0
    dist = {}

    for i in range(str_len):
        s = string[i]
        
        if(s in dist): dist[s] += 1
        else: dist[s] = 0

        if(s in vowels):
            if(not s in set_vowel): n_vowels += 1
            total_vowels += 1
            set_vowel.add(s)
            continue
        if(not s in set_consonants): n_consonants += 1
        total_consonants += 1
        set_consonants.add(s)
    
    return dist 

for t in range(N):
    print("Case #{}".format(t+1), solution())

