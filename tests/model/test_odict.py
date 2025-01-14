from yge.model.odict import OrderedDict

d = OrderedDict()
d.default_step = 10
d[2]= "two"
d[1] = "one"
d[None] = "three"
d[2.5] = "two half"

d.pp()
del d[1]

#print("two" in d)
#print(2 in d)
d.pp()
del d[None]
d.pp()
d[None] = "three"
d.pp()
