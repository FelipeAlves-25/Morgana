from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Janela(BoxLayout):
  pass

class Construtor(App):
  def build(self):
    return Janela()

Construtor().run()