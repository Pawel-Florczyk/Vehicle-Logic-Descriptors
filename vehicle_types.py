from descriptors import Counter, Tank
from errors import FuelLevelError


class Vehicle:

    mileage = Counter()
    fuel_tank = Tank()

    def __init__(
            self,
            brand: str,
            year: int,
            vin: str,
            engine_volume: int,
            max_capacity: int
    ) -> None:
        self.brand = brand
        self.year = year
        self.__vin = vin
        self.__engine_volume = engine_volume
        type(self).fuel_tank.min_capacity = 0
        type(self).fuel_tank.max_capacity = max_capacity
        self.fuel_tank = 0

    def tanking(self, liters_to_tank) -> None:
        try:
            self.fuel_tank += liters_to_tank
        except FuelLevelError as error:
            print(error)


class Car(Vehicle):

    kilometrage = Counter()

    def __init__(
            self,
            brand: str,
            year: int,
            vin: str,
            engine_volume: int,
            drivetrain: str,
            max_capacity: int
    ) -> None:
        super().__init__(
            brand,
            year,
            vin,
            engine_volume,
            max_capacity
        )
        self.drivetrain = drivetrain

    def traveling(self, traveled_kilometers: int) -> None:
        try:
            self.kilometrage += traveled_kilometers
            self.fuel_tank -= traveled_kilometers * 0.06
        except FuelLevelError as error:
            print(error)


class Motorcycle(Vehicle):

    kilometrage = Counter()

    def __init__(
            self,
            brand: str,
            year: int,
            vin: str,
            engine_volume: int,
            max_capacity: int,
            tire_type: str
    ) -> None:
        super().__init__(
            brand,
            year,
            vin,
            engine_volume,
            max_capacity
        )
        self.tire_type = tire_type

    def traveling(self, traveled_kilometers: int) -> None:
        try:
            self.kilometrage += traveled_kilometers
            self.fuel_tank -= traveled_kilometers * 0.06
        except FuelLevelError as error:
            print(error)


class CrossBike(Motorcycle):

    motor_hours = Counter()

    def __init__(
            self,
            brand: str,
            year: int,
            vin: str,
            engine_volume: int,
            max_capacity: int,
            tire_type: str
    ) -> None:
        super().__init__(
            brand,
            year,
            vin,
            engine_volume,
            max_capacity,
            tire_type
        )

    def training(self, ridden_mth: float) -> None:
        try:
            if ridden_mth * 2.5 < self.fuel_tank:
                self.motor_hours += ridden_mth
                self.fuel_tank -= ridden_mth * 2.5
            else:
                raise FuelLevelError
        except FuelLevelError as error:
            print(error)


class Superbike(Motorcycle):

    def __init__(
            self,
            brand: str,
            year: int,
            vin: str,
            engine_volume: int,
            max_capacity: int,
            tire_type: str
    ) -> None:
        super().__init__(
            brand,
            year,
            vin,
            engine_volume,
            max_capacity,
            tire_type
        )

    def free_ride(self, traveled_kilometers: int) -> None:
        try:
            self.kilometrage += traveled_kilometers
            self.fuel_tank -= traveled_kilometers * 0.1
        except FuelLevelError as error:
            print(error)
