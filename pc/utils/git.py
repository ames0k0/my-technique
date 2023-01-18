from pathlib import Path


class Local:
  def __init__(self, path: Path):
    self.path = path
  def branch(self):
    pass
  def status(self):
    pass


class Remote:
  def __init__(self, path: Path):
    self.path = path
  def branch(self):
    pass
