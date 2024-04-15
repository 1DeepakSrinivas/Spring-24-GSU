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
    def __init__(self,cargo_type,min_weight,max_weight,capacity,length=20):
        self.cargo_type = cargo_type
        self.min_weight = min_weight
        self.max_weight = max_weight
        self.capacity = capacity
        self.length = length

        def get_cargo_type(self):
            return self.cargo_type

        def get_length(self):
            return self.length
        
        def get_weight(self):
            return self.min_weight + ((self.max_weight - self.min_weight) * self.capacity)

class Train:
    def __init__(self,max_payload,max_speed,length,payload,speed,Locomotive,Railcar):
        self.max_payload = Locomotive.get_maximum_payload()
        self.max_speed = 0
        self.length = 0
        self.payload = payload
        self.speed = speed
        self.Locomotive = []
        self.Railcar = []
    
    def add_locomotive(locomotive):
        train1.append(locomotive)
        self.length += locomotive.length
        self.speed = locomotive.max_speed
        self.max_speed = locomotive.max_speed
        self.max_payload = locomotive.max_payload


    def add_railcar(railcar):
        while self.payload + railcar.capacity <= self.max_payload:
            self.payload += railcar.capacity
            self.length += railcar.length
            self.Railcar.append(railcar)
        else:
            print('Payload Capcity Exceeded.')
    
    def remove_railcar(railcar):
        if railcar in self.Railcar:
            self.payload -= railcar.capacity
            self.length -= railcar.length
            self.Railcar.remove(railcar)
        else:
            print('Railcar not found.')

        
    
    


    
