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

    MERCURY_DIST = 90
    VENUS_DIST = 166
    EARTH_DIST = 230
    EARTH_MOON_DIST = 0.6
    MOON_DIST = EARTH_DIST+EARTH_MOON_DIST
    MARS_DIST = 350
    

    Planets = []
    Planets.append(Planet(MERCURY_DIST, MERCURY_MASS, (150,120,0),5))
    Planets.append(Planet(MARS_DIST, MARS_MASS, (250,0,0),5))
    Planets.append(Planet(EARTH_DIST, EARTH_MASS, (0,50,250),5))
    Planets.append(Planet(VENUS_DIST, VENUS_MASS, (150,150,150),5))
    Planets.append(Planet(MOON_DIST, MOON_MASS, (150,150,150),1))
    #Add velocity for the moon to orbit the earth
    Planets[4].speed += math.sqrt(GRAVITY_FORCE_K*EARTH_MASS/EARTH_MOON_DIST)

    momentum = 0
    for planet in Planets:
        momentum =+ planet.speed*planet.mass
    
    particles = []
    #Sun
    particles.append(Particle(WIDTH/2, HEIGHT/2, 0, -momentum, mass=SUN_MASS, color = (250,250,0), radius = 10))
    #Mars
    
    for planet in Planets:
        particles.append(Particle(WIDTH/2+planet.dist, HEIGHT/2, 0, planet.speed, mass=planet.mass, color = planet.color, radius = planet.radius))

    running = True
    while running:
        clock.tick(FPS)
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        run_simulation(particles)
        #print(np.linalg.norm(particles[0].pos-[WIDTH/2, HEIGHT/2]))
        pygame.display.flip()
    
    pygame.quit()