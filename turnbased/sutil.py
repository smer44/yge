
def myrange(a,b,step=1):
    if a <= b:
        return range(a,b+1,step)
    return range(a, b-1, -step)

def arange(a,b,step):
    while a <b:
        yield a
        a+=step

def to_enum(enum_list, value , *values):
    assert enum_list and len(enum_list) == len(values)
    for n,v in enumerate(values):
        if value < v:
            return enum_list[n]
    return enum_list[-1]



def copy_missing_keys(d_to, d_from,):
    missing_keys = d_from.keys() - d_to.keys()
    for key in missing_keys:
        d_to[key] = d_from[key]
    return d_to


def remove_noholes(lst,n):
    last = lst.pop()
    lst[n] = last

def typecheck(msg,*args_then_types):
    assert(len(args_then_types) %2 == 0), f"typecheck: missing arguments: {args_then_types}"
    for n in range(0,len(args_then_types),2):
        arg = args_then_types[n]
        tp = args_then_types[n+1]
        if not isinstance(arg, tp):
            return msg
    return None

