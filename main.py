import time

from kivymd.app import MDApp
from threading import Thread
from kivy.core.window import Window
from kivy.lang import Builder

Window.size = (500, 650)

KV = """
ScreenManager:
    
    Screen:
        name: "home"
        FloatLayout:
            canvas:
                Color:
                    rgba: .3, .66, 9, .9
                Rectangle:
                    source: "img/shad.jpg"
                    size: self.size
                    pos: self.pos
            MDLabel:
                id: my_label
                text: ""    
                font_style: "H3"
                halign: "center"


"""

class MyApp(MDApp):

    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        Thread(target=self.update_text).start()


    def update_text(self):
        message = f"Hier is Message for typing string\n" \
                  f"Hier you must writing all what you wont!"
        for i in message:
            if i == "\n":
                time.sleep(2)
                self.root.ids.my_label.text = " "
            else:
                time.sleep(0.28)
                self.root.ids.my_label.text += i


if __name__ == "__main__":
    MyApp().run()