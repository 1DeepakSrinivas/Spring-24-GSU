class Train:
    def __init__(self):
        self.locomotives = []
        self.railcars = []
        self.length = 0

    def add_locomotive(self, locomotive):
        self.locomotives.append(locomotive)
        self.length += locomotive.get_length()

    def add_railcar(self, railcar):
        self.railcars.append(railcar)
        self.length += railcar.get_length()