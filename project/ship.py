import pygame
from pygame.sprite import Sprite
class Ship(Sprite):
	
	def __init__(self, ai_settings, screen):
		"""initialize the ship and set its starting position"""
		super(Ship, self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings
		
		#load the ship image and get its rect
		self.image = pygame.image.load(r'project\\images\ship.svg') #return a surface of ship
		self.image_size =(38, 50)
		self.image = pygame.transform.scale(self.image, self.image_size)
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		
		#start each new ship at the bottom center of the screen
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
		self.center = float(self.rect.centerx)
		
		# movement flags
		self.moving_right = False
		self.moving_left = False
		
	def update(self):
		"""Update the the ship's position based on the movement flags"""
		#update the ship's center value not rect.
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center -= self.ai_settings.ship_speed_factor
		
		#update the rect object from self.center
		self.rect.centerx = self.center
			
	def blitme(self):
		"""Draw the ship at its current location"""
		self.screen.blit(self.image, self.rect)
		
	def center_ship(self):
		"""center the ship on the screen"""
		self.center = self.screen_rect.centerx
