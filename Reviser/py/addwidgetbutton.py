from kivymd.uix.button import MDFloatingActionButton

class AddWidgetButton(MDFloatingActionButton):
    def __init__(self, **kwargs):
        super(AddWidgetButton, self).__init__(**kwargs)
        
    def on_release(self):
        print('Widget Added')
