class Vehicle:
    vehicle_count = 0
    
    def __init__(self, make, model):
        self.make = make
        self.model = model
        Vehicle.vehicle_count += 1

v1 = Vehicle('honda', 'shine')        # 0 -> 1
v2 = Vehicle('suzuki', 'hayabusa')    # 1 -> 2
v3 = Vehicle('Ola', 's1')             # 2 -> 3

print(Vehicle.vehicle_count)          # print 3