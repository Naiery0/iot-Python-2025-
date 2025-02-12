# py01_pygame.py
import pygame # pygame 기본모듈 추가
from pygame.locals import QUIT # 종료처리 변수
import sys # 운영체제 시스템 명령

# 기본 변수
pygame.init()
Surface = pygame.display.set_mode((640, 400)) ## tkinter의 geometry
FPSCLOCK = pygame.time.Clock()
pygame.display.set_caption('Pygame Basis')

def main():
    while 1:
        Surface.fill(color='crimson')
        # Surface.fill((255, 255, 255))
        for event in pygame.event.get(): # 키보드 마우스 이벤트
            if event.type == QUIT: # WM_DELETE+WINDOW
                pygame.quit() # Pygame을 종료
                sys.exit( # 윈도우 앱 탈출
                )
        pygame.display.update() # 지금까지 작성 코드를 윈도우창에 표시
        FPSCLOCK.tick(30) # 30프레임 지정

if __name__ == '__main__':
    main()