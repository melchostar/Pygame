import pygame
import sys

# Pygame 초기화
pygame.init()

# 화면 크기 설정
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# 타이틀 설정
pygame.display.set_caption("Day 1 - Pygame Window")

# 게임 루프 시작
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 창 닫기 버튼 누르면
            running = False

    # 화면을 하얀색으로 채움 (RGB)
    screen.fill((255, 255, 255))

    # 화면 업데이트
    pygame.display.update()

# 종료 처리
pygame.quit()
sys.exit()
