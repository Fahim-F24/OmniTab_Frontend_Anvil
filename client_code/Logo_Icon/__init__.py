from ._anvil_designer import Logo_IconTemplate
from anvil import *


class Logo_Icon(Logo_IconTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
