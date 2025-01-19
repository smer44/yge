

speeds = [15,10,7,5,3,1]
speeds = [20,10,5]

order_by_min = [1/s for s in speeds]

def argmin(list, starting_min = 1000000):
    xmin = starting_min
    ret = -1
    for n,x in enumerate(list):
        if x < xmin:
            xmin = x
            ret = n
    return ret



def step(order_by_min, speeds):
    pos_min = argmin(order_by_min)
    val_min = 1/speeds[pos_min]
    #decrease all values on pos_min, except given one:
    for n in range(pos_min):
        order_by_min[n] -= val_min
    for n in range(pos_min+1,len(order_by_min)):
        order_by_min[n] -= val_min
    return order_by_min

def movement_loop(order_by_min,speeds):
    for _ in range(10):
        pos_min = argmin(order_by_min)
        print(f"position {pos_min} is moving with speed {speeds[pos_min]}")
        step(order_by_min,speeds)


movement_loop(order_by_min,speeds)

# now named example:
names = "eagle rabbit dog cat human snail".split()
kw = list( (k,1/w) for k,w in zip(names,speeds))
kw_dict= {k:1/w for k,w in zip(names,speeds)}
print(kw)

def step(kw,kw_original):
    kw.sort(key=lambda t: -t[1])
    print("order : " , kw)
    name,val = kw[-1]
    val2 =  val + kw_original[name]
    kw[-1] = (name,val2)
    print(kw)
    return name

print("--- object ref test --- ")
for _ in range(10):
    print(step(kw,kw_dict))
