from ._anvil_designer import Version_BadgeTemplate
from anvil import *


class Version_Badge(Version_BadgeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
