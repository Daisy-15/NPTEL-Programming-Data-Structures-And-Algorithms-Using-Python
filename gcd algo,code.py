def gcd(m,n):
    fm = []
    fn = []
    cf = []
    for i in range(1,m):
        if m%i == 0:
            fm.append(i)
    for j in range(1,n):
        if n%j == 0:
            fn.append(j)
    for k in fm:
        if k in fn:
            cf.append(k)
            
    print(cf[-1])
    
gcd(14,63)
    