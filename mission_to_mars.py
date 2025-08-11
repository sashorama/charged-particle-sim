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
    planet_mars = Planet(MARS_DIST, MARS_MASS, (250,0,0),2)
    planet_earth = Planet(EARTH_DIST, EARTH_MASS, (0,50,250),2)   
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock() 
    particles = []
    #Sun
    sun = Particle(screen, WIDTH/2, HEIGHT/2, 0, 0, mass=SUN_MASS, color = (250,250,0), radius = 10)
    mars = Particle(screen, WIDTH/2+planet_mars.dist, HEIGHT/2, 0, planet_mars.speed, mass=planet_mars.mass, 
                    color = planet_mars.color, radius = planet_mars.radius)
    earth = Particle(screen, WIDTH/2-planet_earth.dist, HEIGHT/2, 0, -planet_earth.speed, mass=planet_earth.mass, 
                    color = planet_earth.color, radius = planet_earth.radius)
    particles.append(sun)
    particles.append(earth)
    particles.append(mars)
    #calculate the speed for transit to Mars

    mu_sun = GRAVITY_FORCE_K*SUN_MASS
    mu_earth = GRAVITY_FORCE_K*EARTH_MASS
    mu_mars = GRAVITY_FORCE_K*MARS_MASS
    #Calculate Sphere of Influence where planet gravity dominates
    earth_soi = EARTH_DIST*(EARTH_MASS/SUN_MASS)**0.4
    earth_soi *= 1.1 # Extend it by 10% so we get less Earths influece when we start the orbit the Sun
    mars_soi = MARS_DIST*(MARS_MASS/SUN_MASS)**0.4
    print(mars_soi)
    a = (EARTH_DIST+earth_soi+MARS_DIST)/2
    v_transit = np.sqrt(mu_sun*(2/(EARTH_DIST+earth_soi)-1/a))
    v_delta = np.sqrt(mu_sun/MARS_DIST) - np.sqrt(2*mu_sun*(1/MARS_DIST-1/(2*a)))
    #Add 0.35% of velocity to counter the Earths gravitational influence
    #Alternativly mid flight boots can be used
    v_transit *= 1.0035

    text_angle = ""
    text_dV  = "dV to catch Mars not used yet"
    text_probe_distance = "Probe not lounched yet"
    text_dV_theory = f"еxpected dV = {round(v_delta,3)}"
    text_probe_distance_min = "dist_min="

    probe_distance_min = None
    decelerate_probe_used = False
    probe_lounched = False
    probe = None
    running =   True
    while running:
        #probe_distance = None
        clock.tick(FPS)
        screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 24)  # None = default font, 48 = font size
        
        #angle_earth_mars = angle(earth.pos, mars.pos, sun.pos)
        text_surface_angle = font.render(text_angle, True, (255, 255, 255))
        screen.blit(text_surface_angle, (10, 10))

        text_surface_distance = font.render(text_probe_distance, True, (255, 255, 255))
        screen.blit(text_surface_distance, (10, 30))

        text_surface_dV_theory = font.render(text_dV_theory, True, (255, 255, 255))
        screen.blit(text_surface_dV_theory, (10, 50)) 

        text_surface_dV = font.render(text_dV, True, (255, 255, 255))
        screen.blit(text_surface_dV, (10, 70))

        text_surface_distance_min = font.render(text_probe_distance_min, True, (255, 255, 255))
        screen.blit(text_surface_distance_min, (10, 90))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        run_simulation(particles)

    #If the probe is not lounched check the angle between Earth Sun and Mars     
        if not probe:
            angle_earth_mars = angle(earth.pos, mars.pos, sun.pos)
            text_angle = f"theta = {round(angle_earth_mars,3)} deg"
        #If angle between Earth and Mars is 44 degrees shoot the probe
            if abs(angle_earth_mars - 44.2) < 0.2 and probe_lounched == False:
                probe_lounched = True
                earth_vel_norm = earth.vel/np.linalg.norm(earth.vel)
                probe_vel = v_transit * earth_vel_norm 
                earth_pos_sun = earth.pos - sun.pos
                norm_earth_pos_sun = earth_pos_sun/np.linalg.norm(earth_pos_sun)
                probe_pos = earth.pos + norm_earth_pos_sun*earth_soi
                probe = Particle(screen, probe_pos[0], probe_pos[1], probe_vel[0], probe_vel[1],mass=PROBE_MASS, color = (250,250,25), radius = 1)
                particles.append(probe)

        #If the probe is already lounched
        else:
            text_angle = f"lounched at Theta = {round(angle_earth_mars,3)}"
            probe_distance = np.linalg.norm(probe.pos-mars.pos)
            if not probe_distance_min:
                probe_distance_min = probe_distance
            if probe_distance < probe_distance_min:
                probe_distance_min = probe_distance
            text_probe_distance_min = f"dist_min = {probe_distance_min}"
            text_probe_distance = f"dists = {round(probe_distance,3)}"
            if probe_distance < mars_soi and decelerate_probe_used == False:
                decelerate_probe_used = True
                deceleration = mars.vel - probe.vel
                text_dV = f"dV = {round(np.linalg.norm(deceleration),3)}"
                print(f"Mars vel {mars.vel} deceleration")
                print(f"Probe vel  {probe.vel}")
                probe.vel += deceleration
                decelerate_probe_used = True
                print(f"Mars vel {probe.vel} deceleration")
                print(f"Probe vel  {mars.vel}")
        for p in particles:
            p.draw()
        pygame.display.flip()
    
    pygame.quit()