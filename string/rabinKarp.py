'''
Found out of p are in side s
Run time complexity: O(mn)
'''
def rabinKarp(s,p):
    p_hash = hash (p)
    for i in range(0, len(s)-(len(p)-1)):
        s_hash = hash(s[i: i+ len(s)])
        if s_hash == p_hash and s[i:i+len(p)] == p:
            return True
    return False
    