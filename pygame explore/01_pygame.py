import pygame
import sys
import time

pygame.init()

screen = pygame.display.set_mode((640, 480)) 
pygame.display.set_caption("Day 1 - 이벤트 처리")

bg_color = (255, 255, 255) #화면 색상을 바꾸기위해서 변수 지정
#circle_positions = []

#사각형 초기 위치 선언 게임 실행할 동안만 변수
rect_x = 300
rect_y = 220
speed = 5

circle_data = [] #생성된 시간이랑 위치 list로 저장
circle_lifetime = 0.5 #지속시간 (단위: 초)

clock = pygame.time.Clock()

running = True
while running:
    current_time = time.time() #시간은 제일 위에서 갱신시킬 것!
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #창닫기
            running = False    
            
        elif event.type == pygame.KEYDOWN: #키보드 눌림
            print(f"키 눌림: {pygame.key.name(event.key)}")
            
            #화면 색 바꾸기
            if event.key == pygame.K_r: #빨강
                bg_color = (255, 0, 0)
            elif event.key == pygame.K_g: #초록
                bg_color = (0, 255, 0) 
            elif event.key == pygame.K_b: #파랑
                bg_color = (0, 0, 255) 
            
            #사각형 움직이는 화살표키 배당
            if event.key == pygame.K_LEFT:
               rect_x -= speed #rect_x = rect_x -speed
            elif event.key == pygame.K_RIGHT:
                rect_x += speed
            elif event.key == pygame.K_UP:
                rect_y -= speed
            elif event.key == pygame.K_DOWN:
                rect_y += speed
            
             #사각형 이동 제한
            rect_y = max(0, min(480 - 50, rect_y))
            rect_x = max(0, min(640 - 50, rect_x))
        
        elif event.type == pygame.MOUSEBUTTONDOWN: #마우스 눌림
            
             #클릭한 좌표
            print(f"마우스 클릭 위치: {event.pos}")
            pos = event.pos
            
            ''' #원 그리기
            circle_positions.append(pos)
            print(f"원 추가: {pos}")'''
            
            circle_data.append((event.pos, current_time)) #tupple(좌표, 현재시간) 저장
            
    #오래된 원 제거        
    circle_data = [
        (pos, t) for (pos, t) in circle_data
        if current_time - t < circle_lifetime
    ]
    
    #화면 그리기
    screen.fill(bg_color) #screen.fill((200, 200, 200)) #화면 색상 연회색으로 설정
    pygame.draw.rect(screen, (255, 0, 0), (rect_x, rect_y, 50, 50))

    #화면 채운 뒤 원 그리기<<(위치, 시간)data
    #for pos in circle_positions:
    for pos, t in circle_data:
        pygame.draw.circle(screen, (0,0,255), pos, 20) #파란 원
    
    pygame.display.update() #화면 갱신
    clock.tick(60)
    
pygame.quit()
sys.exit()