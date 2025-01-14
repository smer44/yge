class OrderedDict_old(dict):
    def __init__(self, name,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.name = name
        self.keys = list()
        self.to_sort = True
        self.max_key = -1
        #self.default_step = 1

    def __setitem__(self, key, value):
        if key is None:
            key = int(self.max_key+1)
            assert self.max_key != key, f"{self}: auto advance {key=} already present"
            self.max_key = key
        else:
            assert isinstance(key,(int,float)), f"{self}: {key=} is not int"
            assert key not in self, f"{self}: {key=} already present"
            if key < self.max_key:
                self.to_sort = True
            else:
                self.max_key = key
        self.keys.append(key)
        super(OrderedDict, self).__setitem__(key, value)
        super(OrderedDict, self).__setitem__(value, key)

    def __getitem__(self, key):
        self.check_sort()
        return super(OrderedDict, self).__getitem__(key)


    def __delitem__(self, key):

        value = self[key]
        #print(f"__delitem__ {key=}, {value=}")
        if isinstance(key, (int,float)):
            self.keys.remove(key)
        else:
            self.keys.remove(value)
        super(OrderedDict, self).__delitem__(key)
        super(OrderedDict, self).__delitem__(value)

    def check_sort(self):
        if self.to_sort:
            self.keys.sort()
            self.to_sort = False


    def items(self):
        self.check_sort()
        for key in self.keys:
            yield key, super(OrderedDict, self).__getitem__(key)

    def values(self):
        self.check_sort()
        return [self[key] for key in self.keys]

    def __str__(self):
        return f"OrderedDict|{self.name}|"

    def __repr__(self):
        return f"OrderedDict|{self.name}|"

    def pp(self):
        print(f"--- { self.max_key} --- ")
        for k,v in self.items():
            print(f"{k}:{v}")

class OrderedDict(dict):
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.keys = list()
        #self.default_step = 1

    def __setitem__(self, key, value):
        if key not in self:
            self.keys.append(key)
        super(OrderedDict, self).__setitem__(key, value)



    def __delitem__(self, key):
        super(OrderedDict, self).__delitem__(key)
        self.keys.remove(key)


    def items(self):
        for key in self.keys:
            yield key, super(OrderedDict, self).__getitem__(key)

    def kvs(self):
        return [(key, self[key]) for key in self.keys]

    def values(self):
        return [self[key].get_value() for key in self.keys]

    def __str__(self):
        return f"OrderedDict|{self.keys}|"

    def __repr__(self):
        return f"OrderedDict|{self.keys}|"

    def pp(self):
        print(f"--- { self} --- ")
        for k,v in self.items():
            print(f"{k}:{v}")
