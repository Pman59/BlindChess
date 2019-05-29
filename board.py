from block import Block


class Board():
	def __init__(self):
		self._board = {}
		self._players = {'White': None, 'Black': None}

	def add_players(self, player, side):
		for key in self._player.keys():
			if side == key:
				key = player
				return True
		return False

	def setup_board(self):
		self._board[]

	@property
	def board(self):
		return self._board
	
	@property
	def players(self):
		return self._players
	