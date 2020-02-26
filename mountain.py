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
        for trail in self.trails:
            if trail.get_name == trail_name:
                groomed = ""
                open = ""
                if trial.get_groomed == True:
                    groomed = "groomed"
                else:
                    groomed = "not groomed"
                if trail.get_open == True:
                    open = "open"
                else:
                    open = "closed"
                print(trail_name + " is currently " + groomed + " and " + open + ".")


    def lift_status(self, lift_name):
        for lift in self.lifts:
            if lift.get_name == lift_name:
                running = ""
                if lift.get_running == True:
                    running = "running"
                else:
                    running = "not running"
                print(lift_name + " is currently " + running + ".")

    def lodge_status(self, lodge_name):
        #TODO: prints a list of lodges and whether they are open and/or running food or not.
        print("TODO: prints a list of lodges and whether they are open and/or running food or not.")
        for lodge in self.lodges:
            if lodge_name == lodge.get_name:
                open = ""
                food = ""
                if lodge.get_open == True:
                    open = "open"
                else:
                    open = "closed"
                if lodge.get_food == True:
                    food = "serving food"
                else:
                    food = "not serving food"
                print(lodge_name + " is currently " + open + " and " + food + ".")

    def add_trail(self, trail):
        self.trails.append(trail)

    def remove_trail(self, trail):
        self.trails.remove(trail)

    def add_lift(self, lift):
        self.lifts.append(lift)

    def remove_lift(self, lift):
        self.lifts.remove(lift)

    def add_lodge(self, lodge):
        self.lodges.append(lodge)

    def remove_lodge(self, lodge):
        self.lodges.remove(lodge)
