from gravity import *

class Planet:
    def __init__(self, dist, mass, color, radius):
        self.dist = dist
        self.mass = mass
        self.color = color
        self.radius = radius
        self.speed = math.sqrt(SUN_MASS*GRAVITY_FORCE_K/self.dist)


if __name__ == "__main__":   
    
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
    COMMET_DIST = 20
    
    #Calculations
    #Commet excape Sun gravity system velocyty
    v_commet_escape = np.sqrt(2*SUN_MASS*GRAVITY_FORCE_K/COMMET_DIST)
    v_commet_speed = v_commet_escape*0.95
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock() 

    Planets = []
    Planets.append(Planet(MERCURY_DIST, MERCURY_MASS, (150,120,0),5))
    Planets.append(Planet(MARS_DIST, MARS_MASS, (250,0,0),5))
    Planets.append(Planet(EARTH_DIST, EARTH_MASS, (0,50,250),5))
    Planets.append(Planet(VENUS_DIST, VENUS_MASS, (150,150,150),5))
    Planets.append(Planet(MOON_DIST, MOON_MASS, (150,150,150),1))
    #Add velocity for the moon to orbit the earth
    Planets[4].speed += math.sqrt(GRAVITY_FORCE_K*EARTH_MASS/0.6)

    momentum = 0
    for planet in Planets:
        momentum =+ planet.speed*planet.mass
    
    particles = []
    #Sun
    particles.append(Particle(screen, WIDTH/2, HEIGHT/2, 0, -momentum, mass=SUN_MASS, color = (250,250,0), radius = 10))
    #Commet
    particles.append(Particle(screen, WIDTH/2-COMMET_DIST, HEIGHT/2, 0, -v_commet_speed, mass=MARS_MASS, color = (250,250,250), radius = 2))
    #Append Planets
    for planet in Planets:
        particles.append(Particle(screen, WIDTH/2+planet.dist, HEIGHT/2, 0, planet.speed, mass=planet.mass, color = planet.color, radius = planet.radius))

    font = pygame.font.Font(None, 24)  # None = default font, 48 = font size
    text_commet_distance = ''
    running = True
    while running:

        clock.tick(FPS)
        screen.fill((0, 0, 0))
        comment_distance = np.linalg.norm(particles[0].pos - particles[1].pos)
        text_commet_distance = f"Commen to Sun distance = {round(comment_distance)}"
        text_surface_commet_distance = font.render(text_commet_distance, True, (255, 255, 255))
        screen.blit(text_surface_commet_distance, (10, 10))
                    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        run_simulation(particles)    
        for p in particles:
            p.draw()
        pygame.display.flip()
    pygame.quit()