def possible_melee_targets_disciples(hero, team, other_team):
    """
    selects available target for meelee strike according to disciples rules.
    Can hit opposite cell and its neighbours, if opposite cell is occupied.
    if opposite cell is not occupied, can hit two nearest cells to left and to right
    in the front row of the enemy.

    """
    # if i stay in not minimum row in own team, it is impossible to meelee
    x, y = hero
    min_x = min(x for (x, y) in team)
    if x > min_x:
        return []
    front_row_x = min(x for (x, y) in other_team)
    #strikes opposite cell:
    cell = (front_row_x,y)
    if cell in other_team:
        #return cell and its neighbours in the front row
        ret = [cell]
        cell2 = (front_row_x,y+1)
        cell3 = (front_row_x, y - 1)
        if cell2 in other_team:
            ret.append(cell2)
        if cell3 in other_team:
            ret.append(cell3)
    else:
        ret = []
        #choose two neighbours, if present, in front row what are
        #the closest to given y-pos of the character.
        y_max_start = 1000000
        y_min_start = - 1000000
        y_max = y_max_start
        y_min = y_min_start
        y_hero = y
        for x,y in other_team:
            if x == front_row_x:
                if y_hero < y and y < y_max:
                    y_max = y
                if y_hero > y and y > y_min:
                    y_min = y
        if y_max != y_max_start:
            ret.append( (front_row_x, y_max))
        if y_min != y_min_start:
            ret.append( (front_row_x, y_min))
    return ret



enemy_team = {(1,0) : "ork_archer" ,
                        (0,2) : "ork_berserker" ,
                        (0,1) : "ork_grunt" ,
                        (1,2) : "ork_shaman"
                        }



hero_team = {(0,0): "ratman",
                        (0,2): "fighter",
                        (1,1): "arcane_gunner",
                        (1,0): "inquisitor"
                        }

for hero in hero_team:
    targets = possible_melee_targets_disciples(hero, hero_team, enemy_team)
    print(f" targets for hero : {hero_team[hero]} : {list(enemy_team[t] for t in targets)}")

for hero in enemy_team:
    targets = possible_melee_targets_disciples(hero, enemy_team, hero_team)
    print(f" targets for hero : {enemy_team[hero]} : {list(hero_team[t] for t in targets)}")