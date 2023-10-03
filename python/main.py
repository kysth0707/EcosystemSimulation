import pygame

# ============== 라이브러리 기본 설정 ==============
pygame.font.init()
pygame.mixer.init()
pygame.init()


# ============== 변수 설정 ==============
FONT_PATH = r"E:\GithubProjects\EcosystemSimulation\python\malgunbd.ttf"
SCREEN_RATIO = (16, 9)
SCREEN_RESOULUTION = (SCREEN_RATIO[0] * 70, SCREEN_RATIO[1] * 70)
FPS = 60

font20 = pygame.font.Font(FONT_PATH, 20) # 폰트 설정
fpsClock = pygame.time.Clock() # 프레임 조절기


# ============== 화면 최초 설정 ==============
screen = pygame.display.set_mode(SCREEN_RESOULUTION, pygame.RESIZABLE)
pygame.display.set_caption(f"생태계 시스템 예상 프로그램 - by kysth0707(github)")

run = True
while run:
	# ============== 화면 업데이트 ==============
	screen.fill((50,50,50))
	pygame.display.update()

	# ============== 이벤트 처리 ==============
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			print("QUIT")

			run = False
			pygame.quit()
			break

		elif event.type == pygame.VIDEORESIZE:
			w, h = pygame.display.get_surface().get_size()
			SCREEN_RESOULUTION = (w, int(w * SCREEN_RATIO[1] / SCREEN_RATIO[0]))
			screen = pygame.display.set_mode(SCREEN_RESOULUTION, pygame.RESIZABLE)

			# w : ? = SCREEN_RATIO[0], SCREEN_RATIO[1]
			# ? = w * SCREEN_RATIO[1] / SCREEN_RATIO[0]

	fpsClock.tick(FPS) # 프레임 설정