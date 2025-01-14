# in a Person class you make over and over following calculations.
# Also do not make it too complicated.
import pprint as pp

def bounded(min_value, max_value, value):
    return max(min_value, min(value, max_value))


def project(x1, x2, y1, y2, y_value):
    '''
    Linear projection of a value.
    If  intimacy_stage is from 0 to 1,
    and stage multiplier is from x1= 0.7 (early) to x2= 1.3 ( late)
    then compute
    0.7 + (1.3-0.7) / (1 -0)  * value
    To get projected multiplier value

    '''

    return x1 + (y2 - y1) /(x2 - x1)  * y_value


def discrete(value, *levels_and_enum):
    '''Discretisation of a value.
        Having input like
    '''

    for level, enum in levels_and_enum:
        if value >= level:
            return enum
    return levels_and_enum[-1][1]


def dot(v1, v2):
    '''
    Copmutes scalar proruct, a1*b1+a2*b2+a3*b3... for 2 vectors.
    '''
    return sum(v1[n] * v2[n] for n in range(len(v1)))


class ObjDict(dict):

    def __init__(self,*args,**kwargs):
        dict.__init__(self,*args,**kwargs)

    def __getattr__(self, item):
        return self[item]

    def __setattr__(self, key, value):
        self[key] = value

    def __delattr__(self, item):
        del self[item]


class PersonLikes(ObjDict):

    #entities = "energetic_talk calm_talk chat_books chat_movies chat_it flirt dance_classic dance_salsa dance_disco dance_hiphop dance_breakdance joke horny politeness rudeness abuse_other abuse_self listen_jazz rock pop techno classic"

    def __init__(self,*args,**kwargs):
        ObjDict.__init__(self,*args,**kwargs)



#this should be more readable then basic dict?
shy_girl = PersonLikes()
shy_girl.unknown_person = -2
shy_girl.known_person = 1
shy_girl.energetic_talk = -5
shy_girl.polite_talk = 2
shy_girl.chat_books = 5# yep, book nerd
shy_girl.chat_movies = 0
shy_girl.chat_it = 15#secret - is a it - nerd
shy_girl.sweet_flirt = 10
shy_girl.horny_flirt = -5# is shy
shy_girl.rude_flirt = -15

shy_girl.dance_classic = 0
shy_girl.dance_salsa = -2
shy_girl.dance_jazz = 15 # secret - she went to jazz dance as child, then stopped but she likes it even now.
shy_girl.dance_hiphop = -5
shy_girl.dance_breakdance = -10
shy_girl.polite_joke = 2
shy_girl.rude_joke = -5
shy_girl.horny_joke = -2

shy_girl.abuse_other = -5
shy_girl.abuse_self = -10
#rock pop techno classic
shy_girl.listen_jazz = 15 # secret
shy_girl.listen_salsa = 2
shy_girl.listen_rock = -3
shy_girl.listen_pop = -1
shy_girl.listen_techno = -5
shy_girl.listen_classic = 5



punk_girl = PersonLikes()
punk_girl.buy_drink = -5# bitch i can buy shit for myself!
punk_girl.unknown_person = 3# likes meeting new ppl
punk_girl.known_person = -1# boring
punk_girl.energetic_talk = 5
punk_girl.polite_talk = -3
punk_girl.chat_books = -5# boring
punk_girl.chat_movies = -5
punk_girl.chat_it = -15#srsly, us punk girl ?
punk_girl.sweet_flirt = -5
punk_girl.horny_flirt = -2
punk_girl.rude_flirt = 10 # yeah, bitch!

punk_girl.dance_classic = -15# omg in no way dud i m not a grandma
punk_girl.dance_salsa = -2
punk_girl.dance_jazz = 3 # well if it is energetic funk...
punk_girl.dance_hiphop = 7# yeah, bitches!
punk_girl.dance_breakdance = 15# yeeeeeaaaaaah, bitches!
punk_girl.polite_joke = -2# boring!
punk_girl.rude_joke = 10
punk_girl.horny_joke = -2

punk_girl.abuse_other = 5#who does not?
punk_girl.abuse_self = 15#secret
#generally hates listen to boring shit.
punk_girl.listen_jazz = -5
punk_girl.listen_salsa = -5
punk_girl.listen_rock = 15
punk_girl.listen_pop = -5
punk_girl.listen_techno = -5
punk_girl.listen_classic = -15


vip_girl = PersonLikes()
vip_girl.unknown_person = -1
vip_girl.buy_drink = 2# at least some manners!
vip_girl.known_person = -1
vip_girl.energetic_talk = 1
vip_girl.polite_talk = -1
vip_girl.chat_books = -1# boring
vip_girl.chat_movies = 15# secret - likes soap opera
vip_girl.chat_it = -5#srsly, us vip_girl girl ?
vip_girl.sweet_flirt = 3
vip_girl.horny_flirt = 10
vip_girl.rude_flirt = -10 # bad idea.

