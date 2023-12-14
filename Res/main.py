import self as self
from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.bubble import Bubble, BubbleButton
from kivy.uix.dropdown import DropDown
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.togglebutton import ToggleButton

import SignIn
from Res import NEWTESTER, bubble


class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        welcome_label = Label(
            text="Welcome to BetterGUIlds",
            font_size=77,
            pos_hint={'center_x': 0.5, 'center_y': 0.7}
        )

        start_button = Button(
            text="Start",
            size_hint=(None, None),
            size=(100, 80),
            pos_hint={'center_x': 0.5, 'y': 0.1},
            on_press=self.on_start_button_click
        )

        self.add_widget(welcome_label)
        self.add_widget(start_button)

    def on_start_button_click(self, instance):
        self.manager.current = "introduction_of_the_app"


class BubbleScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        bubble1_text_label = Label(
            text='Guilds are a place for like-minded\npeople to come together.',
            font_size=40,
            pos_hint={'center_x': 0.3, 'center_y': 0.8}
        )

        bubble2_text_label = Label(
            text='Make posts, send messages, and\nparticipate in guild events!\nAn active guild is a thriving.',
            font_size=40,
            pos_hint={'center_x': 0.7, 'center_y': 0.56}
        )

        bubble3_text_label = Label(
            text='Guild space is limited!\nMaximum size of a guild is 25 members!\nFight for your place in the '
                 'guild!\nNobody likes a spectator!',
            font_size=40,
            pos_hint={'center_x': 0.45, 'center_y': 0.3}
        )

        continue_button = Button(
            text="I'm ready to use BetterGUIlds now!",
            size_hint=(None, None),
            size=(580, 80),
            pos_hint={'center_x': 0.70, 'y': 0.12},
            on_press=self.on_continue_button_click
        )

        exit_button = Button(
            text="I'm not interested",
            size_hint=(None, None),
            size=(280, 80),
            pos_hint={'center_x': 0.20, 'y': 0.12},
            on_press=self.on_exit_button_click
        )

        self.add_widget(bubble1_text_label)
        self.add_widget(bubble2_text_label)
        self.add_widget(bubble3_text_label)
        self.add_widget(continue_button)
        self.add_widget(exit_button)

    def on_continue_button_click(self, instance):
        self.manager.current = "new_or_returning_window"

    def on_exit_button_click(self, instance):
        self.manager.current = ""


class NewOrReturningWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        newOrReturning_label = Label(
            text="Are you a new or returning user?",
            font_size=50,
            pos_hint={'center_x': 0.5, 'center_y': 0.7}
        )

        new_button = Button(
            text="I am new",
            size_hint=(None, None),
            size=(300, 100),
            pos_hint={'center_x': 0.80, 'y': 0.20},
            on_press=self.on_new_button_click
        )

        returning_button = Button(
            text="I am a returning user",
            size_hint=(None, None),
            size=(300, 100),
            pos_hint={'center_x': 0.20, 'y': 0.20},
            on_press=self.on_returning_button_click
        )

        self.add_widget(newOrReturning_label)
        self.add_widget(new_button)
        self.add_widget(returning_button)

    def on_new_button_click(self, instance):
        self.manager.current = "create_an_acc_window"

    def on_returning_button_click(self, instance):
        self.manager.current = "sign_in_window"


class SignInWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        create_label = Label(
            text="Sign in with your BetterGuild Account",
            font_size=50,
            pos_hint={'center_x': 0.5, 'center_y': 0.8}
        )

        done_button = Button(
            text="Login with this username and password",
            size_hint=(None, None),
            size=(550, 65),
            pos_hint={'center_x': 0.5, 'y': 0.1},
            on_press=self.on_done_button_click
        )

        username_text_label = Label(
            text='Your Username',
            font_size=50,
            pos_hint={'center_x': 0.3, 'center_y': 0.7}
        )

        # Use a TextInput for entering the description
        self.moreUN_text_input = TextInput(
            hint_text='Type here',
            size_hint=(None, None),
            size=(600, 65),
            pos_hint={'center_x': 0.7, 'center_y': 0.7}
        )

        password_text_label = Label(
            text='Your Password',
            font_size=50,
            pos_hint={'center_x': 0.3, 'center_y': 0.5}
        )

        # Use a TextInput for entering the description
        self.morePW_text_input = TextInput(
            hint_text='Type here',
            size_hint=(None, None),
            size=(600, 65),
            pos_hint={'center_x': 0.7, 'center_y': 0.5}
        )

        reenter_password_text_label = Label(
            text='Re-enter Your Password',
            font_size=50,
            pos_hint={'center_x': 0.3, 'center_y': 0.3}
        )

        # Use a TextInput for entering the description
        self.moreRP_text_input = TextInput(
            hint_text='Type here',
            size_hint=(None, None),
            size=(600, 65),
            pos_hint={'center_x': 0.7, 'center_y': 0.3}
        )

        self.add_widget(create_label)
        self.add_widget(username_text_label)
        self.add_widget(self.moreUN_text_input)
        self.add_widget(password_text_label)
        self.add_widget(self.morePW_text_input)
        self.add_widget(reenter_password_text_label)
        self.add_widget(self.moreRP_text_input)
        self.add_widget(done_button)

    def on_done_button_click(self, instance):
        self.manager.current = "home_screen"


class CreateAnAccWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        create_label = Label(
            text="Create an Account",
            font_size=60,
            pos_hint={'center_x': 0.5, 'center_y': 0.8}
        )

        done_button = Button(
            text="Done and create an account now",
            size_hint=(None, None),
            size=(480, 80),
            pos_hint={'center_x': 0.5, 'y': 0.1},
            on_press=self.on_done_button_click
        )

        username_text_label = Label(
            text='Create Your Username',
            font_size=60,
            pos_hint={'center_x': 0.3, 'center_y': 0.7}
        )

        # Use a TextInput for entering the description
        self.moreUN_text_input = TextInput(
            hint_text='Type here',
            size_hint=(None, None),
            size=(600, 80),
            pos_hint={'center_x': 0.7, 'center_y': 0.7}
        )

        password_text_label = Label(
            text='Create Your Password',
            font_size=60,
            pos_hint={'center_x': 0.3, 'center_y': 0.5}
        )

        # Use a TextInput for entering the description
        self.morePW_text_input = TextInput(
            hint_text='Type here',
            size_hint=(None, None),
            size=(600, 80),
            pos_hint={'center_x': 0.7, 'center_y': 0.5}
        )

        reenter_password_text_label = Label(
            text='Re-enter Your Password',
            font_size=60,
            pos_hint={'center_x': 0.3, 'center_y': 0.3}
        )

        # Use a TextInput for entering the description
        self.moreRP_text_input = TextInput(
            hint_text='Type here',
            size_hint=(None, None),
            size=(600, 80),
            pos_hint={'center_x': 0.7, 'center_y': 0.3}
        )

        self.add_widget(create_label)
        self.add_widget(username_text_label)
        self.add_widget(self.moreUN_text_input)
        self.add_widget(password_text_label)
        self.add_widget(self.morePW_text_input)
        self.add_widget(reenter_password_text_label)
        self.add_widget(self.moreRP_text_input)
        self.add_widget(done_button)

    def on_done_button_click(self, instance):
        self.manager.current = "home_screen"


