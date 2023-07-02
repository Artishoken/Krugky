class Cup:
    def __init__(self, material, condition, charge, speed, carring_ability):
        self.material = material
        self.condition = condition
        self.charge = charge
        self.speed = speed
        self.carring_ability = carring_ability
    def check_charge(self):
        return (print ("полетели")if self.charge == 100 else print ("никуда не полетим"))
        
cup1 = Cup("картон","на земле",10,0,10)
cup1.check_charge()
        