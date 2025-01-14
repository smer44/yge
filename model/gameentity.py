from yge.model.odict import OrderedDict
log = []
class GameEntity:
    """
    Basic class of any model entity in game, what has its name and value
    """
    id = 0

    def __init__(self, name, value=True):
        #print(f"Constructor called for {self.__class__.__name__}  {name}")
        self.init(name,value)
        self.init_id()

    def init(self,name,value):
        self.name = name
        self.value = value

    def init_id(self):
        self.idn = GameEntity.id
        GameEntity.id+=1


    def __hash__(self):
        return hash(self.name)

    def shallow_clone(self):
        return self.__class__(self.name,self.value)

    def get_name(self):
        return self.name

    def get_value(self):
        return self.value

    def get_displayed_value(self):
        return self.get_value()

    def tick(self, ticks):
        # Do not change with time
        msg = f"GameEntity {self.name} tick SKIPPED"
        log.append(msg)
        pass

    def __str__(self):
        return f"{self.get_name()}#{self.idn} : {self.get_value()}"


    def __repr__(self):
        return f"{self.__class__.__name__} {self.get_name()} : {self.get_value()}"

class InfluencedEntity(GameEntity):
    '''
    BAsic class of an entity, what can be influenced from
    another entity, so its modified value must be recalculated.
    Also this entity influences on its children.
    The influence function fn(value, other_value)
    takes 2 args - value of current function and other_value and returns resulting
    value, what is set into modified value
    Currently, influence modifies the value.
    So as this entity is updated, the update function for all its children is called.
    '''

    def __init__(self, name, value):
        self.init(name,value)
        self.init_id()


    def init(self, name, value):
        GameEntity.init(self,name, value)
        self.modified_value = value
        self.influences_dict = OrderedDict()
        self.children_dict = dict()


    def get_value(self):
        return self.modified_value

    def __update_children__(self):
        for child_name, child in self.children_dict.items():
            child.update_value()

    def deep_clone(self):
        clone_dict = dict()
        cloned = self.__deep_clone__(clone_dict)
        cloned.update_value()
        return cloned

    def __deep_clone__(self, clone_dict):
        '''
        Clones all dependency graph with nodes what influence
        this node, and nodes what this node influence on.
        :param clone_dict:
        :return:
        '''
        cloned = clone_dict.get(self,None)
        if cloned is None:
            cloned = self.shallow_clone()
            clone_dict[self] = cloned
            # clone influences:
            if self.tuple_influences:
                for infl_name, (infl_obj, fn) in self.influences_dict.items():
                    known_infl_obj = infl_obj.__deep_clone__(clone_dict)
                    cloned.add_influence(known_infl_obj, fn,False,False)
            else:
                for infl_name, infl_obj in self.influences_dict.items():
                    known_infl_obj = infl_obj.__deep_clone__(clone_dict)
                    cloned.add_influence(known_infl_obj,False,False)
            #clone children:
            for child_name, child_obj in self.children_dict.items():
                known_cloned_obj = child_obj.__deep_clone__(clone_dict)
                self.children_dict[known_cloned_obj.get_name()] = known_cloned_obj
        return cloned





class InfluencedSeqEntity(InfluencedEntity):
    tuple_influences = True

    def add_influence(self, other, fn, update_value = True, update_children= True):
        assert other.get_name() not in self.influences_dict
        assert self.get_name() not in other.children_dict
        #self.influences_list.append((other, fn))
        self.influences_dict[other.get_name()] = (other, fn)
        other.children_dict[self.get_name()] = self
        if update_value:
            self.update_value(update_children)

    def update_value(self, update_children= True):
        value = self.value
        for other, fn in self.influences_dict.items():
            value = fn(value, other.get_value())
        self.modified_value = value
        if update_children:
            self.__update_children__()


