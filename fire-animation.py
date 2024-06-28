import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fire Animation")

# Colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

# Fire parameters
num_particles = 100
particles = []

# Create particles
for _ in range(num_particles):
   x = random.randint(0, WIDTH)
   y = random.randint(HEIGHT - 100, HEIGHT)
   speed_x = random.uniform(-1, 1)
   speed_y = random.uniform(-3, -1)
   size = random.randint(2, 5)
   color = random.choice([RED, ORANGE, YELLOW])
   particles.append([x, y, speed_x, speed_y, size, color])

def draw_fire():
   win.fill(BLACK)
   for particle in particles:
       x, y, speed_x, speed_y, size, color = particle
       pygame.draw.circle(win, color, (int(x), int(y)), size)

def update_fire():
   for particle in particles:
       particle[0] += particle[2]
       particle[1] += particle[3]
       particle[4] -= 0.1  # Reduce size over time

       # Change color to simulate cooling
       if particle[5] == YELLOW:
           particle[5] = ORANGE
       elif particle[5] == ORANGE:
           particle[5] = RED

       # Respawn particle at the bottom if it disappears
       if particle[1] < 0 or particle[4] <= 0:
           particle[0] = random.randint(0, WIDTH)
           particle[1] = random.randint(HEIGHT - 100, HEIGHT)
           particle[2] = random.uniform(-1, 1)
           particle[3] = random.uniform(-3, -1)
           particle[4] = random.randint(2, 5)
           particle[5] = random.choice([RED, ORANGE, YELLOW])

def main():
   clock = pygame.time.Clock()
   run = True

   while run:
       clock.tick(60)

       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               run = False

       draw_fire()
       update_fire()
       pygame.display.update()

   pygame.quit()

if __name__ == "__main__":
   main()