class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)

        self.add_widget(FloatLayout())

        search_input = TextInput(
            hint_text='Search for a guild...',
            font_size=60,
            size_hint=(None, None),
            size=(1740, 100),
            pos_hint={'x': 0.3, 'y': 0.95},
        )

        submit = Button(
            text="Search",
            font_size=60,
            size_hint=(None, None),
            size=(300, 100),
            pos_hint={'x': 0.8, 'y': 0.95},
        )

        class imageButtons():
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
                size_hint=(None, None),
                on_press=self.on_board_button_click
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
                font_size=100,
                size_hint=(None, None),
                size=(500, 200),
                pos_hint={'x': 0.0, 'y': 0.8},
                on_press=self.on_create_button_click
            )

            myGuilds = Button(
                text="My Guild",
                font_size=100,
                size_hint=(None, None),
                size=(500, 200),
                pos_hint={'x': 0.0, 'y': 0.7},
                on_press=self.on_guilds_button_click
            )
            people = Button(
                text="My People",
                font_size=100,
                size_hint=(None, None),
                size=(500, 200),
                pos_hint={'x': 0.0, 'y': 0.6},
                on_press=self.on_people_button_click
            )

        class ScrollableGrid(ScrollView):
            def __init__(self, **kwargs):
                super(ScrollableGrid, self).__init__(**kwargs)

                self.layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
                self.layout.bind(minimum_height=self.layout.setter('height'))

                self.layout.add_widget(imageButtons.PlankGuild)
                self.layout.add_widget(imageButtons.BoardgameButton)
                self.layout.add_widget(imageButtons.DummyGuild)

                for i in range(7):
                    button_text = f"Fake guild {i + 4}"
                    btn = Button(text=button_text, size=(2000, 500), size_hint=(None, None),
                                 background_normal='FakerGuild.png')
                    self.layout.add_widget(btn)

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
            )

        self.add_widget(search_input)
        self.add_widget(submit)
        self.add_widget(imageButtons.profileButton)
        self.add_widget(GuildBannerMenu.createGuild)
        self.add_widget(GuildBannerMenu.myGuilds)
        self.add_widget(GuildBannerMenu.people)
        self.add_widget(scrollable_grid)

    def on_board_button_click(self, instance):
        self.manager.current = "guild_screen"

    def on_create_button_click(self, instance):
        self.manager.current = "guild_screen"

    def on_guilds_button_click(self, instance):
        self.manager.current = "guild_screen"

    def on_people_button_click(self, instance):
        self.manager.current = "guild_screen"


