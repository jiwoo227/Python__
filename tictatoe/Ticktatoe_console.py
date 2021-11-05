from tictatoe.tictatoe_game_engine import TictatoeGameEngine

class TictactoeConsole:
	def __init__(self):
		self.game_engine = TictatoeGameEngine()

	def play(self):
		self.game_engine.show_board()
		while True:
			row = int(input('행:'))
			col = int(input('열:'))
			self.game_engine.set(row,col)
			self.game_engine.show_board()
			winner = self.game_engine.set_winner()
			if winner == 'X' or winner =='O':
				print(f'{winner} 이겻져요')
				break

			elif winner == 'd':
				print('무승부양')
				break

			self.game_engine.change_turn()

if __name__ == '__main__':
	ttt_console = TictactoeConsole()
	ttt_console.play()