words = {}
with open('list.txt') as f:
    for l in f:
        if l:
            words[l.strip()] = True

# the alphabet. i assume repeats are possible?
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
'W', 'X', 'Y', 'Z']

exclude = {
    'Q': True,
    'U': True,
    'I': True,
    'E': True,
}
# known letters, the yellow ones,
# the '#' is a wildcard in this case.
guess = ['C', 'K', 'H', '#', '#']
known = {
    1: 'H',
    3: 'C',
    4: 'K',
}
# dictionary for uniques. i probably should have used a set
uniques = {}

def toArray(s):
    l=[]
    l[:0]=s
    return l

def remove_from_list(v, l):
    out = []
    for i in l:
        if i == v:
            continue
        out.append(i)
    return out

def permute(s, l, alpha, max_length=5):
    # start replacing the '#'s. we'll do this recursively too.
    if len(s) >= max_length:
        if '#' not in s:
            uniques[''.join(s)] = True
            return s
        else:
            for j in range(len(alpha)):
                tmp = ''.join(s)
                newT = tmp
                if j not in exclude:
                    newT = tmp.replace('#', alpha[j], 1)
                permute(toArray(newT), l, alpha)
    for i in range(len(l)):
        if len(s) in known:
            letter = known[len(s)]
            # todo: this can be better, 
            # we can make pernament adjustments
            # but i can't figure out the best way to do that atm
            tmpS = s + [letter]
            tmpl = remove_from_list(letter, l)
        else:
            tmpS = s + [l[i]]
            tmpl = l[:i] + l[i+1:]
        permute(tmpS, tmpl, alpha)
    
    return uniques

permute([], guess, alphabet)
u = []
out = []
# i could have used a set but it's too late now
for word in uniques:
    # why didnt i just use lowercase from the beginning lol
    if word.lower() in words:
        print(word)
        should_exclude = False
        for letter in word:
            if letter.upper() in exclude:
                should_exclude = True
                break
        if not should_exclude:
            out.append(word)
print(out)
exit(0)