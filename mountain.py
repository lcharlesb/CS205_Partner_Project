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
        print(*self.trails, sep = "\n")

    def get_lifts(self):
        print(*self.lifts, sep = "\n")

    def get_lodges(self):
        print(*self.lodges, sep = "\n")

    def trail_status(self, trail_name):
        trail_found = False
        for trail in self.trails:
            if trail.get_name == trail_name:
                trail_found = True
                groomed = ""
                open = ""
                if trail.get_groomed == True:
                    groomed = "groomed"
                else:
                    groomed = "not groomed"
                if trail.get_open == True:
                    open = "open"
                else:
                    open = "closed"
                print(trail_name + " is currently " + groomed + " and " + open + ".")
        if trail_found == False:
            print("No trail by the name of " + trail_name + " exists on this mountain.")


    def lift_status(self, lift_name):
        lift_found = False
        for lift in self.lifts:
            if lift.get_name == lift_name:
                lift_found = True
                running = ""
                if lift.get_running == True:
                    running = "running"
                else:
                    running = "not running"
                print(lift_name + " is currently " + running + ".")
        if lift_found == False:
            print("No lift by the name of " + lift_name + " exists on this mountain.")

    def lodge_status(self, lodge_name):
        lodge_found = False
        for lodge in self.lodges:
            if lodge_name == lodge.get_name:
                lodge_found = True
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
        if lodge_found == False:
            print("No lodge by the name of " + lodge_name + " exists on this mountain.")

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
