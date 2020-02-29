class Trail:
    def __init__(self, name="", difficulty=0, groomed=False):
        self.name = name
        self.difficulty = difficulty
        self.groomed = groomed
        self.lifts = list()

    def to_string(self):
        return self.name + ", " + self.difficulty

    def get_name(self):
        return self.name

    def get_difficulty(self):
        return self.difficulty

    def get_groomed(self):
        return self.groomed

    def get_lifts(self):
        for lift in self.lifts:
            print(lift.name)

    def groom_trail(self):
        self.groomed = True

    def add_lift(self, lift):
        self.lifts.append(lift)

    def remove_lift(self, lift_name):
        for lift in self.lifts:
            if lift.name == lift_name:
                self.lifts.remove(lift)
