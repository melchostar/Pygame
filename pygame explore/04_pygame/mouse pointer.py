import pygame
import sys
import time

pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) #화면 설정 pygame.FULLSCREEN은 상수
curser = pygame.image.load("pygame.py/Herta.jpg")
pygame.display.set_caption("min project - make mouse pointer") # 타이틀 설정
pygame.mouse.set_visible(False) #기본 커서 숨기기
screen.blit(curser,pygame.mouse.get_pos()) #이미지 파일로 커서모양 바꾸기

bg_color = (255,255, 255)

circle_data = []
circle_lifetime = 0.5

clock = pygame.time.Clock()

running = True
while running:
    current_time = time.time() #시간 갱신
    
    for event in pygame.event.get():
        if event.type == pygame.quit:
            running = False
        
        elif event.type == pygame.KEYDOWN:
            print(f"{pygame.key.name(event.key)} 키 눌림")
            if event.key == pygame.K_ESCAPE: #ESC 키 눌리면 종료
                running = False        
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(f"마우스{event.type} 클릭 위치: {event.pos}") #좌클릭
            pos = event.pos
        
        '''elif event.type == pygame.MOUSEWHEEL:
            print(f"마우스 휠:{event.pos}")'''
            
    circle_data.append((event.pos, current_time)) #튜플로 저장
    circle_data = [
        (pos, t) for (pos, t) in circle_data
        if current_time - t < circle_lifetime
    ]#오래된 원 제거
    
    screen.fill(bg_color) #화면 색
    for pos, t in circle_data:
        pygame.draw.circle(screen, (200,0,0), pos, 20) #빨간 원
    
    pygame.display.update() #화면 갱신
    clock.tick(60)
pygame.quit()
sys.exit()