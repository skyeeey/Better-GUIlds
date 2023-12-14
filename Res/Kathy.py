from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.graphics import Color, Rectangle, Ellipse
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import StringProperty
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.bubble import Bubble, BubbleButton
from kivy.core.window import Window
from kivy.uix.dropdown import DropDown
from kivy.uix.togglebutton import ToggleButton


class ScrollableLabel(ScrollView):
    text = StringProperty('')

    def __init__(self, initial_text='', **kwargs):
        super(ScrollableLabel, self).__init__(**kwargs)
        self.label = Label(text=initial_text, color=(1, 0, 0, 1), font_size=(30), markup=True)
        self.label.bind(size=self._update_label)
        self.add_widget(self.label)

    def _update_label(self, instance, value):
        self.label.text_size = (self.width, None)
        self.label.texture_update()
        self.height = self.label.texture_size[1]

    def update_text(self, new_text):
        self.label.text += '\n' + new_text

class ChatPage(FloatLayout):
    def __init__(self, **kwargs):
        super(ChatPage, self).__init__(**kwargs)
        self.size_hint = (1, 1)

        # Pre-add some initial text to the ScrollableLabel
        initial_text = "*This is the begining of your chat with Kathy*\n"
        self.chat_history = ScrollableLabel(initial_text=initial_text, size_hint=(.4, 0.6), pos_hint={'x': 0.01, 'y': 0.3})
        self.current_chat_history = self.chat_history


        self.new_message = TextInput(pos_hint={'x': 0.0, 'y': 0.1},
                                    size_hint_x=(0.4),
                                    size_hint_y=(.06), multiline=True, hint_text='Type a message here...')
        self.send = Button(pos_hint={'x': 0.4, 'y': 0.1}, text="Send", size_hint_y=(.06), size_hint_x=(.1), height=self.new_message.height)
        self.send.bind(on_release=self.on_send_message)

        # Bind the on_text_validate event to the on_send_message function
        self.new_message.bind(on_text_validate=self.on_send_message)

        self.add_widget(self.chat_history)
        self.add_widget(self.new_message)
        self.add_widget(self.send)

    def on_send_message(self, instance):
        if self.current_chat_history == self.chat_history:
            message = self.new_message.text
            if message:
                prefix = "*You*: "
                self.chat_history.update_text(f"{prefix}{message}")
                self.new_message.text = ""


class GuildScreen(Screen):
    def __init__(self, **kwargs):
        super(GuildScreen, self).__init__(**kwargs)

        self.title = 'GuildMenu'
        layout = FloatLayout()
        Window.clearcolor = (0, 0, 0, 0)

        self.search_input = TextInput(
            hint_text='Search for a guild...',
            size_hint=(None, None),
            size=(770, 50),
            pos_hint={'x': 0.3, 'y': 0.95}
        )

        self.submit = Button(
            text="Search",
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={'x': 0.7, 'y': 0.95},
        )

        self.profile_button = Button(
            background_normal='UserProfileButton.png',
            pos_hint={'x': .9, 'y': 0.9},
            size_hint=(None, None)
        )
        self.kathy_text_label = Label(
            text='Chat with Kathy',
            font_size=45,
            pos_hint={'center_x': 0.5, 'center_y': 0.83}
        )

        self.guild_banner_menu = GridLayout(cols=1)
        self.create_guild = Button(
            text="+ Guild",
            size_hint=(None, None),
            size=(300, 100),
            pos_hint={'x': 0.0, 'y': 0.8},
        )
        self.my_guilds = Button(
            text="My Guild",
            size_hint=(None, None),
            size=(300, 100),
            pos_hint={'x': 0.0, 'y': 0.7},
        )
        self.people = Button(
            text="My People",
            size_hint=(None, None),
            size=(300, 100),
            pos_hint={'x': 0.0, 'y': 0.6},
        )
        self.guild_banner_menu.add_widget(self.create_guild)
        self.guild_banner_menu.add_widget(self.my_guilds)
        self.guild_banner_menu.add_widget(self.people)

        self.chat_screen = ChatPage(
            pos_hint={'x': 0.3, 'y': -0.1},
        )

        self.history = ScrollableLabel(
            pos_hint={'x': 0.3, 'y': .5},
        )

        layout.add_widget(self.search_input)
        layout.add_widget(self.submit)
        layout.add_widget(self.profile_button)
        layout.add_widget(self.kathy_text_label)
        layout.add_widget(self.guild_banner_menu)
        layout.add_widget(self.chat_screen)
        layout.add_widget(self.history)

        self.add_widget(layout)

    # def submit(self, instance):
    #     search = self.search_input.text
    #     # Here, you can process the submitted weight and height as needed
    #     # For example, you can print them to the console
    #     print(f"Stuff from search bar: {search}")


if __name__ == '__main__':
    GuildScreen().run()