class Mountain:
    def __init__(self, name="", location=""):
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
        for trail in self.trails:
            print(trail.name)

    def get_lifts(self):
        for lift in self.lifts:
            print(lift.name)

    def get_lodges(self):
        for lodge in self.lodges:
            print(lodge.name)

    def trail_status(self, trail_name):
        trail_found = False
        for trail in self.trails:
            if trail.name == trail_name:
                trail_found = True
                groomed = ""
                if trail.groomed == True:
                    groomed = "groomed"
                else:
                    groomed = "ungroomed"
                print(trail_name + " is currently " + groomed + ".")
        if trail_found == False:
            print("No trail by the name of " + trail_name + " exists on this mountain.")


    def lift_status(self, lift_name):
        lift_found = False
        for lift in self.lifts:
            if lift.name == lift_name:
                lift_found = True
                running = ""
                if lift.running == True:
                    running = "running"
                else:
                    running = "not running"
                print(lift_name + " is currently " + running + ".")
        if lift_found == False:
            print("No lift by the name of " + lift_name + " exists on this mountain.")

    def lodge_status(self, lodge_name):
        lodge_found = False
        for lodge in self.lodges:
            if lodge_name == lodge.name:
                lodge_found = True
                open = ""
                food = ""
                if lodge.open == True:
                    open = "open"
                else:
                    open = "closed"
                if lodge.food == True:
                    food = "serving food"
                else:
                    food = "not serving food"
                print(lodge_name + " is currently " + open + " and " + food + ".")
        if lodge_found == False:
            print("No lodge by the name of " + lodge_name + " exists on this mountain.")

    def add_trail(self, trail):
        self.trails.append(trail)

    def remove_trail(self, trail_name):
        for trail in self.trails:
            if trail.name == trail_name:
                self.trails.remove(trail)

    def add_lift(self, lift):
        self.lifts.append(lift)

    def remove_lift(self, lift_name):
        for lift in self.lifts:
            if lift.name == lift_name:
                self.lifts.remove(lift)

    def add_lodge(self, lodge):
        self.lodges.append(lodge)

    def remove_lodge(self, lodge_name):
        for lodge in self.lodges:
            if lodge.name == lodge_name:
                self.lodges.remove(lodge)
