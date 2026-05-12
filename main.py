from vehicle_types import Superbike


ducati = Superbike("ducati", 2027, "kfed93499j03", 450, 20, "Fast track")
ducati.fuel_tank = 5
ducati.tanking(2)
print(ducati.fuel_tank)
ducati.motor_hours = 10
print(ducati.motor_hours)
print(f"fuel level: {ducati.fuel_tank}")
