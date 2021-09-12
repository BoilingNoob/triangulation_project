#import classes.py
import numpy as np
import random as rand
from planar_triangulation_lib import classes as planar_classes


def distance_between_points_with_z(Measurement1,Measurement2):
	x_diff = Measurement1.x - Measurement2.x
	y_diff = Measurement1.y - Measurement2.y
	z_diff = Measurement1.z - Measurement2.z

	distance = (x_diff ** 2 + y_diff**2 + z_diff**2) ** (1/2)
	
	return distance

def generate_data(location = None,range = 1000):
	rand.seed()
	#range = 1000000
	
	if location == None:
		location = planar_classes.Measurment(rand.randint(-1*range,range),rand.randint(-1*range,range),rand.randint(-1*range,range),0)
		
	reading1 = planar_classes.Measurment(rand.randint(-1*range,range),rand.randint(-1*range,range),rand.randint(-1*range,range),0)
	reading1.radius = distance_between_points_with_z(location,reading1)

	reading2 = planar_classes.Measurment(rand.randint(-1*range,range),rand.randint(-1*range,range),rand.randint(-1*range,range),0)
	reading2.radius = distance_between_points_with_z(location,reading2)

	reading3 = planar_classes.Measurment(rand.randint(-1*range,range),rand.randint(-1*range,range),rand.randint(-1*range,range),0)
	reading3.radius = distance_between_points_with_z(location,reading3)

	data = planar_classes.data_packet(reading1,reading2,reading3,location)

	return data


