from kivymd.app import MDApp
from kivy.lang import Builder
from py.addwidgetbutton import AddWidgetButton
from py.topic import Topic
from kivymd.uix.card import MDCard
from kivymd.utils.fitimage import FitImage
from kivymd.utils.cropimage import crop_round_image, add_corners



class MainApp(MDApp):
    def build(self):
        return Builder.load_file(f'kv/main.kv')

    def change_screen(self, name):
        sc = self.root.ids.sc 
        sc.current = name

MainApp().run()