class InfluencedParallelEntity(InfluencedEntity):
    tuple_influences = False
    def __init__(self, name, value,fn):
        self.init(name,value, fn)
        self.init_id()

    def shallow_clone(self):
        return self.__class__(self.name,self.value,self.fn)

    def init(self, name, value,fn):
        InfluencedEntity.init(self,name,value)
        self.fn = fn


    def add_influence(self, other, update_value = True, update_children= True):
        assert other.get_name() not in self.influences_dict
        assert self.get_name() not in other.children_dict
        self.influences_dict[other.get_name()] = other
        other.children_dict[self.get_name()] = self
        if update_value:
            self.update_value(update_children)

    def update_value(self, update_children= True):
        value = self.value
        values = self.influences_dict.values()
        print(f"{self}:{self.influences_dict.kvs()=}")
        value = self.fn(value,*values)

        self.modified_value = value
        #print(f"{self} : update_value: after fn: {self.modified_value=}")
        if update_children:
            self.__update_children__()



class DynamicEntity(GameEntity):

    def __init__(self, name, value, minValue, maxValue, changePerTick):
        self.init()
        self.init_id()
        #backup starting value for object cloning:


    def init(self,name, value, minValue, maxValue, changePerTick):
        GameEntity.init(self,name, value)
        self.starting_value = value
        self.minValue = minValue
        self.maxValue = maxValue
        self.changePerTick = changePerTick



    def tick(self, ticks = 1, update_children = True):
        assert not isinstance(ticks,bool) and  isinstance(ticks,(int,float)), f"{self} : wrong {ticks=}"
        change = self.changePerTick
        #print(f" -- DynamicEntity {self.get_name()} tick with value before set_value : {self.get_value()} ,{change=} * {ticks=} {update_children=}")
        self.set_value(self.get_value() + change * ticks, update_children)
        # msg = f"DynamicEntity {self.name} tick with value after set_value : {self.get_displayed_value()}"
        #print(f" -- DynamicEntity {self.get_name()} tick with value after set_value : {self.get_value()} , {update_children=}")
        # log.append(msg)

    def set_value(self, value,update_children = True):
        #log.append(f"DynamicEntity set_value called")
        self.value = max(self.minValue, min(value, self.maxValue))
        self.update_value(update_children)


    def __repr__(self):
        return f"{self.value} ,{self.minValue} ,{self.maxValue}"


class DynamicParalellEntity(DynamicEntity, InfluencedParallelEntity):
    def __init__(self, name, value, minValue, maxValue, changePerTick, fn):
        #first init DynamicEntity, then InfluencedParallelEntity with super. init
        self.init(name, value, minValue, maxValue, changePerTick, fn)
        self.init_id()

    def init(self, name, value, minValue, maxValue, changePerTick, fn):
        DynamicEntity.init(self,name, value, minValue, maxValue, changePerTick)
        InfluencedParallelEntity.init(self,name, value,fn)

    def shallow_clone(self):
        #swap self.starting_value to self.value if you want to retain dynamic changes of variable
        return self.__class__(self.name, self.starting_value, self.minValue, self.maxValue, self.changePerTick, self.fn)



def can_stand_fn(value, hu , sle):
    #print(f"called can_stand_fn:{value} , {hu} , {sle}")
    res= hu + sle*10
    print(f"called can_stand_fn:{value} , {hu} , {sle}, {res=}")
    return res

hunger = DynamicParalellEntity("hunger", 0,0,100,10, lambda value: value)
sleepy = DynamicParalellEntity("sleepy", 0,0,200,30, lambda value : value)
canStand = InfluencedParallelEntity("canStand", 0,can_stand_fn)

canStand.add_influence(hunger,False)
canStand.add_influence(sleepy)

print(canStand)
hunger.tick()

print(canStand)
sleepy.tick()
print(canStand)
hunger.tick(1,True)
print("---")
print(hunger)
sleepy.tick(1,True)
print("---")
print(canStand)
#sleepy = DynamicEntity("sleepy", 0,0,200,30)

#TODO - deep clone test


print("--- cloned:---")

canStand_cloned = canStand.deep_clone()
print(canStand_cloned)
