class Bus:

    def __init__(self, route_number, destination):
        self.route_number = route_number
        self.destination = destination
        self.passengers = []
        
    def drive(self):
        return "Brum brum"
    
    def passenger_count(self):
        return len(self.passengers)

    def pick_up(self, passenger_to_pick_up):
        self.passengers.append(passenger_to_pick_up)
    
    def drop_off(self, passenger_to_drop_off):
        self.passengers.remove(passenger_to_drop_off)

    def empty_bus(self):
        self.passengers.clear()

    

