def gcd(m,n):
    fm = []
    fn = []
    cf = []
    for i in range(1,m+1):
        if m%i == 0:
            fm.append(i)
    print(fm)
    for j in range(1,n+1):
        if n%j == 0:
            fn.append(j)
    print(fn)
    for k in fm:
        if k in fn:
            cf.append(k)
            
    print(cf[-1])
    
gcd(14,63)
#%%
# BETTER WAY


def gcd(m,n):
    cf = []
    for i in range(1,min(m,n)+1):
        if m%i == 0 and n%i == 0:
            cf.append(i)            
    return cf[-1]
    
gcd(14,63)
#%%

# EVEN BETTER

def gcd(m,n):
    for i in range(1,min(m,n)+1):
        if m%i == 0 and n%i == 0:
            mrcf = i            
    return mrcf
    
gcd(14,63)
#%%
# EVEN MORE BETTER

def gcd(m,n):
    for i in range(min(m,n)+1, 1, -1):
        if m%i == 0 and n%i == 0:
            print(i)
    
gcd(14,63)
#%%
# using while loop

def gcd(m,n):
    i = min(m,n)
    while(i>0):
        if m%i == 0 and n%i == 0:
            return i
        else:
            i = i-1
    
    
gcd(14,63)