class Lift:
    def __init__(self, name, running):
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
        print(*self.trails, sep = "\n")

    def run_lift(self):
        self.running = True

    def stop_lift(self):
        self.running = False

    def add_trail(self, trail):
        self.trails.append(trail)

    def remove_trail(self, trail):
        self.trails.remove(trail)
