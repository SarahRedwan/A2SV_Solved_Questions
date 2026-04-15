from collections import Counter

T = int(input())
for _ in range(T):
    s = input().strip()
    t = input().strip()    
    if len(t) < len(s):
        print("Impossible")
        continue
    
    ct = Counter(t)
    cs = Counter(s)
    if any(ct[c] < cs[c] for c in cs):
        print("Impossible")
        continue
    
    extra = []
    for c in 'abcdefghijklmnopqrstuvwxyz':
        extra.extend([c] * (ct[c] - cs.get(c, 0)))
    
    ans = []
    i = 0 
    j = 0  
    
    while i < len(s) or j < len(extra):
        if i == len(s):
            ans.append(extra[j])
            j += 1
            continue
        if j == len(extra):
            ans.append(s[i])
            i += 1
            continue
        
        x = s[i]
        y = extra[j]
        
        if x < y:
            ans.append(x)
            i += 1
        elif y < x:
            ans.append(y)
            j += 1
        else:
            p = i
            q = j
            while p < len(s) and q < len(extra) and s[p] == extra[q]:
                p += 1
                q += 1
            
            if p == len(s):
                ans.append(y)
                j += 1
            elif q == len(extra):
                ans.append(x)
                i += 1
            else:
                z = s[p]
                w = extra[q]
                if z < w:
                    ans.append(x)  
                    i += 1
                else:
                    ans.append(y) 
                    j += 1
    
    print(''.join(ans))