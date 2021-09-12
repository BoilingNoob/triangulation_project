from planar_triangulation_lib import classes as planar_classes
from planar_triangulation_lib import functions as planar_funcs


import numpy
from numpy import sqrt, dot, cross
from numpy.linalg import norm

# solution from: https://stackoverflow.com/questions/1406375/finding-intersection-points-between-3-spheres

def trilaterate_mine(measurement1, measurement2, measurement3):
    numpy_point_1 = numpy.array([measurement1.x, measurement1.y, measurement1.z])
    numpy_point_2 = numpy.array([measurement2.x, measurement2.y, measurement2.z])
    numpy_point_3 = numpy.array([measurement3.x, measurement3.y, measurement3.z])

    temp1 = numpy_point_2 - numpy_point_1
    e_x = temp1/norm(temp1)
    temp2 = numpy_point_3 - numpy_point_1
    i_vec = dot(e_x, temp2)
    temp3 = temp2 - (i_vec * e_x)
    e_y = temp3/norm(temp3)
    e_z = cross(e_x, e_y)
    d = norm(numpy_point_2 - numpy_point_1)
    j_vec = dot(e_y, temp2)
    x = (measurement1.radius**2 - measurement2.radius**2 + d**2) / (2*d)
    y = (measurement1.radius**2 - measurement3.radius ** 2 - 2*i_vec*x + i_vec**2 + j_vec**2)/(2*j_vec)
    temp4 = measurement1.radius**2 - x**2 - y**2
    if temp4 < 0:
        raise Exception("The spheres do not intesect")
    z = sqrt(temp4)
    p_12_a = numpy_point_1 + x*e_x + y*e_y + z*e_z
    p_12_b = numpy_point_1 + x*e_x + y*e_y - z*e_z

    if p_12_a.all() != p_12_b.all():
        return p_12_a, p_12_b
    else:
        return p_12_a

# P1,P2,P3 are the centers, r1,r2,r3 are the radii
# Implementaton based on Wikipedia Trilateration article.


def trilaterate(P1, P2, P3, r1, r2, r3):
    temp1 = P2-P1
    e_x = temp1/norm(temp1)
    temp2 = P3-P1
    i = dot(e_x, temp2)
    temp3 = temp2 - i*e_x
    e_y = temp3/norm(temp3)
    e_z = cross(e_x, e_y)
    d = norm(P2-P1)
    j = dot(e_y, temp2)
    x = (r1*r1 - r2*r2 + d*d) / (2*d)
    y = (r1*r1 - r3*r3 - 2*i*x + i*i + j*j) / (2*j)
    temp4 = r1*r1 - x*x - y*y
    if temp4 < 0:
        raise Exception("The three spheres do not intersect!")
    z = sqrt(temp4)
    p_12_a = P1 + x*e_x + y*e_y + z*e_z
    p_12_b = P1 + x*e_x + y*e_y - z*e_z

    if p_12_a.all() != p_12_b.all():
        return p_12_a, p_12_b
    else:
        return p_12_a


# the point is 0,0,0
measurement1 = planar_classes.Measurment(50, 0, 0, 50)
measurement2 = planar_classes.Measurment(0, 50, 0, 50)
measurement3 = planar_classes.Measurment(-50, 0, 0, 50)

data = planar_funcs.generate_data(None,1000)
answer = trilaterate_mine(data.measurement1, data.measurement2, data.measurement3)

print("Measure 1: ",data.measurement1)
print("Measure 2: ",data.measurement2)
print("Measure 3: ",data.measurement3)
print("the calculated answer: ", answer)
print("   The original point: ", data.location)
