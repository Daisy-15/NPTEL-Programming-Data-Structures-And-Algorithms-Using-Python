#EUCLID'S ALGORITHM

def gcd(m,n):
    # assume m>=n
    if m < n:
        (m,n) = (n,m)
    if (m%n) == 0:
        return(n)
    else:
        return(gcd(max(n,m-n), min(n,m-n)))
    
#%%
# WHILE VERSION OF EUCLID'S ALGORITHM

def gcd_while(m,n):
    # assume m>=n
    if m < n:
        (m,n) = (n,m)
    while (m%n) != 0:
        return(gcd_while(max(n,m-n), min(n,m-n)))
    return(n)
#%%

def gcd_final(m,n):
    # assume m>=n
    if m < n:
        (m,n) = (n,m)
    if (m%n) == 0:
        return(n)
    else:
        return(gcd_final(n,m%n))
    
#%%

def gcd_final_while(m,n):
    # assume m>=n
    if m < n:
        (m,n) = (n,m)
    while (m%n) != 0:
        (m,n) = (n,m%n)
    return(n)
#%%