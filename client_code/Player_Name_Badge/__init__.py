from ._anvil_designer import Player_Name_BadgeTemplate
from anvil import *


class Player_Name_Badge(Player_Name_BadgeTemplate):
  def __init__(self, **properties):
    # This takes the properties passed from Form1 and applies them
    self.init_components(**properties)

  @property
  def player_name(self):
    return self.label_1.text

  @player_name.setter
  def player_name(self, value):
    # This connects the "property" to the physical "label"
    self.label_1.text = value

    # Any code you write here will run before the form opens.
