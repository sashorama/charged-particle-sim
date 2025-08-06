from gravity import *
from gravity_innter_solar_system import *


def angle(a,b):
    a_norm = np.linalg.norm(a)
    b_norm = np.linalg.norm(b)
    angle_rad = np.arccos(np.dot(a,b)/(a_norm*b_norm))
    return np.degrees(angle_rad)

#print(a)
#T = 2*math.pi*math.sqrt(a**3/(100*100))/25
#print(T)
mu_sun = GRAVITY_FORCE_K*SUN_MASS
#print(math.sqrt(GRAVITY_FORCE_K*MARS_MASS)/0.7)
#print(math.sqrt(mu_sun/(EARTH_DIST+4))*math.sqrt(2*MARS_DIST/(EARTH_DIST+4+MARS_DIST)-1))
#a = (EARTH_DIST+4+MARS_DIST)/2
#v = np.sqrt(mu_sun*(2/(EARTH_DIST+4)-1/a))
#v0= np.sqrt(mu_sun/(EARTH_DIST+4))
#print(v0)

distance_unit = 149_600_000/EARTH_DIST
print(distance_unit)
geo_stat_orbit = 42164/distance_unit
print(geo_stat_orbit)
probe_transit_orbit = EARTH_DIST*(EARTH_MASS/SUN_MASS)**0.4
print(f"Earth SOI {probe_transit_orbit*distance_unit}km or {probe_transit_orbit} units")


#a = np.array([1,0],dtype=float)
#b = np.array([0,-1],dtype=float)
#angle_rad = angle(b,a)
#print(angle_rad)
