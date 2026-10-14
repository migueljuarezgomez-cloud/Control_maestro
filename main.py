import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class ControlApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        lbl = Label(text="¡Control Maestro Activo!", font_size='24sp')
        btn = Button(text="Iniciar", size_hint=(1, 0.2))
        layout.add_widget(lbl)
        layout.add_widget(btn)
        return layout

if __name__ == '__main__':
    ControlApp().run()
  
