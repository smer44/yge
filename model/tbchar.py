import numpy as np
import random

class TurnBasedCharacter:
    short_repr = False#True


    def __init__(self,name,str,dex,mstr,mdex,nn = None):
        self.name = name
        self.str = str
        self.dex = dex
        self.mstr = mstr
        self.mdex = mdex

        self.calc_basic_stats()
        self.rest_full()
        if nn is None:
            self.init_desigion_nn()
        else:
            self.nn =[np.copy(layer) for layer in nn]


    def clone(self,name):
        return TurnBasedCharacter(name, self.str,self.dex,self.mstr,self.mdex, self.nn)

    def __hash__(self):
        return hash(self.name) + hash((self.str,self.dex,self.mstr,self.mdex))

    def mate(self,other):
        name = str((hash(self) + hash(other))//2)[:5]
        nn = [(layer + other_layer)/2 for layer, other_layer in zip(self.nn, other.nn)]
        return TurnBasedCharacter(name,
                                  (self.str + other.str)/2,
                                  (self.dex + other.dex) /2,
                                  (self.mstr+ other.mstr)/2,
                                  (self.mdex +other.mdex)/2,
                                  nn)

    def mutate(self):
        stats = np.array([self.str,self.dex,self.mstr,self.mdex],dtype=np.float64)
        stats += np.random.rand(len(stats))*5
        #print(f"rnd stats {stats}")
        stats = stats / np.sum(stats) * 40.0
        #print(f"norm stats {stats}")
        self.str, self.dex, self.mstr, self.mdex = stats

    def mutate_alt(self):
        mutate_action_key = random.randint(0,5)
        mutate_fields_all = ("str","dex"),("str","mstr"),("str","mdex") , ("dex", "mstr"), ("dex", "mdex") , ("mstr" , "mdex")
        mutate_from, mutate_to = mutate_fields_all[mutate_action_key]
        mutate_from_val, mutate_to_val = getattr(self,mutate_from), getattr(self,mutate_to)
        mutate_amount = max(1,int(mutate_from_val + mutate_to_val)//5)
        mutate_amount = random.randint(-mutate_amount,mutate_amount)//2
        mutate_from_val = mutate_from_val-mutate_amount
        mutate_to_val = mutate_to_val+mutate_amount
        if True:
            if mutate_from_val < 1:
                mutate_from_val = 1
                mutate_to_val -= 1-mutate_from_val
            elif mutate_to_val < 1:
                mutate_to_val = 1
                mutate_from_val -= 1-mutate_to_val




        setattr(self,mutate_from,mutate_from_val)
        setattr(self,mutate_to,mutate_to_val)

        self.calc_basic_stats()
        self.rest_full()

    def mutate_all(self):
        self.mutate()
        self.mutate_ai()
        return self



    def calc_basic_stats(self):
        str = self.str
        dex = self.dex
        mstr = self.mstr
        mdex = self.mdex
        self.max_hp = str * 2 + mstr * 2
        self.max_sta = str+dex
        self.max_mana = mstr + mdex
        self.basic_def = str /2
        self.basic_mdef = mstr /2
        self.basic_speed = dex + mdex


    def rest_full(self):
        self.hp = self.max_hp
        self.sta = self.max_sta
        self.mana = self.max_mana
        self.pdef = self.basic_def
        self.mdef = self.basic_mdef
        self.spd = self.basic_speed

    def can_attack(self):
        return self.sta >=10

    def can_mattack(self):
        return self.mana >=15

    def attack(self,other):
        if not self.can_attack():
            self.rest(other)
            return False
        self.sta -= 10
        other_dmg = self.str - other.pdef
        other.pdef = other.basic_def
        if other_dmg > 0:
            #print(f"attack : {self.name}, dmg: {other_dmg} , to  {other.name}")
            other.hp -= other_dmg
            return True
        else:
            return False

    def mattack(self,other):
        if not self.can_mattack():
            self.rest(other)
            return False
        self.mana -= 15
        other_dmg = self.mstr*1.5-other.mdef
        other.mdef = other.basic_mdef
        if other_dmg > 0:
            other.hp -= other_dmg

            return True
        else:
            return False


    def defend(self,other):
        self.sta -= 5
        self.pdef = self.basic_def + self.str/2

    def mdefend(self,other):
        self.sta -= 7.5
        self.mdef = self.basic_mdef + self.mstr*1.5/2

    def rest(self,other):
        self.mana = min(self.max_mana,self.mana+10)
        self.sta = min(self.max_sta,self.sta+10)


    def __repr__(self):
        if self.short_repr:
            return f"{self.name}"
        return f"{self.name}:hp:{self.hp :.2f}/sta:{self.sta:.2f}/mana:{self.mana:.2f}(str:{self.str:.2f}|dex:{self.dex:.2f}|mstr:{self.mstr:.2f}|mdex:{self.mdex:.2f})[def:{self.pdef:.2f}|mdef:{self.mdef:.2f}|spd:{self.spd:.2f}]"

    def to_nn_input(self):
        return np.array([self.hp,self.sta,self.mana,self.pdef,self.mdef,self.spd])


    def init_desigion_nn(self):
        self.nn = [np.random.rand(6,10), np.random.rand(10,5)]

    def mutate_ai(self):
        for n in range(len(self.nn)):
            self.nn[n] += np.random.rand(*self.nn[n].shape)*0.05


    def decide(self,other):
        input = other.to_nn_input()
        for weights in self.nn:
            input = input @ weights
        return np.argmax(input)

    def do_as_decided(self,other,desigion,verbose = False):
        actions =[self.attack,self.mattack, self.defend, self.mdefend, self.rest]
        action = actions[desigion]
        if verbose:
            print(f"    {action.__name__}: {self} , {other}")
        action(other)


def battle_step(hero,other,verbose = False):
    desigion = hero.decide(other)
    hero.do_as_decided(other,desigion, verbose)




def battle_population(heroes):
    winners = [0 for _ in heroes]
    for n in range(len(heroes)-1):
        hero = heroes[n]
        for m in range(n, len(heroes)):
            other = heroes[m]
            hero_winner = battle_sequence(hero,other)
            id_winner = n if hero_winner else m
            winners[id_winner] +=1
            hero.rest_full()
            other.rest_full()

    return np.array(winners)

def reset_population(heroes):
    for hero in heroes:
        hero.rest_full()



def next_generation(heroes,winners):
    inds = (-winners).argsort()
    #print(f'{inds=}')
    sorted_heroes = heroes[inds[:len(inds)//2]]
    #print(f'{len(sorted_heroes)=}')
    return sorted_heroes

def random_mate(heroes):
    inds = np.arange(len(heroes))
    np.random.shuffle(inds)
    children = []
    for n in range(len(inds)):
        hero = heroes[n-1]
        other = heroes[n]
        child = hero.mate(other)
        child.mutate_all()
        children.append(child)
    children = np.array(children)
    new_heroes = np.concatenate((heroes, children))
    return new_heroes


def init_generation(hero, amount):
    others = [hero.clone(str(n)).mutate_all() for n in range(amount)]
    return np.array(others)






def battle_sequence(hero, other, verbose = False):
    if verbose:
        print(f"battle_sequence: {hero}, {other}, {hero.spd}, {other.spd},")
    turn_ballance = hero.spd - other.spd
    hero_turn = True
    counter = 100
    while hero.hp >0 and other.hp > 0 and counter > 0:
        counter -=1
        if verbose:
            print(f"battle_sequence:{turn_ballance=}")
        if turn_ballance == 0:
            if hero.spd > other.spd or hero.spd == other.spd and hero_turn:
                battle_step(hero,other,verbose)
                turn_ballance -= other.spd
                hero_turn = False
            else:
                battle_step(other,hero,verbose)
                turn_ballance += hero.spd
                hero_turn = True

        elif turn_ballance > 0 :
            battle_step(hero, other,verbose)
            turn_ballance -= other.spd
            hero_turn = False
        else:
            battle_step(other, hero,verbose)
            turn_ballance += hero.spd
            hero_turn = True
    hero_wone = other.hp <= 0
    if verbose:
        print(f"battle_sequence:END: {hero_wone=}")

    return hero_wone



def next_gen_test():
    heroes = np.array(["alice" , "bob", "chy", "dry"])
    wone = np.array([3,0,1,1])
    inds = next_generation(heroes,wone)

    print(inds)

def battle_sequence_test():
    hero = TurnBasedCharacter("hero_bst", 10,10,10,10)
    other = TurnBasedCharacter("other_bst", 15,-1,15,-1)

    battle_sequence(hero,other,True)


def evo_test():
    hero = TurnBasedCharacter("hero", 15,15,10,10)
    other = hero.clone("other")
    hero.mutate()

    heroes = init_generation(hero,32)
    loops = 100
    for n in range(loops):
        wone_count = battle_population(heroes)
        #reset_population(heroes)
        heroes_winners = next_generation(heroes,wone_count)
        #print(f"{len(heroes_winners)}")
        new_heroes = random_mate(heroes_winners)
        #print(f"{len(new_heroes)=}")
        heroes = new_heroes
        #print(new_heroes)

    print("evolution done!")
    print(heroes)
    hero, other = heroes[:2]
    print("test best heroes :")
    battle_sequence(hero, other, True)
    #example battle:



#TODO - how battle sequence works with negative speed?
evo_test()

#battle_sequence_test()











