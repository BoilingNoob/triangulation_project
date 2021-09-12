from dataclasses import dataclass


@dataclass
class Measurment:
    x: float
    y: float
    z: float
    radius: float


class data_packet:
    measurement1 = None
    measurement2 = None
    measurement3 = None
    location = None

    def __init__(self, measurement1, measurement2, measurement3, location):
        self.measurement1 = measurement1
        self.measurement2 = measurement2
        self.measurement3 = measurement3
        self.location = location
