import pygame
import random
import math
import numpy as np
import matplotlib.pyplot as plt

# Pygame setup
WIDTH, HEIGHT = 1000, 800
FPS = 30
PARTICLE_RADIUS = 5
N_PARTICLES = 0
GRAVITY_FORCE_K = 0.1
MASS = 1
VEL_DRAG = 0.99
GRAVITY_FORCE_E = 1 # Gravity Softening in close distance
TIME_STEP = 0.01


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
#pygame.init()
#screen = pygame.display.set_mode((WIDTH, HEIGHT))
#clock = pygame.time.Clock()

class Particle:
    def __init__(self,screen, x, y, vx, vy,  mass=MASS, color = (150,150,150), radius=PARTICLE_RADIUS, walls = False):
        self.pos = np.array([x, y], dtype=np.float64)
        self.vel = np.array([vx, vy], dtype=np.float64)
        self.acc = np.zeros(2)
        self.mass = mass
        self.color = color
        self.radius = radius
        self.screen = screen
        self.walls = walls

    def update(self):
        self.vel += self.acc*TIME_STEP
        self.pos += self.vel*TIME_STEP
        self.acc = np.zeros(2)
        if self.walls:
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
        pygame.draw.circle(self.screen, self.color, self.pos.astype(int), self.radius)


def compute_forces(particles):
    for i, p1 in enumerate(particles):
        for j in range(i+1, len(particles)):
            p2 = particles[j]
            r_vec = p2.pos - p1.pos
            dist = np.linalg.norm(r_vec)
            dir_vec = r_vec / dist


            # Mass Attractions
            f_mag = -GRAVITY_FORCE_K*p1.mass*p2.mass / (dist ** 2+GRAVITY_FORCE_E**2)
            force = f_mag * dir_vec
            p1.acc -= force/p1.mass
            p2.acc += force/p2.mass
            

def run_simulation(particles):       
    for _ in range(int(1/TIME_STEP)):  # TIME_STEP substeps per frame   
        compute_forces(particles)
        for p in particles:
            p.update()

def angle(a,b,center):
    '''Returns the signed angle between a and b coordinates and tip at center'''
    #As Top Left corner is the [0,0] shift the positional vectors
    #Take copy of the positions because we don't want to modify them
    a_centered = a.copy()
    b_centered = b.copy()
    a_centered -= center
    b_centered -= center
    #angle_rad = np.arccos(np.dot(a,b)/(a_norm*b_norm))
    cross = a_centered[0]*b_centered[1] - a_centered[1]*b_centered[0]
    dot = np.dot(a_centered, b_centered)    
    return np.degrees(np.arctan2(cross, dot))

def rotate_vector(vec, angle_degrees):
    angle_radians = np.radians(angle_degrees)
    rotation_matrix = np.array([
        [np.cos(angle_radians), -np.sin(angle_radians)],
        [np.sin(angle_radians),  np.cos(angle_radians)]
    ])
    return rotation_matrix @ vec
