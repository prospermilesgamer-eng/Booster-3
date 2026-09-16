from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.properties import NumericProperty
from kivy.uix.screenmanager import ScreenManager, Screen
KV="""
<BoostScreen>:
 BoxLayout:
  orientation:'vertical'
  padding:20
  Label:
   text:'BOOST MAX ROCKET'
   font_size:24
   bold:True
  Label:
   text:str(int(root.progress))+'%'
   font_size:80
  ProgressBar:
   value:root.progress
   max:100
  Button:
   text:'LAUNCH BOOST'
   height:60
   size_hint_y:None
   on_press:root.start_boost()
<DoneScreen>:
 BoxLayout:
  orientation:'vertical'
  Label:
   text:'BOOSTED!'
  Button:
   text:'AGAIN'
   on_press:app.root.current='boost'
"""
class BoostScreen(Screen):
 progress=NumericProperty(0)
 def start_boost(self):
  self.progress=0
  Clock.schedule_interval(self.update,0.04)
 def update(self,dt):
  self.progress+=2
  if self.progress>=100:
   Clock.unschedule(self.update)
   self.manager.current='done'
   self.progress=0
   return False
class DoneScreen(Screen):pass
class BoosterApp(App):
 def build(self):
  Builder.load_string(KV)
  sm=ScreenManager()
  sm.add_widget(BoostScreen(name='boost'))
  sm.add_widget(DoneScreen(name='done'))
  return sm
BoosterApp().run()
