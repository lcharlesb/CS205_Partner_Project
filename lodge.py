class Lodge:
    def __init__(self, name, open, food):
        self.name = name
        self.open = open
        self.food = food

    def to_string(self):
        return self.name

    def get_name(self):
        return self.name

    def get_open(self):
        return this.open

    def get_food(self):
        return this.food

    def open_lodge(self):
        self.open = True

    def close_lodge(self):
        self.open = False

    def open_food(self):
        self.food = True

    def close_food(self):
        self.food = False
