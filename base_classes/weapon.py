class Weapon:
    def __init__(self, attack, defense, start_x, start_y, name):
        self.attack = attack
        self.defense = defense
        self.x = start_x
        self.y = start_y
        self.name = name
        self.taken = False

    # updates the position of the weapon when ever knight makes a valid move
    def update_pos(self, x, y):
        self.x = x
        self.y = y

    # Called when a knight holds the weapon
    def take(self):
        self.taken = True

    # Called when the knight holding the weapon is killed
    def leave(self):
        self.taken = False

    # in case of debugging, print is automatically taken care
    def __str__(self):
        return '{} {} {} {} {} {}'.format(self.x, self.y, self.name, self.taken, self.attack, self.defense)
