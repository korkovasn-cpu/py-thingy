import pygame
import math
import colorsys

# ---------- CONFIG ----------
WIDTH, HEIGHT = 900, 900
POINTS = 2000
SPEED = 0.002
# ----------------------------

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Math Trance")
clock = pygame.time.Clock()

t = 0.0
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((5, 5, 10))

    cx, cy = WIDTH // 2, HEIGHT // 2
    scale = min(WIDTH, HEIGHT) * 0.35

    for i in range(POINTS):
        a = i / POINTS * math.pi * 2

        # Core math pattern
        r = math.sin(a * 3 + t) * math.cos(a * 2 - t * 0.7)
        x = math.cos(a + t) * (1 + r) * scale
        y = math.sin(a * 2 - t) * (1 - r) * scale

        # Color based on angle + time
        hue = (a / (math.pi * 2) + t * 0.05) % 1.0
        rgb = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
        color = tuple(int(c * 255) for c in rgb)

        screen.set_at((int(cx + x), int(cy + y)), color)

    pygame.display.flip()
    t += SPEED
    clock.tick(60)

pygame.quit()
