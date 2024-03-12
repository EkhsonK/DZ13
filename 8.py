k = 0
for x1 in 'ABEIKNT':
    for x2 in 'ABEIKNT':
        for x3 in 'ABEIKNT':
            for x4 in 'ABEIKNT':
                for x5 in 'ABEIKNT':
                    for x6 in 'ABEIKNT':
                        for x7 in 'ABEIKNT':
                            s = x1+x2+x3+x4+x5+x6+x7
                            alf = ['A','E','I']
                            if s.count('A') == 1 and s.count('B') == 1 and s.count('E') == 1 and s.count('I') and s.count('K') == 1 and s.count('N') and s.count('T') == 1 and s[-1] not in alf:
                                print(s)
                                k+=1
print(k)