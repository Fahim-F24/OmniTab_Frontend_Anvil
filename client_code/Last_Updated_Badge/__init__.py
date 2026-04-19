from ._anvil_designer import Last_Updated_BadgeTemplate
from anvil import *


class Last_Updated_Badge(Last_Updated_BadgeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
