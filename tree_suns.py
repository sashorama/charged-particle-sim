from gravity import *




if __name__ == "__main__":   
    
    SUN_MASS = 100
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock() 
    center = np.array([WIDTH/2, HEIGHT/2], dtype=float)
    
    #Lagrangian orbits
    #Sun 1
    #sun1_pos = center + np.array([0, 100], dtype=float)
    #sun1 = Particle(screen, sun1_pos[0], sun1_pos[1], -0.8, 0, mass=SUN_MASS, color = (0,250,0), radius = 10)
    #sun2_vel = rotate_vector(sun1.vel, 120)
    #sun3_vel = rotate_vector(sun1.vel, 240)
    #Sun 2
    #sun1_pos_vec = sun1.pos - center
    #sun2_pos_vec = rotate_vector(sun1_pos_vec, 120)
    #sun2_pos_vec += center
    #sun2 = Particle(screen, sun2_pos_vec[0], sun2_pos_vec[1], sun2_vel[0], sun2_vel[1], mass=SUN_MASS, color = (250,0,0), radius = 10)
    #Sun 3
    #sun1_pos_vec = sun1.pos - center
    #sun3_pos_vec = rotate_vector(sun1_pos_vec, 240)
    #sun3_pos_vec += center
    #sun3 = Particle(screen, sun3_pos_vec[0], sun3_pos_vec[1], sun3_vel[0], sun3_vel[1], mass=SUN_MASS, color = (0,0,255), radius = 10)

    #Fiugre 8 initial conditions
    #Initial positions
    r1 = np.array([-97.000436, 24.308753], dtype=np.float64)
    r2 = -r1.copy() #symetrical via r3
    r3= np.zeros(2, dtype=np.float64)
    #Figure 8 initial velocity
    v1 = np.array([0.4662036850,  0.4323657300], dtype=np.float64)
    v2 = v1.copy()
    v3 = -2*v1.copy()

    #Scale the figure 8 to be bigger
    FIGURE_8_SCALE = 2
    r1 *= FIGURE_8_SCALE
    r2 *= FIGURE_8_SCALE
    r3 *= FIGURE_8_SCALE

    #To keep the figure Speed have to be scaled too
    v1 /= np.sqrt(FIGURE_8_SCALE/GRAVITY_FORCE_K)
    v2 /= np.sqrt(FIGURE_8_SCALE/GRAVITY_FORCE_K)
    v3 /= np.sqrt(FIGURE_8_SCALE/GRAVITY_FORCE_K)

    #Shift the fugre to the center of the drawing
    r1 += center
    r2 += center
    r3 += center



    #Sun 1


    sun1 = Particle(screen, r1[0], r1[1],v1[0], v1[1], mass=SUN_MASS, color = (0,250,0), radius = 5)

    #Sun 2

    sun2 = Particle(screen, r2[0], r2[1],v2[0], v2[1], mass=SUN_MASS, color = (250,0,0), radius = 5)
    #Sun 3

    sun3 = Particle(screen, r3[0], r3[1],v3[0], v3[1], mass=SUN_MASS, color = (0,0,250), radius = 5)

    particles = []
    particles.append(sun1)
    particles.append(sun2)
    particles.append(sun3)

    font = pygame.font.Font(None, 24)  # None = default font, 48 = font size
    text_commet_distance = ''
    running = True
    while running:

        clock.tick(FPS)
        screen.fill((0, 0, 0))
        comment_distance = np.linalg.norm(sun1.pos - sun2.pos)
        text_commet_distance = f"Sun1 to Sun2 = {round(comment_distance)}"
        text_surface_commet_distance = font.render(text_commet_distance, True, (255, 255, 255))
        screen.blit(text_surface_commet_distance, (10, 10))
        sun2_sun3 = np.linalg.norm(sun2.pos - sun3.pos)
        sun2_sun3_distance = f"Sun2 to Sun3 = {round(sun2_sun3)}"
        text_surface_commet_distance = font.render(sun2_sun3_distance, True, (255, 255, 255))
        screen.blit(text_surface_commet_distance, (10, 30))
                    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        run_simulation(particles)    
        for p in particles:
            p.draw()
        pygame.display.flip()
    pygame.quit()