class Locomotive:
    def __init__(self,max_payload,max_speed,length=23):
        self.length = length
        self.max_payload = max_payload
        self.max_speed=max_speed

    def get_length(self):
        return self.length

    def get_maximum_payload(self):
        return self.max_payload

    def get_maximum_speed(self):
        return self.max_speed


class Railcar:
    def __init__(self, cargo_type, min_weight, max_weight, capacity, length=20):
        self.length = length
        self.cargo_type = cargo_type
        self.min_weight = min_weight
        self.max_weight = max_weight
        self.capacity = capacity

    def get_length(self):
        return self.length

    def get_cargo_type(self):
        return self.cargo_type

    def get_weight(self):
        return self.min_weight + self.capacity * (self.max_weight - self.min_weight)


class Train:
    def __init__(self):
        self.locomotives = []
        self.railcars = []

    def get_length(self):
        total_length = 0
        for loco in self.locomotives:
            total_length += loco.get_length()
        for car in self.railcars:
            total_length += car.get_length()
        return total_length

    def get_payload(self):
        payload = 0
        for car in self.railcars:
            payload += car.get_weight()
        return payload

    def get_speed(self):
        slowest_loco_speed = min(loco.get_maximum_speed() for loco in self.locomotives)
        total_payload = self.get_payload()
        return slowest_loco_speed * (1 - 0.5 * total_payload / slowest_loco_speed)

    def add_railcar(self, railcar):
        total_payload = self.get_payload()
        total_loco_payload = sum(loco.get_maximum_payload() for loco in self.locomotives)
        if total_payload + railcar.get_weight() <= total_loco_payload:
            self.railcars.append(railcar)

    def remove_railcar(self):
        if len(self.railcars) > 0:
            self.railcars.pop()

    def add_locomotive(self, locomotive):
        self.locomotives.append(locomotive)

    def remove_locomotive(self):
        if len(self.locomotives) > 1:
            self.locomotives.pop()
        else:
            print('Cannot remove locomotive.')

    def print_train(self):
        print(f'Payload: {self.get_payload()} tons')
        print(f'Speed: {self.get_speed()} mph')
        print(f'Length: {self.get_length()} meters')
        composition=[]
        for loco in self.locomotives:
            composition.append('L')
        for car in self.railcars:
            if car.get_cargo_type() == 'Passenger':
                composition.append('P')
            elif car.get_cargo_type() == 'Freight':
                composition.append('F')
        
        for i in range(len(composition)):
            print(f".{composition[i]}",end='.')


train1=Train()

loco1=Locomotive(100,100)
loco2=Locomotive(200,200)

railcar1=Railcar('Passenger',10,20,0.5)
railcar2=Railcar('Freight',20,40,0.5)

train1.add_locomotive(loco1)
train1.add_locomotive(loco2)

train1.add_railcar(railcar1)
train1.add_railcar(railcar2)

train1.print_train()

