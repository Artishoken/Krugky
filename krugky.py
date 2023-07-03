class Cup:
    def __init__(self, material, condition, charge, speed, speed_limit, carring_ability, containing, x, y, z):
        self.material = material
        self.condition = condition
        self.charge = charge
        self.speed = speed
        self.speed_limit = speed_limit
        self.carring_ability = carring_ability
        self.containing = containing
        self.x = x
        self.y = y
        self.z = z

    def drive(self, speed):
        self.charge -= 10
        return print("ЖЖЖЖЖ-жжжж-жжж-жжж")

    def check_charge(self):
        return (print("полетели") if self.charge < 50 else print("никуда не полетим"))

    def power_the_cup(self, full):
        if self.charge < 100:
            self.charge = full
        else:
            print("незачем заряжать")

    def fill_cup(self):
        if self.carring_ability == self.containing:
            print("Кружка полная")
        else:
            print("долейте ещё", self.carring_ability - self.containing)

    def check_speed(self):
        if self.speed != 0:
            print("стоим на месте")
        elif self.speed < self.speed_limit:
            print("летим")
        else:
            print("падаем")

    def check_line(self):

        # Имитация движения и сравнение координат
        for _ in range(10):
            # Имитация движения (пример: изменение координат на случайную величину)
            cup1.x += 1
            cup1.y += 1
            cup1.z += 1

            cup2.x += 2
            cup2.y += 2
            cup2.z += 2

            # Сравнение координат и проверка столкновения
            if (
                    abs(cup1.x - cup2.x) == 0 and
                    abs(cup1.y - cup2.y) == 0 and
                    abs(cup1.z - cup2.z) == 0
            ):
                print("Столкновение произошло!")
                self.speed = 21
                self.check_speed()
                return False

            # Дополнительные действия при отсутствии столкновения
            else:
                # Вывод текущих координат кружек
                print("Координаты cup1:", cup1.x, cup1.y, cup1.z)
                print("Координаты cup2:", cup2.x, cup2.y, cup2.z)
                return True

cup1 = Cup(material="картон",
           condition="на земле",
           charge=100,
           speed=10,
           speed_limit=20,
           carring_ability=100,
           containing=100,
           x=5, y=5, z=5)
cup2 = Cup(material="картон",
           condition="на земле",
           charge=100,
           speed=10,
           speed_limit=20,
           carring_ability=100,
           containing=100,
           x=0, y=0, z=0)

cup1.check_charge()

cup1.power_the_cup(100)
print(cup1.charge)

cup1.fill_cup()
distance = 100
cup1.check_speed()
while True :
    if cup1.check_line():
        distance -= 10
        cup1.drive(100)
        print(cup1.charge, distance)
    else:
        break


