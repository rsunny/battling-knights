

# Knight class's attack_score and defense_Score member functions calculate the
# respective scores, so we just need to compare them. For the attacker surprise
# score is not handled by attack_score, so 0.5 is added.
def fight(attacker, defender):
    attack_score = attacker.attack_score() + 0.5
    defense_score = defender.defense_score()
    return attack_score > defense_score


# Iterates through all weapons and checks if there is any non taken weapon
# in the current position of the knight, so that can be grabbed.
# In case of multiple weapons in the same position, the first found
# weapon is taken and quits the search. It is fine because the loop is
# iterated in the respective precedence manner.
def check_possible_weapon(knight, weapons):
    for weapon in weapons.values():
        if weapon.taken:
            continue
        if weapon.x == knight.x and weapon.y == knight.y:
            knight.get_weapon(weapon)
            break


# Iterates through all knights who are alive and if there is someone in
# current position, fight is picked and stronger one lives.
def check_possible_fight(knight, knights):
    for other in knights.values():
        if not other.live:
            continue
        if knight.name == other.name:
            continue
        if knight.x == other.x and knight.y == other.y:
            if fight(knight, other):
                other.killed()
            else:
                knight.killed()
            break


def process_knight(knight, direction, knights, weapons):
    knight = knights[knight]
    knight.move(direction)  # makes the move for the knight
    if not knight.live:  # if the knight is killed nothing happens
        return
    if not knight.weapon:  # if the knight doesn't have a weapon checks if the current position have any
        check_possible_weapon(knight, weapons)
    check_possible_fight(knight, knights)  # checks if there is any other knight in the current position to fight
