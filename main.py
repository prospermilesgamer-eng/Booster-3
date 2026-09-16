from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.properties import NumericProperty
from kivy.uix.screenmanager import ScreenManager, Screen
import random

KV = """
<BoostScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: 20
        spacing: 15
        canvas.before:
            Color:
                rgba: 0.05, 0.05, 0.18, 1
            Rectangle:
                pos: self.pos
                size: self.size
        Label:
            text: 'BOOST MAX ROCKET'
            font_size: 26
            bold: True
        Label:
            id: rocket
            text: '🚀'
            font_size: 80
        Label:
            id: fire
            text: '🔥🔥🔥'
            font_size: 28
        Label:
            text: f'{int(root.progress)}%'
            font_size: 65
            bold: True
        ProgressBar:
            value: root.progress
            max: 100
            size_hint_y: None
            height: 12
        Label:
            id: status
            text: 'Ready for launch!'
            size_hint_y: None
            height: 30
        Button:
            text: '🚀 LAUNCH BOOST'
            size_hint_y: None
            height: 70
            background_color: 0,0.8,0.4,1
            bold: True
            on_press: root.start_boost()
"""

class BoostScreen(Screen):
    progress = NumericProperty(0)
    def start_boost(self):
        self.progress = 0
        Clock.schedule_interval(self.update, 0.04)
    def update(self, dt):
        self.progress += 1.5
        self.ids.fire.text = random.choice(['🔥','🔥🔥','🔥🔥🔥','💥'])
        self.ids.status.text = random.choice(['🚀 Igniting...','🔥 Burning junk...','❄️ Cooling...'])
        if self.progress >= 100:
            Clock.unschedule(self.update)
            self.ids.status.text = 'BOOSTED! 47°C -> 31°C Cooled!'
            self.progress = 100
            return False

class BoosterApp(App):
    def build(self):
        Builder.load_string(KV)
        sm = ScreenManager()
        sm.add_widget(BoostScreen(name='boost'))
        return sm

BoosterApp().run()