# do not likes to dance, escept....
vip_girl.dance_classic = -5# omg in no way dud i m not a grandma
vip_girl.dance_salsa = 15# secret
vip_girl.dance_jazz = -5 # well if it is energetic funk...
vip_girl.dance_hiphop = -5
vip_girl.dance_breakdance = -7
vip_girl.polite_joke = 0#
vip_girl.rude_joke = -10
vip_girl.horny_joke = 15#secret

vip_girl.abuse_other = 5#who does not?
vip_girl.abuse_self = -15# bad idea
#
vip_girl.listen_jazz = -5
vip_girl.listen_salsa = -5
vip_girl.listen_rock = -5
vip_girl.listen_pop = 5
vip_girl.listen_techno = 15# secret
vip_girl.listen_classic = -5


gold_digger = PersonLikes()
gold_digger.unknown_person = 15#how rich is he?
gold_digger.known_person = 0 # knows that he is not rich

#wrong topics
gold_digger.chat_shopping= 5#
gold_digger.buy_drink = 5# nice pet!
gold_digger.chat_books = -5#
gold_digger.chat_movies = -5# secret - likes soap opera
gold_digger.chat_it = -15#srsly, us gold_digger girl ?
gold_digger.chat_own_business = 15# gold sack found!
gold_digger.sweet_flirt = 0#does not care
gold_digger.horny_flirt = 0#does not care
gold_digger.rude_flirt = -10 # bad idea.

# Generally do not likes to dance
gold_digger.dance_classic = -5# omg in no way dud i m not a grandma
gold_digger.dance_salsa = -5#
gold_digger.dance_jazz = -5 # well if it is energetic funk...
gold_digger.dance_hiphop = -5
gold_digger.dance_breakdance = -15 # really?
gold_digger.polite_joke = 0#does not care
gold_digger.rude_joke = -10
gold_digger.horny_joke = 0#does not care


gold_digger.abuse_other = 0#does not care
gold_digger.abuse_self = -15# bad idea

#Does not have specific music taste
gold_digger.listen_jazz = -5
gold_digger.listen_salsa = -5
gold_digger.listen_rock = -5
gold_digger.listen_pop = -5
gold_digger.listen_techno = -5# secret
gold_digger.listen_classic = -5

#pp.pprint(gold_digger)

class NamedHashObj:
    def __init__(self, name):
        self.name = name

    def __str__(self, name):
        assert isinstance(name, str)
        self.name = name

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return self.name




class DesigionInSituation(NamedHashObj,ObjDict):

    #entities = "energetic_talk calm_talk chat_books chat_movies chat_it flirt dance_classic dance_salsa dance_disco dance_hiphop dance_breakdance joke horny politeness rudeness abuse_other abuse_self listen_jazz rock pop techno classic"

    def __init__(self,name, *args,**kwargs):
        NamedHashObj.__init__(self,name)
        ObjDict.__init__(self,*args,**kwargs)


    def finalize(self):
        self.temp = {k:1/v for k,v in self.items() if isinstance(v,(int,float))}


    def decide(self):
        #get fastest pair:
        key, value = min(self.temp.items(), key=lambda item: item[1])
        print("doing:",key)
        self.temp[key] += 1/self[key]


class TextSequence(list):

    def __add__(self, other):
        assert isinstance(other, str)
        self.append(other)
        pos = 0

    def next(self):
        if self.pos < len(self):
            text = self[self.pos]
            self.pos+=1
            return text
        else:
            return None

    def pp(self):
        for text in self:
            print(text)





# this are actions just
shy_girl_on_date = DesigionInSituation("shy_girl_on_date")
shy_girl_on_date.be_shy = 13
shy_girl_on_date.chat_it = 11
shy_girl_on_date.small_talk = 5
shy_girl_on_date.play_intelectual_game = 7
shy_girl_on_date.smart_talk = 9
shy_girl_on_date.ask_for_dance = 3

shy_girl_on_date.finalize()

for _ in range(25):
    #print(shy_girl_on_date.temp)
    shy_girl_on_date.decide()
print(shy_girl_on_date.temp)

#TODO - this are not single phrases, but the text sequences/labels what are triggered, so each of this is small dialogue fragment.
#TODO - There must be object what represent players menu choises
shy_girl_on_first_date_be_shy = TextSequence()
shy_girl_on_first_date_be_shy + "He... hello, nice to meet you!"
shy_girl_on_first_date_be_shy + "I like it here, it is such cozy place...i mean... when there aren't too many people..."
shy_girl_on_first_date_be_shy + "You know, I... um... usually stay home or go somewhere with friends."


shy_girl_on_first_date_chat_it = TextSequence()
shy_girl_on_first_date_chat_it + "I go here sometimes to work on the laptop."
shy_girl_on_first_date_chat_it + "The Wifi of the corporate building nearby is in the reach here... emm.. nevermind"
shy_girl_on_first_date_chat_it + "Don't think anything weird about me, i just  use Aircrack-ng to hijack those building's Wifi so i can work online from here."

#shy_girl_on_first_date_smart_talk = TextSequence()
##shy_girl_on_first_date_smart_talk +

shy_girl_on_first_date_chat_it.pp()


#



