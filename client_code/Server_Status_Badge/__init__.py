from ._anvil_designer import Server_Status_BadgeTemplate
from anvil import *


class Server_Status_Badge(Server_Status_BadgeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
