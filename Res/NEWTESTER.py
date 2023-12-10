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

from Res import createguild


class HomeScreen(App):
    class HomeScreen(Screen):

        def __init__(self, **kwargs):
            super().__init__(kwargs)
            # self.on_addGuild_button_click = createguild.MyApp().run()

    def build(self):
        self.title = 'Home Screen'
        self.root = FloatLayout()
        Window.clearcolor = (0, 0, 0, 0)
        # Use a Label for the description

        search_input = TextInput(
            hint_text='Search for a guild...',
            font_size=(60),
            size_hint=(None, None),
            size=(1880, 100),
            pos_hint={'x': 0.3, 'y': 0.95}
        )

        submit = Button(
            text="Search",
            font_size=(60),
            size_hint=(None, None),
            size=(300, 100),
            pos_hint={'x': 0.8, 'y': 0.95},
            # on_press=self.submit
        )

        class imageButtons():
            # Make Sure Image is in directory
            profileButton = Button(
                background_normal='UserProfileButton.png',
                pos_hint={'x': .9, 'y': 0.9},
                size=(300, 100),
                size_hint=(None, None)
            )

            BoardgameButton = Button(
                color=(1, 0, .65, 1),
                background_normal='DummyGuild.png',
                size=(2000, 500),
                size_hint=(None, None)
                # on_press = self.on_boardgame_button_click
            )

            DummyGuild = Button(
                color=(1, 0, .65, 1),
                background_normal='ActualDummyGuild.png',
                size=(2000, 500),
                size_hint=(None, None)
            )

            PlankGuild = Button(
                color=(1, 0, .65, 1),
                background_normal='PlankGuild.png',
                size=(2000, 500),
                size_hint=(None, None)
            )

        class GuildBannerMenu():
            createGuild = Button(
                text="+ Guild",
                font_size=(100),
                size_hint=(None, None),
                size=(500, 200),
                pos_hint={'x': 0.0, 'y': 0.8},
                # on_press=self.submit
            )

            myGuilds = Button(
                text="My Guild",
                font_size=(100),
                size_hint=(None, None),
                size=(500, 200),
                pos_hint={'x': 0.0, 'y': 0.7},
                # on_press=self.submit
            )
            people = Button(
                text="My People",
                font_size=(100),
                size_hint=(None, None),
                size=(500, 200),
                pos_hint={'x': 0.0, 'y': 0.6},
                # on_press=self.submit
            )

        # class GuildScrolling():
        #     guilds = GridLayout(cols=1, spacing=10, size_hint_y=None)
        #     guilds.bind(minimum_height=self.root.layout.setter('height'))

        #     for i in range(20):
        #         button_text = f"Button {i + 1}"
        #         btn = Button(text=button_text, size=(100, 40), size_hint=(None, None))
        #         guilds.add_widget(btn)

        #     ScrollingGuilds = ScrollView()

        #     ScrollingGuilds.add_widget(guilds)

        class ScrollableGrid(ScrollView):
            def __init__(self, **kwargs):
                super(ScrollableGrid, self).__init__(**kwargs)

                # Create a GridLayout
                self.layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
                self.layout.bind(minimum_height=self.layout.setter('height'))

                self.layout.add_widget(imageButtons.PlankGuild)
                self.layout.add_widget(imageButtons.BoardgameButton)
                self.layout.add_widget(imageButtons.DummyGuild)

                # Add buttons to the GridLayout
                for i in range(7):
                    button_text = f"Fake guild {i + 4}"
                    btn = Button(text=button_text, size=(2000, 500), size_hint=(None, None),
                                 background_normal='FakerGuild.png')
                    self.layout.add_widget(btn)

                # Add the GridLayout to the ScrollView
                self.add_widget(self.layout)

        scrollable_grid = ScrollableGrid(
            pos_hint={'x': 0.3, 'y': -0.1}
        )

        class FakeGuildButton():
            clickable = Button(
                text="+ Guild",
                size_hint=(None, None),
                size=(300, 100),
                pos_hint={'x': 0.0, 'y': 0.8},
                # on_press=self.on_addGuild_button_click
            )

        self.root.add_widget(search_input)
        self.root.add_widget(submit)
        self.root.add_widget(imageButtons.profileButton)
        self.root.add_widget(GuildBannerMenu.createGuild)
        self.root.add_widget(GuildBannerMenu.myGuilds)
        self.root.add_widget(GuildBannerMenu.people)
        self.root.add_widget(scrollable_grid)

    # def submit(self, instance):
    #     search = self.search_input.text
    #     # Here, you can process the submitted weight and height as needed
    #     # For example, you can print them to the console
    #     print(f"Stuff from search bar: {search}")

# class BoardDimension(Screen):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#
#


if __name__ == '__main__':
    HomeScreen().run()
