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
G = 6.67E-11
M = 2e+30
EARTH_DIST_SI = 149_600_000_000
distance_unit = EARTH_DIST_SI/EARTH_DIST
G_unit = G/GRAVITY_FORCE_K
mass_unit = M/SUN_MASS
T_unit = np.sqrt(distance_unit**3/(G_unit*mass_unit))*FPS
Earth_period = (2*math.pi*np.sqrt(EARTH_DIST**3/(GRAVITY_FORCE_K*SUN_MASS)))/FPS
speed_unit = (G*M)*EARTH_DIST/(mu_sun*EARTH_DIST_SI)
speed_unit = np.sqrt(speed_unit)
print(f"Earth_period={Earth_period}")
print(f"Earth_period={Earth_period*T_unit/(24*3600)} days")
earth_soi = EARTH_DIST*(EARTH_MASS/SUN_MASS)**0.4
a = (EARTH_DIST+earth_soi+MARS_DIST)/2

#print(f"Earth SOI {earth_soi*distance_unit}km or {earth_soi} units")

v_transit = np.sqrt(mu_sun*(2/(EARTH_DIST+earth_soi)-1/a))
v_orbit = np.sqrt(mu_sun/EARTH_DIST)
v_delta = np.sqrt(mu_sun/MARS_DIST) - np.sqrt(2*mu_sun*(1/MARS_DIST-1/(2*a)))
print(f"v_delta={v_delta} in SI v_delta={v_delta*speed_unit} m/s")
print(f"v_orbit={v_orbit} in SI v_orbit={v_orbit*speed_unit} m/s")

#a = np.array([1,0],dtype=float)
#b = np.array([0,-1],dtype=float)
#angle_rad = angle(b,a)
#print(angle_rad)
