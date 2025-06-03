import pygame
import sys

pygame.init() #초기화
character = pygame.image.load("02_pygame/Malleus Draconia.jpg")#이미지 객체 만들기
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) #화면 설정 pygame.FULLSCREEN은 상수
pygame.display.set_caption("Day 2 - Pygame image load, moving character") # 타이틀 설정

rect_x = 300 #초기값
rect_y = 220
speed = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.quit:  # 창 닫기 버튼 누르면
            running = False

        elif event.type == pygame.KEYDOWN: #키 배당, 창 안넘게
            print(f"{pygame.key.name(event.key)} 키 눌림")
            
            if event.key == pygame.K_ESCAPE:  # ⬅ ESC 키로 종료
                running = False
            
            if event.key == pygame.K_UP:
                rect_y -= speed
            if event.key == pygame.K_DOWN:
                rect_y += speed
            if event.key == pygame.K_RIGHT:
                rect_x += speed
            if event.key == pygame.K_LEFT:
                rect_x -= speed
                
            #rect_y = max(0, min(pygame.FULLSCREEN, rect_y))
            #rect_x = max(0, min(pygame.FULLSCREEN, rect_x)) 
            rect_y = max(0, min(screen.get_height() - character.get_height(), rect_y)) #character.get_height(), haracter.get_weight() 이미지 크기 조절 함수수
            rect_x = max(0, min(screen.get_width() - character.get_width(), rect_x))
             
    screen.fill((200, 200, 200))        
    screen.blit(character, (rect_x, rect_y)) #문자열 경로가 아니라 변수로
    pygame.display.update() #화면 반영
    
pygame.quit()
sys.exit()






'''✅ 실습 미션 1: 이미지 불러오기
힌트만 줄게!
pygame.image.load("파일명.png") 를 사용해서 이미지 객체를 만들 수 있어.
blit() 함수로 그려주고,
pygame.display.update()로 화면에 반영해줘.

🧠 생각해볼 점:
이미지를 프로젝트 폴더에 어디에 두면 좋을까?
이미지 크기와 위치는 어떻게 설정하지?

✅ 실습 미션 2: 캐릭터 이동 구현
목표는 화살표 키를 누르면 캐릭터가 움직이게 만드는 것!

힌트:
이전에 만든 rect_x, rect_y, speed 변수 기억나지?
screen.blit()에 rect 좌표를 넣으면 이미지도 움직여.
경계 제한도 걸어줘야 화면 밖으로 나가지 않겠지?'''
