class Cup:
    def __init__(self, material, condition, charge, speed,speed_limit, carring_ability, containing):
        self.material = material
        self.condition = condition
        self.charge = charge
        self.speed = speed
        self.speed_limit = speed_limit
        self.carring_ability = carring_ability
        self.containing = containing 
    
    def drive(self,speed):
        self.charge-=10
        return print("ЖЖЖЖЖ-жжжж-жжж-жжж")
    def check_charge(self):
        return (print ("полетели")if self.charge == 100 else print ("никуда не полетим"))
    def power_the_cup(self, full): 
        if self.charge < 100:
           self.charge = full 
        else:
            print ("незачем зарежать") 
    def fill_cup(self):
        if self.carring_ability == self.containing:
            print ("Кружка полная")
        else:
            print ("долейте ещё", self.carring_ability - self.containing)  
    def check_speed(self):
        if self.speed == 0:
            print ("стоим на месте")
        elif self.speed < self.speed_limit:
            print ("летим")
        else:
            print ("падаем")
        
cup1 = Cup("картон","на земле",100,0,20,100,100)

cup1.check_charge()

cup1.power_the_cup(100) 
print (cup1.charge)  

cup1.fill_cup()

cup1.check_speed()
