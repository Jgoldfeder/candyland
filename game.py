import pygame

# --- constants --- (UPPER_CASE names)

SCREEN_WIDTH = int(640*1.5)
SCREEN_HEIGHT = int(480*1.5)

#BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN   = (0,   255,   0)
BLUE = (0,   0,   255)
YELLOW = (255,255,0)
FPS = 30

# --- classses --- (CamelCase names)

# empty

# --- functions --- (lower_case names)

# empty

# --- main ---

# - init -

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
bg = pygame.image.load("board2.png")

pygame.display.set_caption("Tracking System")

# - objects -

red_rect = pygame.rect.Rect(40, 40, 17, 17)
blue_rect = pygame.rect.Rect(40, 80, 17, 17)
green_rect = pygame.rect.Rect(40, 120, 17, 17)
yellow_rect = pygame.rect.Rect(40, 160, 17, 17)

red_rect_draging = False
blue_rect_draging = False
green_rect_draging = False
yellow_rect_draging = False

# - mainloop -

clock = pygame.time.Clock()

running = True

while running:

    # - events -

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:            
                if red_rect.collidepoint(event.pos):
                    red_rect_draging = True
                    mouse_x, mouse_y = event.pos
                    offset_x = red_rect.x - mouse_x
                    offset_y = red_rect.y - mouse_y
                if blue_rect.collidepoint(event.pos):
                    blue_rect_draging = True
                    mouse_x, mouse_y = event.pos
                    offset_x = blue_rect.x - mouse_x
                    offset_y = blue_rect.y - mouse_y
                if green_rect.collidepoint(event.pos):
                    green_rect_draging = True
                    mouse_x, mouse_y = event.pos
                    offset_x = green_rect.x - mouse_x
                    offset_y = green_rect.y - mouse_y 
                if yellow_rect.collidepoint(event.pos):
                    yellow_rect_draging = True
                    mouse_x, mouse_y = event.pos
                    offset_x = yellow_rect.x - mouse_x
                    offset_y = yellow_rect.y - mouse_y     
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:            
                red_rect_draging = False
                blue_rect_draging = False
                green_rect_draging = False
                yellow_rect_draging = False

        elif event.type == pygame.MOUSEMOTION:
            if red_rect_draging:
                mouse_x, mouse_y = event.pos
                red_rect.x = mouse_x + offset_x
                red_rect.y = mouse_y + offset_y
            if blue_rect_draging:
                mouse_x, mouse_y = event.pos
                blue_rect.x = mouse_x + offset_x
                blue_rect.y = mouse_y + offset_y  
            if green_rect_draging:
                mouse_x, mouse_y = event.pos
                green_rect.x = mouse_x + offset_x
                green_rect.y = mouse_y + offset_y      
            if yellow_rect_draging:
                mouse_x, mouse_y = event.pos
                yellow_rect.x = mouse_x + offset_x
                yellow_rect.y = mouse_y + offset_y      
    # - updates (without draws) -

    # empty

    # - draws (without updates) -

    screen.fill(WHITE)
    
    screen.blit(bg, (0, 0))
    pygame.draw.rect(screen, RED, red_rect)
    pygame.draw.rect(screen, BLUE, blue_rect)
    pygame.draw.rect(screen, GREEN, green_rect)
    pygame.draw.rect(screen, YELLOW, yellow_rect)

    pygame.display.flip()

    # - constant game speed / FPS -

    clock.tick(FPS)

# - end -

pygame.quit()