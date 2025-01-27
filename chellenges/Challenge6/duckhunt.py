import pygame
import random
import sys
import time

pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Duck Hunt")

# Загрузка иконки
icon = pygame.image.load("/Users/ilya/Documents/GitHub/School/Softwere dev./SD/Leren-programen/chellenges/Challenge6/assets/icon.png")
pygame.display.set_icon(icon)

# Загрузка фона
background = pygame.image.load("/Users/ilya/Documents/GitHub/School/Softwere dev./SD/Leren-programen/chellenges/Challenge6/assets/stage.png")

# Загрузка кадров утки
duck_frames = [
    pygame.image.load("/Users/ilya/Documents/GitHub/School/Softwere dev./SD/Leren-programen/chellenges/Challenge6/assets/2.gif"),
    pygame.image.load("/Users/ilya/Documents/GitHub/School/Softwere dev./SD/Leren-programen/chellenges/Challenge6/assets/0.gif"),
]

# Изменение размера кадров утки
duck_size = (100, 75)
duck_frames = [pygame.transform.scale(frame, duck_size) for frame in duck_frames]
duck_rect = duck_frames[0].get_rect()

# Параметры анимации
duck_frame_index = 0
animation_speed = 10
animation_counter = 0

# Параметры движения утки
duck_speed = [5, 3]
duck_rect.topleft = (random.randint(0, WIDTH - duck_rect.width), random.randint(0, HEIGHT - duck_rect.height))

# Загрузка звуков
shot_sound = pygame.mixer.Sound("Leren-programen/chellenges/Challenge6/assets/uhodyaschee-vdal-eho-posle-pistoletnogo-vyistrela.wav")
doel_raken = pygame.mixer.Sound("/Users/ilya/Documents/GitHub/School/Softwere dev./SD/Leren-programen/chellenges/Challenge6/assets/popadanie-tochno-v-tsel.wav")

# Загрузка фоновой музыки
pygame.mixer.music.load("/Users/ilya/Documents/GitHub/School/Softwere dev./SD/Leren-programen/chellenges/Challenge6/assets/deti-online.com_-_lesa-finlyandii.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

score = 0
ammo = 5 
kills = 0  
font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()
running = True

while running:
    screen.blit(background, (0, 0))  

    animation_counter += 1
    if animation_counter % animation_speed == 0:
        duck_frame_index = (duck_frame_index + 1) % len(duck_frames)

    duck_rect = duck_rect.move(duck_speed)
    if duck_rect.left < 0 or duck_rect.right > WIDTH:
        duck_speed[0] = -duck_speed[0]
    if duck_rect.top < 0 or duck_rect.bottom > HEIGHT:
        duck_speed[1] = -duck_speed[1]

    screen.blit(duck_frames[duck_frame_index], duck_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: 
            if ammo > 0:
                ammo -= 1  
                if duck_rect.collidepoint(event.pos): 
                    doel_raken.play()
                    score += 1
                    kills += 1
                    if kills % 2 == 0: 
                        ammo = 5
                    duck_speed[0] += random.choice([0, 1])
                    duck_speed[1] += random.choice([0, 1])
                    duck_rect.topleft = (random.randint(0, WIDTH - duck_rect.width), random.randint(0, HEIGHT - duck_rect.height))
                else:
                    shot_sound.play() 

   
    if ammo == 0:
        running = False  

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    ammo_text = font.render(f"Ammo: {ammo}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    screen.blit(ammo_text, (10, 50))

    pygame.display.flip()
    clock.tick(60)

message = f"Game Over. Scoren: {score}" 
font = pygame.font.Font(None, 72)  
text = font.render(message, True, (255, 255, 255))  

# Получаем прямоугольник текста и выравниваем его по центру
text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

# Отрисовываем текст на экране
screen.blit(text, text_rect)

# Обновляем экран
pygame.display.flip()
pygame.quit()
time.sleep(5)
sys.exit()
