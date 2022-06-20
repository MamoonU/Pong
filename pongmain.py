#Pong by Mamoon Umar 2022
#Small arcade game called pong made using pygame library and internet resources
#Please enjoy



#Importing game library as well as ball and paddle files
import pygame
from random import randint

#Initialises all imported pygame modules 
pygame.init()

#class
class Paddle(pygame.sprite.Sprite):
	def __init__(self, color, width, height):
		super().__init__()

		#set
		self.image = pygame.Surface([width, height])
		self.image.fill(BLACK)
		self.image.set_colorkey(BLACK)

		#draw paddle
		pygame.draw.rect(self.image, color, [0, 0, width, height])

		#fetch rectangle
		self.rect = self.image.get_rect()


	#moving up
	def moveUp(self, pixels):
		self.rect.y -= pixels
		if self.rect.y < 0:
			self.rect.y = 0

	#moving down
	def moveDown(self, pixels):
		self.rect.y += pixels
		if self.rect.y > 500:
			self.rect.y = 500

#class
class Ball(pygame.sprite.Sprite):
	def __init__(self, color, width, height):
		super().__init__()

		#set
		self.image = pygame.Surface([width, height])
		self.image.fill(BLACK)
		self.image.set_colorkey(BLACK)

		#draw ball
		pygame.draw.rect(self.image, color, [0, 0, width, height])

		#velocity
		self.velocity = [randint(4,8),randint(-8,8)]

		#fetch rectangle
		self.rect = self.image.get_rect()

	#update
	def update(self):
		self.rect.x += self.velocity[0]
		self.rect.y += self.velocity[1]

	#bounce
	def bounce(self):
		self.velocity[0] = -self.velocity[0]
		self.velocity[1] = randint(-8, 8)

#RGB value of colours
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)

#Window size and Miscellaneous 
size = (1000, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pygame Pong")
carryOn = True
clock = pygame.time.Clock()

#Paddles settings (Colour, Size)
paddle1 = Paddle(RED, 20, 100)
paddle1.rect.x = 0
paddle1.rect.y = 250
paddle2 = Paddle(BLUE, 20, 100)
paddle2.rect.x = 980
paddle2.rect.y = 250

#Ball Settings (Colour, Size)
ball = Ball(WHITE, 10, 10)
ball.rect.x = 345
ball.rect.y = 195

#spritelist
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(paddle1)
all_sprites_list.add(paddle2)
all_sprites_list.add(ball)

#score
scoreA = 0
scoreB = 0

#main
while carryOn:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			carryOn = False

	#paddle movement
	keys = pygame.key.get_pressed()
	if keys[pygame.K_w]:
		paddle1.moveUp(5)
	if keys[pygame.K_s]:
		paddle1.moveDown(5)
	if keys[pygame.K_UP]:
		paddle2.moveUp(5)
	if keys[pygame.K_DOWN]:
		paddle2.moveDown(5)

	all_sprites_list.update()

	#ball check
	if ball.rect.x >= 990:
		scoreA += 1
		ball.velocity[0] = -ball.velocity[0]
	if ball.rect.x <= 0:
		scoreB += 1
		ball.velocity[0] = -ball.velocity[0]
	if ball.rect.y > 590:
		ball.velocity[1] = -ball.velocity[1]
	if ball.rect.y < 0:
		ball.velocity[1] = -ball.velocity[1]

	if pygame.sprite.collide_mask(ball, paddle1) or pygame.sprite.collide_mask(ball, paddle2):
		ball.bounce()

	#drawing
	screen.fill(BLACK)
	pygame.draw.line(screen, WHITE, [500, 0], [500, 600], 5)
	all_sprites_list.draw(screen)

	#score display
	font = pygame.font.Font(None, 74)
	text = font.render(str(scoreA), 1, WHITE)
	screen.blit(text, (25, 10))
	text = font.render(str(scoreB), 1, WHITE)
	screen.blit(text, (950, 10))

	#screen update
	pygame.display.flip()
	clock.tick(80)

#quit
pygame.quit()