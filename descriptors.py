from errors import FuelLevelError


class Counter:
    def __init__(self) -> None:
        self.name = None

    def __set_name__(self, owner, name: str) -> None:
        self.name = "_" + name

    def __get__(self, instance, owner) -> float | Counter:
        if instance is None:
            return self
        value = getattr(instance, self.name, 0)
        print(f"Reading...\n {self.name}: {value}")
        return value

    def __set__(self, instance, new_value) -> None:
        old_value = getattr(instance, self.name, 0)
        if new_value < old_value:
            raise ValueError("Odometer rollback is not allowed.")
        else:
            setattr(instance, self.name, new_value)
            print(f"Odometer successfully set to: {new_value}")


class Tank:
    def __init__(
            self,
            min_capacity: int = 0,
            max_capacity: int = 100
    ) -> None:
        self.min_capacity = min_capacity
        self.max_capacity = max_capacity

    def __set_name__(self, owner, name):
        self.storage_name = "_" + name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        fuel_level = getattr(instance, self.storage_name, 0)
        return fuel_level

    def __set__(self, instance, new_fuel_level):
        try:
            new_fuel_level = int(new_fuel_level)
        except ValueError:
            raise ValueError("Type must be an integer")
        else:
            if self.min_capacity <= new_fuel_level <= self.max_capacity:
                setattr(instance, self.storage_name, new_fuel_level)
            else:
                raise FuelLevelError(
                    f"Capacity must be between"
                    f" {self.min_capacity} and {self.max_capacity}!"
                )
