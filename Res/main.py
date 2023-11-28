import self as self
from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.bubble import Bubble, BubbleButton
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

import SignIn
from Res import NEWTESTER, bubble


class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        welcome_label = Label(
            text="Welcome to BetterGUIlds",
            font_size=35,
            pos_hint={'center_x': 0.5, 'center_y': 0.7}
        )

        start_button = Button(
            text="Start",
            size_hint=(None, None),
            size=(100, 50),
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
            font_size=35,
            pos_hint={'center_x': 0.3, 'center_y': 0.8}
        )

        bubble2_text_label = Label(
            text='Make posts, send messages, and\nparticipate in guild events!\nAn active guild is a thriving.',
            font_size=35,
            pos_hint={'center_x': 0.7, 'center_y': 0.56}
        )

        bubble3_text_label = Label(
            text='Guild space is limited!\nMaximum size of a guild is 25 members!\nFight for your place in the '
                 'guild!\nNobody likes a spectator!',
            font_size=35,
            pos_hint={'center_x': 0.45, 'center_y': 0.3}
        )

        continue_button = Button(
            text="I'm ready to use BetterGUIlds now!",
            size_hint=(None, None),
            size=(580, 50),
            pos_hint={'center_x': 0.70, 'y': 0.12},
            on_press=self.on_continue_button_click
        )

        exit_button = Button(
            text="I'm not interested",
            size_hint=(None, None),
            size=(280, 50),
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
            font_size=45,
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
            font_size=35,
            pos_hint={'center_x': 0.5, 'center_y': 0.8}
        )

        done_button = Button(
            text="Login with this username and password",
            size_hint=(None, None),
            size=(550, 50),
            pos_hint={'center_x': 0.5, 'y': 0.1},
            on_press=self.on_done_button_click
        )

        username_text_label = Label(
            text='Your Username',
            font_size=30,
            pos_hint={'center_x': 0.3, 'center_y': 0.7}
        )

        # Use a TextInput for entering the description
        self.moreUN_text_input = TextInput(
            hint_text='Type here',
            size_hint=(None, None),
            size=(600, 50),
            pos_hint={'center_x': 0.7, 'center_y': 0.7}
        )

        password_text_label = Label(
            text='Your Password',
            font_size=30,
            pos_hint={'center_x': 0.3, 'center_y': 0.5}
        )

        # Use a TextInput for entering the description
        self.morePW_text_input = TextInput(
            hint_text='Type here',
            size_hint=(None, None),
            size=(600, 50),
            pos_hint={'center_x': 0.7, 'center_y': 0.5}
        )

        reenter_password_text_label = Label(
            text='Re-enter Your Password',
            font_size=30,
            pos_hint={'center_x': 0.3, 'center_y': 0.3}
        )

        # Use a TextInput for entering the description
        self.moreRP_text_input = TextInput(
            hint_text='Type here',
            size_hint=(None, None),
            size=(600, 50),
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
            font_size=35,
            pos_hint={'center_x': 0.5, 'center_y': 0.8}
        )

        done_button = Button(
            text="Done and create an account now",
            size_hint=(None, None),
            size=(480, 50),
            pos_hint={'center_x': 0.5, 'y': 0.1},
            on_press=self.on_done_button_click
        )

        username_text_label = Label(
            text='Create Your Username',
            font_size=30,
            pos_hint={'center_x': 0.3, 'center_y': 0.7}
        )

        # Use a TextInput for entering the description
        self.moreUN_text_input = TextInput(
            hint_text='Type here',
            size_hint=(None, None),
            size=(600, 50),
            pos_hint={'center_x': 0.7, 'center_y': 0.7}
        )

        password_text_label = Label(
            text='Create Your Password',
            font_size=30,
            pos_hint={'center_x': 0.3, 'center_y': 0.5}
        )

        # Use a TextInput for entering the description
        self.morePW_text_input = TextInput(
            hint_text='Type here',
            size_hint=(None, None),
            size=(600, 50),
            pos_hint={'center_x': 0.7, 'center_y': 0.5}
        )

        reenter_password_text_label = Label(
            text='Re-enter Your Password',
            font_size=30,
            pos_hint={'center_x': 0.3, 'center_y': 0.3}
        )

        # Use a TextInput for entering the description
        self.moreRP_text_input = TextInput(
            hint_text='Type here',
            size_hint=(None, None),
            size=(600, 50),
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
        super().__init__(**kwargs)

        done_button = Button(
            text="Home",
            size_hint=(None, None),
            size=(500, 50),
            pos_hint={'center_x': 0.5, 'y': 0.1},
            on_press=self.on_done_button_click
        )

        self.add_widget(done_button)

    def on_done_button_click(self, instance):
        self.manager.current = NEWTESTER.HomeScreen().run()


class MyApp(App):
    def build(self):
        screen_manager = ScreenManager()
        welcome_screen = WelcomeScreen(name="welcome")
        introduction_of_the_app = BubbleScreen(name="introduction_of_the_app")
        new_or_returning_window = NewOrReturningWindow(name="new_or_returning_window")
        sign_in_window = SignInWindow(name="sign_in_window")
        create_an_acc_window = CreateAnAccWindow(name="create_an_acc_window")
        home_screen = HomeScreen(name="home_screen")

        screen_manager.add_widget(welcome_screen)
        screen_manager.add_widget(introduction_of_the_app)
        screen_manager.add_widget(new_or_returning_window)
        screen_manager.add_widget(sign_in_window)
        screen_manager.add_widget(create_an_acc_window)
        screen_manager.add_widget(home_screen)

        return screen_manager


if __name__ == '__main__':
    MyApp().run()
