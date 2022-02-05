

################-This is a function that find the minimum number of moves to one of the favourite given numbers
def blackbox(chars,favc):
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    matrix = []
    k = 0
    i = 0
    res = 0
    
    for x in favc:
        n = alpha.index(x)
        matrix.append([])
        if n < 14:
            for y in chars:
                m = alpha.index(y)
                if m < 14:
                    if n<m:
                        matrix[k].append(m-n)
                    else: 
                        matrix[k].append(n-m)
                else:
                    if n<m:
                        if m - n > 13:
                            matrix[k].append(26 - (m-n))
                        else:
                            matrix[k].append(m-n)
                    else:
                        #which i DOUBT would happen
                        matrix[k].append(n-m)
                        
        else:
            for y in chars:
                m = alpha.index(y)
                if m < 14:
                    if m < n:
                        if n - m > 13: 
                            matrix[k].append(26-(n-m))
                        else:
                            matrix[k].append(n - m)
                    else:
                        matrix[k].append(m-n)
                else:
                    if m < n:
                        matrix[k].append(n-m)
                    else:
                        matrix[k].append(m-n)
        k += 1

    while i < len(matrix[0]):
        s = None
        for e in matrix:
            if s != None:
                s = min(s, e[i])
            else:
                s = e[i]
        res += s
        i += 1

    return [matrix,res]


print(blackbox('xyzabcdefghijklmnopqrstuvwxyz','ao'))



