import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout

class Login(GridLayout):
    def __init__(self, **kwargs):
        super(Login, self).__init__(**kwargs)
        self.cols = 2

        self.add_widget(Label(text="Nama"))
        self.nama = TextInput(multiline=False)
        self.add_widget(self.nama)
        
        self.add_widget(Label(text="kata-kata sandi"))
        self.sandi = TextInput(multiline=False, password=True)
        self.add_widget(self.sandi)        
class aplikasi(App):
    def build(self):
        return Login()
    
aplikasi().run()