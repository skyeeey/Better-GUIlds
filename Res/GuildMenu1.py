from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty
from kivy.core.window import Window
from kivy.uix.dropdown import DropDown
from kivy.uix.floatlayout import FloatLayout


class ScrollableLabel(ScrollView):
    text = StringProperty('')


class ChatPage(BoxLayout):
    def __init__(self, **kwargs):
        super(ChatPage, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.history = ScrollableLabel(height=Window.size[1] * 0.5, size_hint_y=None)
        self.new_message = TextInput(width=Window.size[0] * 0.8, size_hint_x=None, height=Window.size[1] * .2,
                                     size_hint_y=None, multiline=False, hint_text = 'Type a message here...')
        self.send = Button(text="Send")
        self.send.bind(on_release=self.on_send_message)

        bottom_line = BoxLayout(orientation='horizontal')
        bottom_line.add_widget(self.new_message)
        bottom_line.add_widget(self.send)

        self.add_widget(self.history)
        self.add_widget(bottom_line)

    def on_send_message(self, instance):
        message = self.new_message.text
        if message:
            # self.history.text.font_size =(100)
            self.history.text += '\n' + message
            self.new_message.text = ""


class GuildScreen(App):
    def build(self):
        self.title = 'GuildMenu'
        self.root = FloatLayout()
        Window.clearcolor = (0, 0, 0, 0)

        search_input = TextInput(
            hint_text='Search for a guild...',
            size_hint=(None, None),
            size=(770, 50),
            pos_hint={'x': 0.3, 'y': 0.95}
        )

        submit = Button(
            text="Search",
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={'x': 0.7, 'y': 0.95},
        )

        class ImageButtons:
            profile_button = Button(
                background_normal='UserProfileButton.png',
                pos_hint={'x': .9, 'y': 0.9},
                size_hint=(None, None)
            )

            toggle_button = Button(
                color=(1, 0, .65, 1),
                background_normal='ToggleButton1.png',
                background_down='ToggleButton2.png',
                size=(700, 100),
                pos_hint={'x': .35, 'y': 0.8},
                size_hint=(None, None)
            )

            board_dimension_text_label = Label(
                text='Board Dimension',
                font_size=30,
                pos_hint={'center_x': 0.5, 'center_y': 0.9}
            )

        class GuildBannerMenu:
            create_guild = Button(
                text="+ Guild",
                font_size=(100),
                size_hint=(None, None),
                size=(500, 200),
                pos_hint={'x': 0.0, 'y': 0.8},
            )

            my_guilds = Button(
                text="My Guild",
                font_size=(100),
                size_hint=(None, None),
                size=(500, 200),
                pos_hint={'x': 0.0, 'y': 0.7},
            )
            people = Button(
                text="My People",
                font_size=(100),
                size_hint=(None, None),
                size=(500, 200),
                pos_hint={'x': 0.0, 'y': 0.6},
            )

        view_guild_members = Button(
            background_normal='DropdownMenuButton.png',
            size=(400, 100),
            size_hint=(None, None),
            pos_hint={'x': 0.8, 'y': 0.8}
        )

        dropdown = DropDown()
        for index in range(10):
            btn = Button(text=f"User {index + 1}", size_hint_y=None, height=40)
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))
            dropdown.add_widget(btn)

        view_guild_members.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance, x: setattr(view_guild_members, 'text', x))

        chat_screen = ChatPage(
            pos_hint={'x': 0.3, 'y': -0.1},
        )

        history = ScrollableLabel(
            pos_hint={'x': 0.5, 'y': .5},
        )

        self.root.add_widget(search_input)
        self.root.add_widget(submit)
        self.root.add_widget(ImageButtons.profile_button)
        self.root.add_widget(ImageButtons.toggle_button)
        self.root.add_widget(ImageButtons.board_dimension_text_label)
        # self.root.add_widget(ImageButtons.chat_button)
        self.root.add_widget(GuildBannerMenu.create_guild)
        self.root.add_widget(GuildBannerMenu.my_guilds)
        self.root.add_widget(GuildBannerMenu.people)
        self.root.add_widget(view_guild_members)
        self.root.add_widget(chat_screen)
        self.root.add_widget(history)


if __name__ == '__main__':
    GuildScreen().run()