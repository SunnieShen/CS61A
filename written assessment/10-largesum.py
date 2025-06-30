def large(s,n):
    #using tree recusion
    if s ==[]: return []
    elif s[0]>n: 
        return large(s[1:],n)
    else:
        first=s[0]
        with_s0=[first]+large(s[1:],n-first)
        without_s0=large(s[:1],n)
        if sum_list(with_s0)>sum_list(without_s0):
            return with_s0
        else:
            return with_s0

