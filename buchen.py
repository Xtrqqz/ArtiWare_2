from camera4kivy import Preview
from kivy.clock import mainthread
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen
from PIL import Image
from pyzbar.pyzbar import decode

Builder.load_string("""
#: import CRoundedButton custom_widgets
<Buchen>:
    name:"buchen"
    canvas.before:
        Color:
            rgb: 0.23, 0.23 , 0.23, 1
        Rectangle:
            pos: self.pos
            size: self.size

    BoxLayout:
        orientation: "vertical"
        #padding:[0,dp(0), 0,dp(15)]
        #spacing: dp(10)
        AnchorLayout:
            anchor_x: 'right'
            anchor_y: 'bottom'
            size_hint: 1, 0.05
            #padding:[0,dp(0), dp(15),dp(0)]
            
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
            size_hint: 1, 0.10
            padding:[dp(120), dp(20), dp(10),0]
            BoxLayout:
                size_hint_x:None
                width:self.minimum_width
                Label:
                    text: "Einbuchen"
                    font_size: dp(30)
                    font_name:"Roboto-Black.ttf"
        BoxLayout:
            orientation: "vertical"
            size_hint: 1, 0.70
            padding:[dp(60), dp(0), dp(60),dp(20)]
            spacing: dp(20)
            
            ###########################################Artikel Eingabe
            BoxLayout:
                spacing: dp(10)
                orientation: "vertical"
                size_hint: 1, 0.40
                padding:[dp(0), dp(0), dp(0),dp(50)]
                Label:
                    text:"Artikel-Nr.:"
                    size_hint_x:None
                    size:self.texture_size
                    font_name:"Roboto-Thin.ttf"
                    font_size: dp(20)
                ##### Artikel Nr.
                BoxLayout:
                    spacing: dp(8)
                    size_hint_y:None
                    height:dp(35)  
                    TextInput:
                        id:qr_code_buchen_artikel
                        padding:[dp(10), dp(8), dp(0),dp(0)]
                        size_hint: 0.80, 1
                        hint_text:"Scanne Artikel"  
                        font_name:"Roboto-Italic.ttf"
                        font_size: dp(15)
                    Button:
                        size_hint: 0.20, 1
                        background_normal:"qr_scan.png"
                        #ackground_down:"home_2_pressed.png" 
                        on_press:root.popup_cam_show()   
                
                ##### Stückzahl
                BoxLayout:
                    size_hint_y:None
                    height:dp(35)
                    padding:[dp(0), dp(0), dp(60),dp(0)]
                    spacing: dp(15)
                    Label:
                        size_hint_x:None
                        size:self.texture_size
                        text:"Stückzahl:"
                        font_name:"Roboto-Thin.ttf"
                        font_size: dp(20)
                    TextInput:
                        hint_text:""
                        font_name:"Roboto-Italic.ttf"
                        font_size: dp(15)
            
            ##########################################Lagerplatz Eingabe
            BoxLayout:
                size_hint: 1, 0.30
                spacing: dp(10)
                orientation: "vertical"
                padding:[dp(0), dp(0), dp(0),dp(50)]
                Label:
                    text:"Lagerplatz-Nr.:"
                    size_hint_x:None
                    size:self.texture_size
                    font_name:"Roboto-Thin.ttf"
                    font_size: dp(20)
                     
                ##### Artikel Nr.
                BoxLayout:
                    spacing: dp(8)
                    size_hint_y:None
                    height:dp(35) 
                    TextInput:
                        padding:[dp(10), dp(8), dp(0),dp(0)]
                        size_hint: 0.80, 1
                        hint_text:"Scanne Lagerplatz"  
                        font_name:"Roboto-Italic.ttf"
                        font_size: dp(15)
                    Button:
                        size_hint: 0.20, 1
                        background_normal:"qr_scan.png"
                        #ackground_down:"home_2_pressed.png"   
            
            
            #Navigation
            BoxLayout:
                size_hint: 1, 0.30
                orientation: "vertical"
                spacing: dp(20)
                CRoundedButton:
                    text:"speichern"
                    font_name:"Roboto-Bold.ttf"
                    font_size: dp(20)
                    size_hint_y:None
                    height:dp(50)
                    #on_release:root.switch_to_signup()
                CRoundedButton:
                    text:"zurück"
                    font_name:"Roboto-Bold.ttf"
                    font_size: dp(20)
                    size_hint_y:None
                    height:dp(50)
                    on_release:root.switch_to_menu()
        
        BoxLayout:
            size_hint: 1, 0.05
        
        
        AnchorLayout:
            canvas.before:
                Color:
                    rgb: 0, 0 , 0, 1
                Rectangle:
                    pos: self.pos
                    size: self.size
            
            #anchor_x: 'center'
            #anchor_y: 'bottom'
            size_hint: 1, 0.108
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
        

""")
class Pop_up(Popup):
    def __init__(self, screen_manager, **kwargs):
        super(Pop_up, self).__init__(**kwargs)
        self.screen_manager = screen_manager



    def on_kv_post(self, obj):
        # Ändere die Kamera-ID auf "zwei"
        self.ids.preview.connect_camera(camera_id="0", enable_analyze_pixels=True, default_zoom=0.0)

    @mainthread
    def got_result(self, result):
        string = str(result)
        self.ids.ti.text = string[2:-1]
        signup_screen = self.screen_manager.get_screen("buchen")
        signup_screen.ids.qr_code_buchen_artikel.text = self.ids.ti.text

        # Kamera-Verbindung trennen
        self.ids.preview.disconnect_camera()

        # Popup schließen
        self.dismiss()

class Buchen(Screen):
    def switch_to_menu(self):
        self.manager.current = "menu"
    def switch_to_menu_2(self):
        self.manager.current = "menu_2"

    def switch_to_signup(self):
        self.manager.current = "signup"

    def popup_cam_show(self):
        popup = Pop_up(screen_manager=self.manager)  # Pass the ScreenManager reference
        popup.signup_screen = self
        popup.open()

    def safe_value(self):
        value = "testCODE"
        if 'qr_code' in self.ids:
            self.ids.qr_code.text = str(value)
        else:
            print("Error: 'qr_code' not found in ids dictionary")