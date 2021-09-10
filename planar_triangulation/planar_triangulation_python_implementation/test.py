from dataclasses import dataclass

@dataclass
class Measurment:
    lattitude: float
    longitude: float
    alltitude: float
    radius: float


measurment1 = Measurment(100,100,100,0.9)