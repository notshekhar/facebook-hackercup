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
            else: v_dist[s] = 1
            if(not s in set_vowel): n_vowels += 1
            total_vowels += 1
            set_vowel.add(s)
            continue

        if(s in c_dist): c_dist[s] += 1
        else: c_dist[s] = 1
        if(not s in set_consonants): n_consonants += 1
        total_consonants += 1
        set_consonants.add(s)
    
    if(n_vowels == 1): return total_consonants
    if(n_consonants == 1): return total_vowels
    if(n_vowels == 0 or n_consonants == 0): return str_len

    v_max_f = 0
    c_max_f = 0
    for key in v_dist:
        freq = v_dist[key]
        v_max_f = max(v_max_f, freq)

    for key in c_dist:
        freq = c_dist[key]
        c_max_f = max(c_max_f, freq)

    cal_vowel = total_vowels - v_max_f
    cal_consonant = total_consonants - c_max_f

    total_min = 0
    total_max = 0
    max_f = 0

    if(cal_vowel < cal_consonant):
        max_f = v_max_f
        total_min = total_vowels
        total_max = total_consonants
    else: 
        max_f = c_max_f
        total_min = total_consonants
        total_max = total_vowels

    return (2*(total_min-max_f)) + total_max


for t in range(N):
    print("Case #{}:".format(t+1), solution())

