class Lift:
    def __init__(self, name="", running=False):
        self.name = name
        self.running = running
        self.trails = list()

    def to_string(self):
        return self.name

    def get_name(self):
        return self.name

    def get_running(self):
        return self.running

    def get_trails(self):
        for trail in self.trails:
            print(trail.name)

    def run_lift(self):
        self.running = True

    def stop_lift(self):
        self.running = False

    def add_trail(self, trail):
        self.trails.append(trail)

    def remove_trail(self, trail_name):
        for trail in self.trails:
            if trail.name == trail_name:
                self.trails.remove(trail)
