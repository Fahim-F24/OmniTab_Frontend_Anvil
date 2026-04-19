from ._anvil_designer import minecraft_server_screenTemplate
from anvil import *


class minecraft_server_screen(minecraft_server_screenTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  @handle("button_1", "click")
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form2')
