class Mountain:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.trails = list()
        self.lifts = list()
        self.lodges = list()

    def to_string(self):
        return self.name + ", " + self.location

    def get_name(self):
        return self.name

    def get_location(self):
        return self.location

    def get_trails(self):
        print(*self.trails, sep = "\n")

    def get_lifts(self):
        print(*self.lifts, sep = "\n")

    def get_lodges(self):
        print(*self.lodges, sep = "\n")

    def trail_status(self, trail_name):
        #TODO: prints a list of trails and whether they are open or not, as well as if they are groomed or not.
        print("TODO: prints a list of trails and whether they are open or not, as well as if they are groomed or not.")

    def lift_status(self, lift_name):
        #TODO: prints a list of lifts and whether they are running or not.
        print("TODO: prints a list of lifts and whether they are running or not.")

    def lodge_status(self, lodge_name):
        #TODO: prints a list of lodges and whether they are open and/or running food or not.
        print("TODO: prints a list of lodges and whether they are open and/or running food or not.")
