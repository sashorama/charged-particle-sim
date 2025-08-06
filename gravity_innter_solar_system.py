from gravity import *

SUN_MASS = 100
MERCURY_MASS = 0.0000166
VENUS_MASS = 0.000245
EARTH_MASS = 0.0003
MOON_MASS = 0.0000037
MARS_MASS = 0.0000323
PROBE_MASS = 0.0000000001

MERCURY_DIST = 90
VENUS_DIST = 166
EARTH_DIST = 230
EARTH_MOON_DIST = 0.6
MOON_DIST = EARTH_DIST+EARTH_MOON_DIST
MARS_DIST = 350
    

class Planet:
    def __init__(self, dist, mass, color, radius):
        self.dist = dist
        self.mass = mass
        self.color = color
        self.radius = radius
        self.speed = math.sqrt(SUN_MASS*GRAVITY_FORCE_K/self.dist)



if __name__ == "__main__":       

    #Planets = []
    #Planets.append(Planet(MERCURY_DIST, MERCURY_MASS, (150,120,0),5))
    planet_mars = Planet(MARS_DIST, MARS_MASS, (250,0,0),2)
    planet_earth = Planet(EARTH_DIST, EARTH_MASS, (0,50,250),2)
    #Planets.append(Planet(VENUS_DIST, VENUS_MASS, (150,150,150),5))
    #Planets.append(Planet(MOON_DIST, MOON_MASS, (150,150,150),1))
    #Add velocity for the moon to orbit the earth
    #Planets[4].speed += math.sqrt(GRAVITY_FORCE_K*EARTH_MASS/0.6)

    momentum = 0
    #for planet in Planets:
    #    momentum =+ planet.speed*planet.mass
    
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock() 
    particles = []
    #Sun
    sun = Particle(screen, WIDTH/2, HEIGHT/2, 0, -momentum, mass=SUN_MASS, color = (250,250,0), radius = 10)
    particles.append(sun)
    #Probe
    #particles.append(Particle(screen, WIDTH/2-20, HEIGHT/2, 0, -31.5, mass=MARS_MASS, color = (250,250,250), radius = 2))
    #particles.append(Particle(screen, WIDTH/2+EARTH_DIST+4,HEIGHT/2,0,7.157060159564102,mass=PROBE_MASS, color = (250,250,25), radius = 4))
    #for planet in Planets:
    #    particles.append(Particle(screen, WIDTH/2+planet.dist, HEIGHT/2, 0, planet.speed, mass=planet.mass, color = planet.color, radius = planet.radius))
    mars = Particle(screen, WIDTH/2+planet_mars.dist, HEIGHT/2, 0, planet_mars.speed, mass=planet_mars.mass, color = planet_mars.color, radius = planet_mars.radius)
    earth = Particle(screen, WIDTH/2+planet_earth.dist, HEIGHT/2, 0, planet_earth.speed, mass=planet_earth.mass, color = planet_earth.color, radius = planet_earth.radius)
    particles.append(earth)
    particles.append(mars)
    #calculate the speed for transit to Mars

    mu_sun = GRAVITY_FORCE_K*SUN_MASS
    mu_earth = GRAVITY_FORCE_K*EARTH_MASS
    probe_transit_orbit = EARTH_DIST*(EARTH_MASS/SUN_MASS)**0.4
    probe_transit_orbit *= 1.1
    print(f" Probe transit orbit hight is {probe_transit_orbit}")
    a = (EARTH_DIST+probe_transit_orbit+MARS_DIST)/2
    v_escape = np.sqrt(2*mu_earth/probe_transit_orbit)
    v_transit = np.sqrt(mu_sun*(2/(EARTH_DIST+probe_transit_orbit)-1/a))
    #Add 0.35% of velocity to counter the Earths gravitational influence
    #Alternativly mid flight boots can be used
    v_transit *= 1.0035

    decelerate_probe_used = False
    probe_lounched = False
    probe = None
    running =   True
    while running:
        #probe_distance = None
        clock.tick(FPS)
        #screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        run_simulation(particles)

        angle_earth_mars = angle(earth.pos, mars.pos, sun.pos)
        if abs(angle_earth_mars - 44) < 3: 
            print(f"angle is {angle_earth_mars}")
        
        #If angle between Earth and Mars is 44 degrees shoot the probe
        if abs(angle_earth_mars - 43.8) < 0.5 and probe_lounched == False:
            probe_lounched = True
            print(f"Probe lounched at {angle_earth_mars}")
            earth_vel_norm = earth.vel/np.linalg.norm(earth.vel)
            probe_vel = v_transit * earth_vel_norm 
            earth_pos_sun = earth.pos - sun.pos
            norm_earth_pos_sun = earth_pos_sun/np.linalg.norm(earth_pos_sun)
            probe_pos = earth.pos + norm_earth_pos_sun*probe_transit_orbit
            probe = Particle(screen, probe_pos[0], probe_pos[1], probe_vel[0], probe_vel[1],mass=PROBE_MASS, color = (250,250,25), radius = 1)
            particles.append(probe)
            pass
        
        if probe:
            probe_distance = np.linalg.norm(probe.pos-mars.pos)
            if probe_distance < 3:
                print(probe_distance)
            if False and probe_distance < 0.7:
                speed_difference = mars.vel-probe.vel
                r_speed_vec = speed_difference/np.linalg.norm(speed_difference)
                dist_vec = mars.pos-probe.pos
                r_dist_vec = dist_vec/np.linalg.norm(dist_vec)
                rotated_r_dist_vec = np.array([-r_dist_vec[1], r_dist_vec[0]])
                v_orbital = math.sqrt(GRAVITY_FORCE_K*MARS_MASS/np.linalg.norm(dist_vec))
                deceleration = probe.vel + rotated_r_dist_vec*v_orbital
                probe.vel = deceleration
                decelerate_probe_used = True
                #print(f"speed difference {speed_difference} deceleration {deceleration}")
                #print(f"speed difference after {particles[1].vel-particles[3].vel}")
        for p in particles:
            p.draw()
        pygame.display.flip()
    
    pygame.quit()