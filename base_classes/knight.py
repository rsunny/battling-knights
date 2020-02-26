# A simple way to return the values for the direction of the movement.
moves = {
    'N': (-1, 0),
    'E': (0, 1),
    'S': (1, 0),
    'W': (0, -1)
}


class Knight:
    def __init__(self, x, y, name, limit_x=7, limit_y=7):
        self.limit_x, self.limit_y = limit_x, limit_y
        self.x, self.y = x, y
        self.name = name
        self.live = True
        self.status = 'LIVE'
        self.weapon = None

    # checks if the current position of the knight is a valid one or not
    def is_valid(self):
        if self.x < 0 or self.x > self.limit_x or self.y < 0 or self.y > self.limit_y:
            return False
        return True

    # makes the move in the requested direction and if the move is invalid, knight will
    # be killed. Also updates the position of the weapon if needed.
    def move(self, direction):
        if not self.live:
            return
        x, y = moves[direction]
        self.x += x
        self.y += y
        if not self.is_valid():
            self.killed('DROWNED')
        if self.weapon:
            self.weapon.update_pos(self.x, self.y)

    # assigns the weapon to the knight
    def get_weapon(self, weapon):
        if not self.live or self.weapon:
            return
        self.weapon = weapon
        self.weapon.take()

    # Returns the weapon used by the knight. If there is no weapon None is returned
    def weapon_name(self):
        if not self.weapon:
            return None
        return self.weapon.name

    # Actions needed to be handled when the knight is killed. Respective way of
    # getting killed is also added. Also the weapon is left if any.
    def killed(self, way='DEAD'):
        self.live = False
        self.status = way
        if self.weapon:
            self.weapon.leave()
            self.weapon = None

    # attack score of the knight is calculated with out the surprise.
    # attack_score = base attack score (1) + weapon's attack points (if there is a weapon)
    def attack_score(self):
        attack_score = 1
        if self.weapon:
            attack_score += self.weapon.attack
        return attack_score

    # defense score of the knight is calculated.
    # defense_score = base defense score (1) + weapon's defense points (if there is a weapon)
    def defense_score(self):
        defense_score = 1
        if self.weapon:
            defense_score += self.weapon.defense
        return defense_score

    # in case of debugging, print is automatically taken care
    def __str__(self):
        return '{} {} {} {} -- {}'.format(self.x, self.y, self.name, self.live, self.weapon)
