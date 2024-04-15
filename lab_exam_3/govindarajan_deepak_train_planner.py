class Locomotive:
    def __init__(self,length,max_payload,max_speed):
        self.length = length
        self.max_payload = max_payload
        self.max_speed=max_speed

        def get_length(self):
            print(f'Length: {self.length} metres.')

        def get_maximum_payload(self):
            print(f'Maximum payload: {self.max_payload} tons.')

        def get_maximum_speed(self):
            print(f'Maximum speed: {self.max_speed} mph.')

        
class Railcar:
    def __init__(self,length,cargo_type,min_weight,max_weight,capacity):
        self.length = length
        self.cargo_type = cargo_type
        self.min_weight = min_weight
        self.max_weight = max_weight
        self.capacity = capacity

    def get_length(self):
        print(f'Length: {self.length} metres.')

    def get_cargo_type(self):
        print(f'Cargo type: {self.cargo_type}.')

    def get_weight_range(self):
        print(f'Weight range: {self.min_weight} - {self.max_weight} tons.')

class Train:
    train1=([])
    def __init__(self,max_payload,max_speed,length,payload,speed,Locomotive,Railcar):
        self.max_payload = max_payload
        self.max_speed = max_speed
        self.length = length
        self.payload = payload
        self.speed = speed
        self.Locomotive = Locomotive
        self.Railcar = Railcar

    def get_length(self):
        

    def get_payload(self):

    
    def get_speed(self):

    
    def add_locomotive(locomotive):
        self.Locomotive = locomotive
        self.length += locomotive.length
        train1.append('L')

    def add_railcar(railcar):
        while self.payload + railcar.capacity <= self.max_payload:
            self.payload += railcar.capacity
            self.length += railcar.length
            self.Railcar.append(railcar)
    
    def remove_railcar(railcar):
        if railcar in self.Railcar:
            self.payload -= railcar.capacity
            self.length -= railcar.length
            self.Railcar.remove(railcar)
    
    

    

def print_train():
    print(f'Train length: {self.length} metres.')
    rint(f'Train speed: {self.speed} mph.')
    print(f'Train payload: {self.payload} tons.')
    p
