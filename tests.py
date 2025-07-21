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
    
        for _ in range(int(1/TIME_STEP)):  # 4 substeps per frame   
            compute_forces(particles)
            for p in particles:
                p.update()
        for p in particles:
            p.draw()

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
    
        for _ in range(int(1/TIME_STEP)):  # 4 substeps per frame   
            compute_forces(particles)
            for p in particles:
                p.update()
        for p in particles:
            p.draw()

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
    
        for _ in range(int(1/TIME_STEP)):  # 4 substeps per frame   
            compute_forces(particles)
            for p in particles:
                p.update()
        for p in particles:
            p.draw()

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
    
        for _ in range(int(1/TIME_STEP)):  # 4 substeps per frame   
            compute_forces(particles)
            for p in particles:
                p.update()
        for p in particles:
            p.draw()

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
    
        for _ in range(int(1/TIME_STEP)):  # 4 substeps per frame   
            compute_forces(particles)
            for p in particles:
                p.update()
        for p in particles:
            p.draw()

        pygame.display.flip()
##########Begin Tests#####################

#two_protons_two_electrons()
two_protons_low_speed()
two_protons_high_speed()
proton_neutron_low_speed()
proton_neutron_high_speed()
two_protons_two_electrons()
pygame.quit()