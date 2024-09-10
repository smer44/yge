
def myrange(a,b,step=1):
    if a <= b:
        return range(a,b+1,step)
    return range(a, b-1, -step)