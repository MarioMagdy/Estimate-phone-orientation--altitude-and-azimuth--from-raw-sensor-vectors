import numpy as np
import math

def mag(x):
    return math.sqrt(sum(i ** 2 for i in x))

G2 = [-29,-17.5,17]
H2 = [-0.45,8.85,-4.5]

real_az_2 = 107

G = [-34, -34.0,-12]
H = [0.2,9.4,2.9]

Z= [0,0,1]

real_az_1 = 90
Us = ['x','y','z']


def get_azimuth(G,H,real_az_1):
    for i in  range(3):
        Z= [i==0,i==1,i==2]

        A = np.cross(G,H)
        B = np.cross(G,Z)
        d = np.dot(A,B)

        azimuth = np.divide(d,mag(A)* mag(B))*180/math.pi
        azimuth2 = np.divide(d,mag(A)* mag(B))*100

        print(Us[i],azimuth,azimuth2,real_az_1)

    print()


get_azimuth(G,H,real_az_1)
get_azimuth(G2,H2,real_az_2)
# print(azimuth)