class GuildScreen(Screen):
    def __init__(self, **kwargs):
        super(GuildScreen, self).__init__(**kwargs)

        self.title = 'GuildMenu'
        layout = FloatLayout()
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

        class ScrollableLabel(ScrollView):
            text = StringProperty('')

            def __init__(self, initial_text='', **kwargs):
                super(ScrollableLabel, self).__init__(**kwargs)
                self.label = Label(text=initial_text, color=(1, 0, 0, 1), font_size=(60), markup=True)
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
                initial_text1 = "Martin: Welcome to the chat!\nHaley: How is everyone doing today?.\nOscar: I'm doing good!"
                initial_text2 = "*You do not have permision to type in this channel*\n\nMartin: Welcome to the Announcments channel\nMartin: We are having a party at Micheals place on Friday"
                self.chat_history1 = ScrollableLabel(initial_text=initial_text1, size_hint=(.5, 0.5),
                                                     pos_hint={'x': 0.01, 'y': 0.3})
                self.chat_history2 = ScrollableLabel(initial_text=initial_text2, size_hint=(.5, 0.5),
                                                     pos_hint={'x': 0.01, 'y': 0.3})
                self.current_chat_history = self.chat_history1

                self.new_message = TextInput(pos_hint={'x': 0.0, 'y': 0.0}, width=Window.size[0] * 0.8,
                                             size_hint_x=None, height=Window.size[1] * 0.1,
                                             size_hint_y=None, multiline=True, hint_text='Type a message here...')
                self.send = Button(pos_hint={'x': 0.3, 'y': 0.0}, text="Send", size_hint_y=(.06), size_hint_x=(.1),
                                   height=self.new_message.height)
                self.send.bind(on_release=self.on_send_message)

                # Bind the on_text_validate event to the on_send_message function
                self.new_message.bind(on_text_validate=self.on_send_message)

                self.add_widget(self.chat_history1)
                self.add_widget(self.new_message)
                self.add_widget(self.send)

            def on_send_message(self, instance):
                if self.current_chat_history == self.chat_history1:
                    message = self.new_message.text
                    if message:
                        prefix = "*You*: "
                        self.chat_history1.update_text(f"{prefix}{message}")
                        self.new_message.text = ""

            def toggle_chat_version(self, instance):
                if self.current_chat_history == self.chat_history1:
                    self.remove_widget(self.chat_history1)
                    self.add_widget(self.chat_history2)
                    self.current_chat_history = self.chat_history2
                else:
                    self.remove_widget(self.chat_history2)
                    self.add_widget(self.chat_history1)
                    self.current_chat_history = self.chat_history1

        class ImageButtons:
            profile_button = Button(
                background_normal='UserProfileButton.png',
                pos_hint={'x': .9, 'y': 0.9},
                size_hint=(None, None)
            )

            toggle_button = ToggleButton(
                color=(1, 0, .65, 1),
                background_normal='ToggleButton1.png',
                background_down='ToggleButton2.png',
                size=(1200, 200),
                pos_hint={'x': .35, 'y': 0.8},
                size_hint=(None, None),
            )

            board_dimension_text_label = Label(
                text='Guild: Board Dimension',
                font_size=80,
                pos_hint={'center_x': 0.55, 'center_y': 0.75}
            )

            view_guild_members = Button(
                background_normal='DropdownMenuButton.png',
                size=(400, 100),
                size_hint=(None, None),
                pos_hint={'x': 0.8, 'y': 0.8}
            )

            @staticmethod
            def on_view_guild_members_press(instance):
                instance.background_color = (0, 1, 0, 1)  # Change the color when pressed

            @staticmethod
            def on_view_guild_members_release(instance):
                instance.background_color = (1, 1, 1, 1)  # Reset to the original color

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

        dropdown = DropDown()
        for index in range(10):
            btn = Button(text=f"User {index + 1}", size_hint_y=None, height=40)
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))
            dropdown.add_widget(btn)

        ImageButtons.view_guild_members.bind(on_press=ImageButtons().on_view_guild_members_press)
        ImageButtons.view_guild_members.bind(on_release=ImageButtons().on_view_guild_members_release)
        dropdown.bind(on_select=lambda instance, x: setattr(ImageButtons.view_guild_members, 'text', x))

        chat_screen = ChatPage(
            pos_hint={'x': 0.3, 'y': 0.0},
        )

        history = ScrollableLabel(
            pos_hint={'x': 0.5, 'y': 0.15},
            size_hint=(None, None),
            size=(Window.size[0], Window.size[1] * 0.3),
        )

        ImageButtons.toggle_button.bind(on_press=chat_screen.toggle_chat_version)

        layout.add_widget(search_input)
        layout.add_widget(submit)
        layout.add_widget(ImageButtons.profile_button)
        layout.add_widget(ImageButtons.toggle_button)
        layout.add_widget(ImageButtons.board_dimension_text_label)
        layout.add_widget(ImageButtons.view_guild_members)
        layout.add_widget(GuildBannerMenu.create_guild)
        layout.add_widget(GuildBannerMenu.my_guilds)
        layout.add_widget(GuildBannerMenu.people)
        layout.add_widget(chat_screen)

        self.add_widget(layout)


class MyApp(App):
    def build(self):
        screen_manager = ScreenManager()
        welcome_screen = WelcomeScreen(name="welcome")
        introduction_of_the_app = BubbleScreen(name="introduction_of_the_app")
        new_or_returning_window = NewOrReturningWindow(name="new_or_returning_window")
        sign_in_window = SignInWindow(name="sign_in_window")
        create_an_acc_window = CreateAnAccWindow(name="create_an_acc_window")
        home_screen = HomeScreen(name="home_screen")
        guild_menu = GuildScreen(name="guild_screen")

        screen_manager.add_widget(welcome_screen)
        screen_manager.add_widget(introduction_of_the_app)
        screen_manager.add_widget(new_or_returning_window)
        screen_manager.add_widget(sign_in_window)
        screen_manager.add_widget(create_an_acc_window)
        screen_manager.add_widget(home_screen)
        screen_manager.add_widget(guild_menu)

        return screen_manager


if __name__ == '__main__':
    MyApp().run()
