from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivy.uix.boxlayout import BoxLayout

# Define the KV language string
KV = '''
ScreenManager:
    MainScreen:

<MainScreen>:
    name: "main"
    BoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)
        MDRaisedButton:
            text: "Click Me!"
            pos_hint: {"center_x": .5}
            on_release: app.show_label_text()
        MDLabel:
            id: label_message
            text: ""
            halign: "center"
'''

class MainScreen(Screen):
    pass

class MyApp(MDApp):
    def build(self):
        return Builder.load_string(KV)
    
    def show_label_text(self):
        # Get the label by its ID and set the text
        label = self.root.get_screen('main').ids.label_message
        label.text = "Hello, this is a label!"


if __name__ == "__main__":
    MyApp().run()
