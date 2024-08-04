from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.popup import Popup
from kivy.clock import Clock 


class Autoriz(Screen):
    login = StringProperty('Nika')
    password = StringProperty('password')
    def auth(self):
        if self.ids.login.text != self.login:
            popup = Popup(title = 'Авторизація', content = Label(text='Логін не вірний! Спробуйте ще раз!'), size_hint = (0.8, 0.5))
            popup.open()
        elif self.ids.password .text != self.password:
            popup = Popup(title = 'Авторизація', content = Label(text='Пароль не вірний! Спробуйте ще раз!'), size_hint = (0.8, 0.5))
            popup.open()
        else:
            self.manager.current = 'main'

class Main(Screen):
    logiks = NumericProperty(150)
    def on_enter(self, *args):
        self.promiz = 0
        Clock.schedule_interval(self.tick, 0.01)
        return super().on_enter(*args)
    def tick(self, dt):
        if self.promiz < self.logiks:
            self.promiz += 1
            self.ids.logiks.text = str(self.promiz) + 'логіків'
        else:
            return False
    def exit(self):
        self.manager.current = 'autoriz'
        
class LogikaPCApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Autoriz(name='autoriz'))
        sm.add_widget(Main(name='main'))
        return sm
    
Window.size = (450, 600)

LogikaPCApp().run()