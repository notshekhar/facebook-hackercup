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
    v_dist = {}
    c_dist = {}

    for i in range(str_len):
        s = string[i]
        
        

        if(s in vowels):
            if(s in v_dist): v_dist[s] += 1
            else: v_dist[s] = 0
            if(not s in set_vowel): n_vowels += 1
            total_vowels += 1
            set_vowel.add(s)
            continue

        if(s in c_dist): c_dist[s] += 1
        else: c_dist[s] = 0
        if(not s in set_consonants): n_consonants += 1
        total_consonants += 1
        set_consonants.add(s)
    
    if(n_vowels == 1): return total_consonants
    if(n_consonants == 1): return total_vowels
    if(n_vowels == 0 or n_consonants == 0): return str_len

    _min  = min(n_vowels, n_consonants)
    return str_len
for t in range(N):
    print("Case #{}".format(t+1), solution())

