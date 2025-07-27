from particle import *


def two_protons_two_electrons():
    # Create particles
    particles = []
    particles.append(Particle(500, 200, 0, 3, 1))
    particles.append(Particle(550, 200, 0, -3, -1, mass = 0.1))
    particles.append(Particle(100, 110, 0, 0, 1))
    particles.append(Particle(550, 205, 0, -3, -1, mass = 0.1))
    # Main loop
    running = True

    while running:
        clock.tick(FPS)
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        run_simulation(particles)

        pygame.display.flip()

    #pygame.quit()

def two_protons_low_speed():
    # Create particles
    particles = []
    particles.append(Particle(300, 200, 5, 0, 1))
    particles.append(Particle(500,200, -5, 0, 1))
    # Main loop
    running = True

    while running:
        clock.tick(FPS)
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        run_simulation(particles)

        pygame.display.flip()

def two_protons_high_speed():
    # Create particles
    particles = []
    particles.append(Particle(300, 200, 30, 0, 1))
    particles.append(Particle(500,200, -30, 0, 1))
    # Main loop
    running = True

    while running:
        clock.tick(FPS)
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        run_simulation(particles)

        pygame.display.flip()

def proton_neutron_low_speed():
    # Create particles
    particles = []
    particles.append(Particle(300, 200, 5, 0, 1))
    particles.append(Particle(500,200, -5, 0, 0))
    # Main loop
    running = True

    while running:
        clock.tick(FPS)
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        run_simulation(particles)

        pygame.display.flip()

def proton_neutron_high_speed():
    # Create particles
    particles = []
    particles.append(Particle(300, 200, 30, 0, 1))
    particles.append(Particle(500,200, -30, 0, 0))
    # Main loop
    running = True

    while running:
        clock.tick(FPS)
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        run_simulation(particles)

        pygame.display.flip()

def four_protons():
    # Create particles
    particles = []
    particles.append(Particle(300, 200, 0, 0, 1))
    particles.append(Particle(500, 200, 0, 0, 1))
    particles.append(Particle(300, 400, 0, 0, 1))
    particles.append(Particle(500, 400, 0, 0, 1))
    # Main loop
    running = True

    while running:
        clock.tick(FPS)
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        run_simulation(particles)

        pygame.display.flip()

def proton_electron():
    # Create particles
    particles = []
    particles.append(Particle(300, 200, 0, 0, 1))
    particles.append(Particle(400, 200, 0, 30, -1, mass=0.01))
    # Main loop
    running = True

    while running:
        clock.tick(FPS)
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        run_simulation(particles)

        pygame.display.flip()
##########Begin Tests#####################

two_protons_two_electrons()
four_protons()
two_protons_low_speed()
two_protons_high_speed()
proton_neutron_low_speed()
proton_neutron_high_speed()
proton_electron()
two_protons_two_electrons()
pygame.quit()