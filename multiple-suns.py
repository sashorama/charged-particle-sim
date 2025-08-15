from gravity import *




if __name__ == "__main__":   
    
    SUN_MASS = 100
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock() 
    #Sun 1
    center = np.array([WIDTH/2, HEIGHT/2], dtype=float)
    sun1_pos = center + np.array([0, 100], dtype=float)
    sun1 = Particle(screen, sun1_pos[0], sun1_pos[1], -1.5, 0, mass=SUN_MASS, color = (0,250,0), radius = 10)
    sun2_vel = rotate_vector(sun1.vel, 120)
    sun3_vel = rotate_vector(sun1.vel, 240)
    sun4_vel = rotate_vector(sun1.vel, 60)
    sun5_vel = rotate_vector(sun1.vel, 180)
    sun6_vel = rotate_vector(sun1.vel, 300)
    #Sun 2
    sun1_pos_vec = sun1.pos - center
    sun2_pos_vec = rotate_vector(sun1_pos_vec, 120)
    sun2_pos_vec += center
    sun2 = Particle(screen, sun2_pos_vec[0], sun2_pos_vec[1], sun2_vel[0], sun2_vel[1], mass=SUN_MASS, color = (250,0,0), radius = 10)
    #Sun 3
    sun1_pos_vec = sun1.pos - center
    sun3_pos_vec = rotate_vector(sun1_pos_vec, 240)
    sun3_pos_vec += center
    sun3 = Particle(screen, sun3_pos_vec[0], sun3_pos_vec[1], sun3_vel[0], sun3_vel[1], mass=SUN_MASS, color = (0,0,255), radius = 10)

    #Sun 4
    sun1_pos_vec = sun1.pos - center
    sun4_pos_vec = rotate_vector(sun1_pos_vec, 60)
    sun4_pos_vec += center
    sun4 = Particle(screen, sun4_pos_vec[0], sun4_pos_vec[1], sun4_vel[0], sun4_vel[1], mass=SUN_MASS, color = (0,255,255), radius = 10)

    #Sun 5
    sun1_pos_vec = sun1.pos - center
    sun5_pos_vec = rotate_vector(sun1_pos_vec, 180)
    sun5_pos_vec += center
    sun5 = Particle(screen, sun5_pos_vec[0], sun5_pos_vec[1], sun5_vel[0], sun5_vel[1], mass=SUN_MASS, color = (255,0,255), radius = 10)

    #Sun 6
    sun1_pos_vec = sun1.pos - center
    sun6_pos_vec = rotate_vector(sun1_pos_vec, 300)
    sun6_pos_vec += center
    sun6 = Particle(screen, sun6_pos_vec[0], sun6_pos_vec[1], sun6_vel[0], sun6_vel[1], mass=SUN_MASS, color = (255,255,0), radius = 10)

    particles = []
    particles.append(sun1)
    particles.append(sun2)
    particles.append(sun3)
    particles.append(sun4)
    particles.append(sun5)
    particles.append(sun6)
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