class GameStats():
	"""Track statistics for alien invasion"""
	
	def __init__(self, ai_settings):
		"""Initialize statistics"""
		self.ai_settings = ai_settings
		self.reset_stats()
		#High score should be never reset
		self.high_score = 0
		
		#start Alien invasion in an inactive state.
		self.game_active = False
	
	def reset_stats(self):
		"""Initialize statistics that can change during the game."""
		self.ships_left = self.ai_settings.ship_limit
		self.score = 0
		self.level = 1
