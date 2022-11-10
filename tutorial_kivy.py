from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout

class TutorialApp(App):
    def build(self):
        b = BoxLayout(orientation="vertical")
        t = TextInput(font_size=150, text="default",
        size_hint_y=None, height=200)
        f = FloatLayout()
        s = Scatter()
        l = Label(text="Hello", font_size=150)
        
        
        f.add_widget(s)
        s.add_widget(l)
        
        b.add_widget(f)
        b.add_widget(t)
        return b

if __name__ == "__main__":
    TutorialApp().run()