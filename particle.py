import pygame
import random
import math
import numpy as np

# Pygame setup
WIDTH, HEIGHT = 800, 600
FPS = 25
PARTICLE_RADIUS = 5
N_PARTICLES = 20
CHARGE_FORCE_K = 1000  # Coulomb constant (scaled)
NUCLEAR_FORCE_A = 500   # Strength of short-range attraction
NUCLEAR_SIGMA = 25       # Range of short-range attraction

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

class Particle:
    def __init__(self, x, y, vx, vy, charge,  mass=5.0):
        self.pos = np.array([x, y], dtype=float)
        self.vel = np.array([vx, vy], dtype=float)
        self.acc = np.zeros(2)
        self.charge = charge  # +1 for proton, 0 for neutron
        self.mass = mass

    def update(self):
        self.vel += self.acc
        self.pos += self.vel
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
        color = (255, 0, 0) if self.charge == 1 else (150, 150, 150)
        pygame.draw.circle(screen, color, self.pos.astype(int), PARTICLE_RADIUS)


def compute_forces(particles):
    for i, p1 in enumerate(particles):
        for j in range(i + 1, len(particles)):
            p2 = particles[j]
            r_vec = p2.pos - p1.pos
            dist = np.linalg.norm(r_vec)
            if dist < 1e-1:
                continue  # Avoid division by zero
            dir_vec = r_vec / dist

            # Charge repulsion (only protons)
            if p1.charge == 1 and p2.charge == 1:
                f_mag = CHARGE_FORCE_K / (dist ** 2)
                force = f_mag * dir_vec
                p1.acc -= force/p1.mass
                p2.acc += force/p2.mass

            # Nuclear attraction (short range, for all)
            #if dist < NUCLEAR_SIGMA * 2:
            #    f_mag = -NUCLEAR_FORCE_A * math.exp(-dist ** 2 / NUCLEAR_SIGMA ** 2)
            #    force = f_mag * dir_vec
            #    p1.acc += force/p1.mass
            #    p2.acc -= force/p1.mass


# Create particles
particles = []
for _ in range(N_PARTICLES):
    x = random.uniform(PARTICLE_RADIUS, WIDTH - PARTICLE_RADIUS)
    y = random.uniform(PARTICLE_RADIUS, HEIGHT - PARTICLE_RADIUS)
    vx = random.uniform(-1, 1)
    vy = random.uniform(-1, 1)
    charge = 1 if random.random() < 0.5 else 0
    particles.append(Particle(x, y, vx, vy, charge))

# Main loop
running = True
while running:
    clock.tick(FPS)
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    compute_forces(particles)
    for p in particles:
        p.update()
        p.draw()

    pygame.display.flip()

pygame.quit()
