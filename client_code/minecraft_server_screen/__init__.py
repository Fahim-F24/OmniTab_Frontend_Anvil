from ._anvil_designer import minecraft_server_screenTemplate
from ..Player_Name_Badge import Player_Name_Badge
from anvil import *


class minecraft_server_screen(minecraft_server_screenTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

    # Run the test list immediately when the app opens
    self.refresh_player_list()

  def refresh_player_list(self):
    self.player_container.clear()

    # Your manual test array
    online_players = ["RampageIsAgo", "TheBigSniffer", "Deku19", "Notch", "Herobrine", "DASDa", "asdok34", "das94dfk", "Herobrine", "DASDa", "asdok34", "das94dfk"] 

    for name in online_players:
      new_badge = Player_Name_Badge(player_name=name)
      self.player_container.add_component(new_badge)
