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

MOUSE_POS = (0, 0)
ROUTE3 = 1351/780 #루트 3의 근삿값

COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_RAINBOW = [
	(255, 0, 0),
	(255, 125, 0),
	(255, 255, 0),
	(0, 255, 0),
	(0, 0, 255),
	(0, 30, 255),
	(100, 0, 255),
]

font20 = pygame.font.Font(FONT_PATH, 20) # 폰트 설정
fpsClock = pygame.time.Clock() # 프레임 조절기

# ============== 함수 설정 ==============
def getPos(xy : tuple) -> tuple:
	"""
	1600, 900 을 기준으로 받은 x, y를\n
	현재 화면 크기에 맞춰 반환합니다.\n
	"""
	x, y = xy
	return (int(x / 1600 * SCREEN_RESOULUTION[0]), int(y / 900 * SCREEN_RESOULUTION[1]))

def getValueX(val : int) -> int:
	"""
	1600, 900 을 기준으로 받은 val을\n
	현재 화면의 x 크기에 맞춰 반환합니다\n
	"""
	return int(val / 1600 * SCREEN_RESOULUTION[0])

def getValueY(val : int) -> int:
	"""
	1600, 900 을 기준으로 받은 val을\n
	현재 화면의 y 크기에 맞춰 반환합니다\n
	"""
	return int(val / 900 * SCREEN_RESOULUTION[1])

# ============== 그리기 함수 설정 ==============

def drawEquilateralTriangleWithBox(xy : tuple, height : int, width : int = 0, color : tuple = (255, 255, 255), outline : int = 0):
	"""
	x, y에 color 색 정삼각형과 width 크기 상자를 그립니다\n
	위쪽 꼭짓점 기준임\n
	"""
	x, y = xy

	if width == 0:
		pygame.draw.polygon(screen, color, [
			[int(x - height / ROUTE3), int(y + height)],
			[x, y],
			[int(x + height / ROUTE3), int(y + height)],
		], outline)
	
	else:
		pygame.draw.polygon(screen, color, [
			[int(x - width / 2 - height / ROUTE3), int(y + height)],
			[int(x - width / 2), y],
			[int(x + width / 2), y],
			[int(x + width / 2 + height / ROUTE3), int(y + height)],
		], outline)

def drawEcoTriangle(xy : tuple, height : int, count : int, data : list, colors : list):
	"""
	생태계 삼각형을 그립니다
	"""
	gap = height / count
	x, y = xy
	for i in range(count):
		triPos = (x, y + gap * i)
		width = i * gap / ROUTE3 * 2
		drawEquilateralTriangleWithBox(
			triPos,
			gap,
			width,
			colors[i]
		)
		
		# 마우스 감지
		if triPos[0] - width / 2 - gap / ROUTE3 < MOUSE_POS[0] and MOUSE_POS[0] < triPos[0] + width / 2 + gap / ROUTE3:
			if triPos[1] < MOUSE_POS[1] and MOUSE_POS[1] < triPos[1] + gap:
				drawEquilateralTriangleWithBox( # 아웃라인 그리기
					triPos,
					gap,
					width,
					COLOR_WHITE,
					6
				)
				

# ============== 화면 최초 설정 ==============
screen = pygame.display.set_mode(SCREEN_RESOULUTION, pygame.RESIZABLE)
pygame.display.set_caption(f"생태계 시스템 예상 프로그램 - by kysth0707(github)")

run = True
while run:
	# ============== 화면 업데이트 ==============
	screen.fill((50,50,50))
	
	# drawEquilateralTriangle(getPos((500, 100)), getValueY(700), COLOR_WHITE)
	drawEcoTriangle(getPos((500, 100)), getValueY(700), 5, [], COLOR_RAINBOW)

	pygame.display.update()

	# ============== 이벤트 처리 ==============
	MOUSE_POS = pygame.mouse.get_pos()
	for event in pygame.event.get():
		if event.type == pygame.QUIT: # 종료 이벤트 처리
			print("QUIT")

			run = False
			pygame.quit()
			break

		elif event.type == pygame.VIDEORESIZE: # 가변적 화면 크기
			w, h = pygame.display.get_surface().get_size()
			SCREEN_RESOULUTION = (w, int(w * SCREEN_RATIO[1] / SCREEN_RATIO[0]))
			screen = pygame.display.set_mode(SCREEN_RESOULUTION, pygame.RESIZABLE)

			# w : ? = SCREEN_RATIO[0], SCREEN_RATIO[1]
			# ? = w * SCREEN_RATIO[1] / SCREEN_RATIO[0]

	fpsClock.tick(FPS) # 프레임 설정