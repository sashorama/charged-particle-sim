import pygame
import random
import math
import numpy as np
import matplotlib.pyplot as plt

# Pygame setup
WIDTH, HEIGHT = 800, 600
FPS = 1
PARTICLE_RADIUS = 5
N_PARTICLES = 0
CHARGE_FORCE_K = 1000  # Coulomb constant (scaled)
NUCLEAR_FORCE_A = 0   # Strength of short-range attraction 500
NUCLEAR_SIGMA = 20       # Range of short-range attraction
NUCLEAR_TOO_CLOSE = 5    # Disapears of too close
NUCLEAR_TOO_FAR = 20
MASS = 1
VEL_DRAG = 0.95
CHARGE_FORCE_E = 90 # Coulomb force softnef especially in close distance
MINIMUM_DISTANCE = 2

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

class Particle:
    def __init__(self, x, y, vx, vy, charge,  mass=MASS):
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
        if self.charge == 1:
            color = (255,0,0)
        elif self.charge == 0:
            color = (150,150,150)
        else:
            color = (0,0,255)
        pygame.draw.circle(screen, color, self.pos.astype(int), PARTICLE_RADIUS)


def compute_forces(particles):
    for i, p1 in enumerate(particles):
        for j in range(i + 1, len(particles)):
            p2 = particles[j]
            r_vec = p2.pos - p1.pos
            dist = np.linalg.norm(r_vec)
            if dist < MINIMUM_DISTANCE:
                p1.pos += random.uniform(-MINIMUM_DISTANCE, MINIMUM_DISTANCE)
                r_vec = p2.pos - p1.pos
                dist = np.linalg.norm(r_vec)
                #continue  # Avoid division by zero
            dir_vec = r_vec / dist

            # Nuclear repultion and spead drag at very close distance
            if dist < 5:
                p1.vel *= VEL_DRAG
                p2.vel *= VEL_DRAG

            # Charge repulsion
            f_mag = CHARGE_FORCE_K*p1.charge*p2.charge / (dist ** 2+CHARGE_FORCE_E**2)
            force = f_mag * dir_vec
            p1.acc -= force/p1.mass
            p2.acc += force/p2.mass
            
            # Nuclear attraction at close distance
            if dist >= NUCLEAR_TOO_CLOSE and dist < NUCLEAR_TOO_FAR:
                f_mag = -NUCLEAR_FORCE_A * math.exp(-dist ** 2 / NUCLEAR_SIGMA ** 2)
                force = f_mag * dir_vec
                p1.acc -= force/p1.mass
                p2.acc += force/p2.mass
                #p1.acc = 0
                #p2.acc = 0
                

#mathplotlib
def nuclear_force(r):
    f_strong = -NUCLEAR_FORCE_A * np.exp(-r ** 2 / NUCLEAR_SIGMA ** 2)
    f_strong[r > NUCLEAR_TOO_FAR] = 0  # truncate force
    f_strong[r < NUCLEAR_TOO_CLOSE] = 0  # truncate force
    return f_strong

r = np.linspace(1, 100, 1000)
f_elect = CHARGE_FORCE_K / ((r ** 2)+CHARGE_FORCE_E**2)
f_strong = nuclear_force(r)
plt.figure(figsize=(10, 6))
plt.plot(r, f_elect, 'r--', label='Electrostatic (Proton-Proton)')
plt.plot(r, f_strong, 'b-', label='Nuclear (Proton-Proton)')
plt.axhline(0, color='gray', linewidth=0.5)
plt.xlabel('Distance (pixels)')
plt.ylabel('Force magnitude')
plt.title('Force vs. Distance')
plt.legend()
plt.grid(True)
plt.tight_layout()
#plt.yscale('log')
plt.show()
# Create particles
particles = []
for _ in range(N_PARTICLES):
    x = random.uniform(PARTICLE_RADIUS, WIDTH - PARTICLE_RADIUS)
    y = random.uniform(PARTICLE_RADIUS, HEIGHT - PARTICLE_RADIUS)
    vx = random.uniform(-1, 1)
    vy = random.uniform(-1, 1)
    charge = 1 if random.random() < 0.9 else 0
    if random.random() < 0.5:
        charge *= -1 
    particles.append(Particle(x, y, vx, vy, charge))

particles.append(Particle(500, 200, 0, 3, 1))
particles.append(Particle(550, 200, 0, -3, -1, mass = 0.1))
particles.append(Particle(100,110, 0, 0, 1))
#particles.append(Particle(105,105, 0, 0, 0))
# Main loop
running = True

while running:
    clock.tick(FPS)
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    for _ in range(10):  # 4 substeps per frame   
        compute_forces(particles)
        for p in particles:
            p.update()
    for p in particles:
        p.draw()

    pygame.display.flip()

pygame.quit()
