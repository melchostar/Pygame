import pygame

pygame.init()

# 화면 설정
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("더 헤르타")

# FPS
clock = pygame.time.Clock()



#캐릭터 불러오기
character = pygame.image.load("06_pygame/The Herta the reading.jpg")
character = pygame.transform.scale(character, (50, 50))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width - screen_width)//2
character_y_pos = screen_height - character_height

# 적 캐릭터 불러오기
enemy = pygame.image.load("06_pygame/creeper.jpg")
enemy = pygame.transform.scale(enemy, (50, 50))
enemy_x_pos = 300
enemy_y_pos = 200

#이동할 좌표
to_x = 0
to_y = 0
speed = 5

# 이벤트
running = True
while running:
    dt = clock.tick(60) #초당 프레임
    
    
    # 메인 루프 안에서
    character_rect = character.get_rect(topleft=(character_x_pos, character_y_pos))
    enemy_rect = enemy.get_rect(topleft=(enemy_x_pos, enemy_y_pos))

    if character_rect.colliderect(enemy_rect):
        print("충돌!")
        running = False
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # 키누름
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= speed
            elif event.key == pygame.K_RIGHT:
                to_x += speed
            elif event.key == pygame.K_UP:
                to_y -= speed
            elif event.key == pygame.K_DOWN:
                to_y += speed
                
        # 키 뗌
        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                to_x = 0
            if event.key in [pygame.K_UP, pygame.K_DOWN]:
                to_y = 0
        # 충돌 감지
        if character_rect.colliderect(enemy_rect):
            print("충돌했어요!")
            running = False

        
        #위치 반영
    character_x_pos += to_x
    character_y_pos += to_y
        
        #경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
        
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height
        
        # 화면 갱신, 그리기
    screen.fill((255, 255, 255))
    screen.blit(character,(character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))
        
    pygame.display.update()
    
pygame.quit()