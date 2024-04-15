class Train:
    def __init__(self):
        self.locomotives = []
        self.railcars = []

    def get_length(self):
        return sum(car.get_length() for car in self.locomotives + self.railcars)

    def get_payload(self):
        return sum(car.get_weight() for car in self.railcars)

    def get_speed(self):
        max_speed = min(loco.get_maximum_speed() for loco in self.locomotives)
        max_payload = sum(loco.get_maximum_payload() for loco in self.locomotives)
        current_payload = self.get_payload()
        return max_speed * (1 - 0.5 * (current_payload / max_payload))

    def add_railcar(self, railcar):
    total_payload = self.get_payload() + railcar.get_weight()
    max_payload = sum(loco.get_maximum_payload() for loco in self.locomotives)
    
    if total_payload <= max_payload:
        self.railcars.append(railcar)
    
    if total_payload <= max_payload:
        self.railcars.append(railcar)

    def remove_railcar(self):
        if self.railcars:
            self.railcars.pop()

    def add_locomotive(self, locomotive):
        self.locomotives.append(locomotive)

    def remove_locomotive(self):
        if len(self.locomotives) > 1:
            self.locomotives.pop()

    def print_train(self):
        print(f'Payload: {self.get_payload()} tons')
        print(f'Speed: {self.get_speed()} mph')
        print(f'Length: {self.get_length()} meters')
        print('Composition:')
        for loco in self.locomotives:
            print('L', end='')
        for car in self.railcars:
            print(car.get_cargo_type()[0], end='')
        print()

train1 = Train()

# Create locomotives
locomotive1 = Locomotive(max_speed=120, max_payload=20000)
locomotive2 = Locomotive(max_speed=100, max_payload=15000)

# Add locomotives to the train
train1.add_locomotive(locomotive1)
train1.add_locomotive(locomotive2)

# Create railcars
railcar1 = Railcar(weight=5000, cargo_type='coal')
railcar2 = Railcar(weight=7000, cargo_type='oil')

# Add railcars to the train
train1.add_railcar(railcar1)
train1.add_railcar(railcar2)