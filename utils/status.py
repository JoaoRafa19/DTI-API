class GameNotFound:
  def __init__(self):
    super().__init__()

class GameEnded:
  def __init__(self, winner):
    super().__init__()
    self.winner = winner
