import kivy

kivy.require('2.0.0')

from kivy.app import App

#import some library
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.bubble import Bubble, BubbleButton
from kivy.core.window import Window


class MyApp(App):
    def build(self):

        #create float layout
        self.root = FloatLayout()
        Window.clearcolor = (0,0,0,0)

        #add button to layout
        #button = Button(text = "Press here to read the rules of BetterGUIlds...", 
                       # on_press = self.show_bubble)

        #now add button to layout
       # self.root.add_widget(button)

        #return self.root

        bubble1 = Bubble(orientation = "horizontal",
                        size_hint = (None, None),
                        size = (800, 350),
                        #pos_hint = {'center_x': 0.5, 'center_y': 0.5})
                        pos_hint = {'x':0.05, 'y':0.8})
        
        bubble2 = Bubble(orientation = "horizontal",
                        size_hint = (None, None),
                        size = (800, 350),
                        #pos_hint = {'center_x': 0.5, 'center_y': 0.9})
                        pos_hint = {'x':0.4, 'y':0.45})

        
        bubble3 = Bubble(orientation = "horizontal",
                        size_hint = (None, None),
                        size = (800, 350),
                        pos_hint = {'center_x': 0.85, 'center_y': 0.1})
        
        #now add buttons to bubble (cut copy and paste)
        button1 = BubbleButton(text = "1) Guilds are a place for like-minded\npeople to come together.", font_size ='20sp')
        button2 = BubbleButton(text = "2) Make posts, send messages, and\nparticipate in guild events!\nAn active guild is a thriving guild :)", font_size ='20sp')
        button3 = BubbleButton(text = "3) Guild space is limited!\nMaximum size of a guild is 25 members!\nFight for your place in the guild!\nNobody likes a spectator!", font_size ='20sp')
        
       # button3 = BubbleButton(text = "Paste")

        #now add buttons to bubble
        bubble1.add_widget(button1)
        bubble2.add_widget(button2)
        bubble3.add_widget(button3)
       # bubble.add_widget(button3)
    

        #finally add bubble to root(float layout)
        self.root.add_widget(bubble1)
        self.root.add_widget(bubble2)
        self.root.add_widget(bubble3)


if __name__ == '__main__':
    MyApp().run()