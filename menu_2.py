

from kivy.lang import Builder
from kivy.properties import ObjectProperty

from kivy.uix.screenmanager import Screen


Builder.load_string("""
#: import CRoundedButton custom_widgets
<Menu_2>:
    name:"menu_2"
    canvas.before:
        Color:
            rgb: 0.23, 0.23 , 0.23, 1
        Rectangle:
            pos: self.pos
            size: self.size

    BoxLayout:
        orientation: "vertical"
        

        AnchorLayout:
            anchor_x: 'right'
            anchor_y: 'bottom'
            size_hint: 1, 0.05
            padding:[0,dp(0), dp(15),0]
            BoxLayout:
                
                size_hint_x:None
                width:self.minimum_width
                spacing: dp(5)
                Image:
                    source: "logged_in_guy.png"
                    size_hint: None, None
                    size: dp(20), dp(20)  # Setzen Sie die Größe je nach Bedarf

                Label:
                    text: "User: "
                    size_hint: None, None
                    size: self.texture_size  # Setzen Sie die Breite und Höhe auf die minimale Größe des Textes
                    font_name:"Roboto-Medium.ttf"
                    font_size: dp(15)
                    
                Label:
                    text: "Gjalt Schröder"
                    size_hint: None, None
                    size: self.texture_size  # Setzen Sie die Breite und Höhe auf die minimale Größe des Textes
                    font_name:"Roboto-Medium.ttf"
                    font_size: dp(15)
        AnchorLayout:
            anchor_x: 'left'
            anchor_y: 'top'
            size_hint: 1, 0.20
            padding:[dp(120), dp(20), dp(10),0]
            BoxLayout:
                size_hint_x:None
                width:self.minimum_width
                Label:
                    text: "Artikel buchen"
                    font_size: dp(30)
                    font_name:"Roboto-Black.ttf"
        BoxLayout:
            orientation: "vertical"
            padding:[dp(60), dp(0), dp(60),dp(90)]
            spacing: dp(20)
            size_hint: 1, 0.50
            CRoundedButton:
                text:"Buchen"
                font_name:"Roboto-Bold.ttf"
                font_size: dp(20)
                size_hint_y:None
                height:dp(50)
                on_press:root.switch_to_buchen()
                
            CRoundedButton:
                text:"Ausbuchen"
                font_name:"Roboto-Bold.ttf"
                font_size: dp(20)
                size_hint_y:None
                height:dp(50)
                on_release:root.switch_to_signup()
            CRoundedButton:
                text:"zurück"
                font_name:"Roboto-Bold.ttf"
                font_size: dp(20)
                size_hint_y:None
                height:dp(50)
                on_release:root.switch_to_menu()
                
        
        AnchorLayout:
            canvas.before:
                Color:
                    rgb: 0, 0 , 0, 1
                Rectangle:
                    pos: self.pos
                    size: self.size
            
            #anchor_x: 'center'
            #anchor_y: 'bottom'
            size_hint: 1, 0.09
            padding:[dp(40), dp(10), dp(30),dp(10)]
            BoxLayout:
                spacing: dp(15)
                #padding:[dp(0), dp(0), dp(0),dp(10)]
                
                Button:
                    #text:"Lagerverwaltung"
                    font_size: dp(10)
                    background_normal:"lager.png"
                    background_down:"lager_pressed.png"
                    #size: dp(20), dp(20)
                    #on_press:root.switch_to_menu()
                    
                Button:
                    #text:"Kommisionieren"
                    font_size: dp(10)
                    background_normal:"komissionieren.png"
                    background_down:"komissionieren_pressed.png"
                    #size: dp(20), dp(20)
                    
                Button:
                    #text:"Artikel buchen"    
                    font_size: dp(10)
                    background_normal:"buchen.png"
                    background_down:"buchen_pressed.png"
                    #size: dp(20), dp(20)
                    on_press:root.switch_to_menu_2()
                Button:
                    #text:"Home"    
                    font_size: dp(10)
                    background_normal:"home_2.png"
                    background_down:"home_2_pressed.png"
                    on_press:root.switch_to_menu()
                    #size: dp(20), dp(20)
                    
                
                #Image:
                    #source: "artiware.png"
                    #size_hint: None, None
                    #size: dp(40), dp(40)  # Setzen Sie die Größe je nach Bedarf
                

""")







class Menu_2(Screen):
    def switch_to_menu(self):
        self.manager.current = "menu"

    def switch_to_menu_2(self):
        self.manager.current = "menu_2"

    def switch_to_signup(self):
        self.manager.current = "signup"

    def switch_to_buchen(self):
        self.manager.current = "buchen"
