from kivy.core.window import Window
from kivy.metrics import dp
from kivy.utils import platform
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, FadeTransition, NoTransition
from cam import Cam
from signup import Signup, Pop_up
from login import Login
from menu import Menu, Pop_up
from menu_2 import Menu_2
from buchen import Buchen



#Window.size=(400,800)
#Window.clearcolor = (0.23, 0.23 , 0.23, 1)
class Interface(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.transition=NoTransition()
        buchen=Buchen()
        cam=Cam()
        signup=Signup()
        login=Login()
        menu=Menu()
        menu_2=Menu_2()
        self.add_widget(login)
        self.add_widget(buchen)

        self.add_widget(menu)


        self.add_widget(signup)
        self.add_widget(menu_2)
        self.add_widget(cam)


class BarcodeApp(MDApp):
    def build(self):
        if platform == 'android':
            from android.permissions import request_permissions, Permission
            request_permissions([Permission.WRITE_EXTERNAL_STORAGE, Permission.CAMERA, Permission.RECORD_AUDIO])
        return Interface()


if __name__ == '__main__':
    BarcodeApp().run()