import pygame
import random
import math
import numpy as np
import matplotlib.pyplot as plt

# Pygame setup
WIDTH, HEIGHT = 1000, 800
FPS = 25
PARTICLE_RADIUS = 5
N_PARTICLES = 0
GRAVITY_FORCE_K = 100
MASS = 1
VEL_DRAG = 0.99
GRAVITY_FORCE_E = 4 # Gravity Softening in close distance
TIME_STEP = 0.01

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

class Particle:
    def __init__(self, x, y, vx, vy,  mass=MASS, color = (150,150,150), radius=PARTICLE_RADIUS):
        self.pos = np.array([x, y], dtype=float)
        self.vel = np.array([vx, vy], dtype=float)
        self.acc = np.zeros(2)
        self.mass = mass
        self.color = color
        self.radius = radius

    def update(self):
        self.vel += self.acc*TIME_STEP
        self.pos += self.vel*TIME_STEP
        self.acc = np.zeros(2)
        self.wall_collision()

    def wall_collision(self):
        for i in [0, 1]:
            if self.pos[i] - PARTICLE_RADIUS < 0:
                self.pos[i] = PARTICLE_RADIUS
                self.vel[i] *= -1
            elif self.pos[i] + PARTICLE_RADIUS > (WIDTH if i == 0 else HEIGHT):
                self.pos[i] = (WIDTH if i == 0 else HEIGHT) - PARTICLE_RADIUS
                self.vel[i] *= -1

    def draw(self):
        pygame.draw.circle(screen, self.color, self.pos.astype(int), self.radius)


def compute_forces(particles):
    for i, p1 in enumerate(particles):
        for j in range(i+1, len(particles)):
            p2 = particles[j]
            r_vec = p2.pos - p1.pos
            dist = np.linalg.norm(r_vec)
            dir_vec = r_vec / dist

            # Spead drag at very close distance
            #if dist < 5 and np.linalg.norm(p1.vel - p2.vel) > 50:
            #    p1.vel *= VEL_DRAG
            #    p2.vel *= VEL_DRAG

            # Mass Attractions
            f_mag = -GRAVITY_FORCE_K*p1.mass*p2.mass / (dist ** 2+GRAVITY_FORCE_E**2)
            force = f_mag * dir_vec
            p1.acc -= force/p1.mass
            p2.acc += force/p2.mass
            

def run_simulation(particles):       
    for _ in range(int(1/TIME_STEP)):  # 4 substeps per frame   
        compute_forces(particles)
        for p in particles:
            p.update()
    for p in particles:
        p.draw()
#mathplotlib

if __name__ == '__main__':
    # Create particles
    particles = []
    for _ in range(N_PARTICLES):
        x = random.uniform(PARTICLE_RADIUS, WIDTH - PARTICLE_RADIUS)
        y = random.uniform(PARTICLE_RADIUS, HEIGHT - PARTICLE_RADIUS)
        vx = random.uniform(-5, 5)
        vy = random.uniform(-5, 5)
        particles.append(Particle(x, y, vx, vy))

    particles = []
    particles.append(Particle(WIDTH/2, HEIGHT/2, 0, -0.1496, mass=100, color = (250,250,0), radius = 10))
    particles.append(Particle(WIDTH/2+350, HEIGHT/2, 0, 5, color = (0,0,250), radius = 5))
    particles.append(Particle(WIDTH/2+365, HEIGHT/2, 0, 7.8, mass = 0.2, radius = 3))
    particles.append(Particle(WIDTH/2+70, HEIGHT/2, 0, 10, mass = 0.2, color = (150,120,0), radius = 5))
    particles.append(Particle(WIDTH/2+150, HEIGHT/2, 0, 8, mass = 0.8, color = (150,150,150), radius = 5))
    
    #particles.append(Particle(WIDTH/2, HEIGHT/2, 0, -0.065, mass=100, color = (250,250,0), radius = 10))
    #particles.append(Particle(WIDTH/2+350, HEIGHT/2, 0, 5, color = (0,0,250), radius = 5))
    #particles.append(Particle(WIDTH/2+360, HEIGHT/2, 0, 7.5, mass = 0.2, radius = 3))
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
    
    pygame.quit()
