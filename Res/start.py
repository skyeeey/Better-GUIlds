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
        self.manager.current = "new_or_returning_window"


class NewOrReturningWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        newOrReturning_label = Label(
            text="Are you a new or returning user?",
            font_size=45,
            pos_hint={'center_x': 0.5, 'center_y': 0.7}
        )

        new_button = Button(
            text="I am new.",
            size_hint=(None, None),
            size=(300, 100),
            pos_hint={'center_x': 0.80, 'y': 0.20},
            on_press=self.on_new_button_click
        )

        returning_button = Button(
            text="I am a returning user.",
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
        self.manager.current = SignIn.SignUpApp().run()


class SignUpApp(App):
    def build(self):
        self.title = 'Sign In!'
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        Window.hide()
        Window.clearcolor = (1, 1, 1, 1)

        # Create a title label with an image
        title_layout = BoxLayout(spacing=10)
        title_label = Label(text='Sign Into Your BetterGUIlds Account!', font_size='50sp', color=(0, 0, 0, 1))
        title_image = Image(source='account.png')  # Replace with the actual image path
        title_layout.add_widget(title_label)
        title_layout.add_widget(title_image)

        # Create a GridLayout for input fields and sign-up button
        input_layout = GridLayout(cols=1, spacing=10, size_hint_y=None, height=160)

        # Create input widgets
        username_input = TextInput(hint_text='Username', size_hint_y=400, height=200, multiline=False, font_size='20sp')
        password_input = TextInput(hint_text='Password', password=True, size_hint_y=400, height=200, multiline=False,
                                   font_size='20sp')

        # Set text color to black for input fields
        username_input.foreground_color = (0, 0, 0, 1)
        password_input.foreground_color = (0, 0, 0, 1)

        # Add input widgets to the GridLayout
        input_layout.add_widget(username_input)
        input_layout.add_widget(password_input)

        # Define the sign-up button behavior
        def sign_up_button_callback(instance):
            username = username_input.text
            password = password_input.text
            message_label.text = f'Signing in with: Username: {username} and entered password'
            sign_up_button.bind(on_press="home_screen")

        # RGB values for CornflowerBlue (#6495ED)
        cornflower_blue_rgb = (100 / 255.0, 149 / 255.0, 237 / 255.0, 1.0)

        # Create sign-up button
        sign_up_button = Button(text='Sign Into Your BetterGUIlds Account', size_hint_y=None, height=40,
                                on_press=sign_up_button_callback, font_size='17sp')
        sign_up_button.background_color = cornflower_blue_rgb
        sign_up_button.color = (1, 1, 1, 1)  # Set text color to white

        # Create a label to display messages
        message_label = Label(text='', size_hint_y=None, height=40, color=(0, 0, 0, 1))

        # Add widgets to the main layout
        layout.add_widget(title_layout)
        layout.add_widget(input_layout)
        layout.add_widget(sign_up_button)
        layout.add_widget(message_label)

        return layout


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
        self.manager.current = "blank_screen"


# class BlankScreen(Screen):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#
#     bubble_button = Button(
#         text="start the application introduction",
#         size_hint=(None, None),
#         size=(550, 50),
#         pos_hint={'center_x': 0.5, 'y': 0.1},
#         on_press=self.on_bubble_button_click
#     )
#
#     def on_bubble_button_click(self, instance):
#         self.manager.current = Bubble.Myapp.run()
#

class Myapp(App):
    def build(self):
        # create float layout
        self.root = FloatLayout()
        Window.clearcolor = (0, 0, 0, 0)

        # add button to layout
        # button = Button(text = "Press here to read the rules of BetterGUIlds...",
        # on_press = self.show_bubble)

        # now add button to layout
        # self.root.add_widget(button)

        # return self.root

        bubble1 = Bubble(orientation="horizontal",
                         size_hint=(None, None),
                         size=(800, 350),
                         # pos_hint = {'center_x': 0.5, 'center_y': 0.5})
                         pos_hint={'x': 0.05, 'y': 0.8})

        bubble2 = Bubble(orientation="horizontal",
                         size_hint=(None, None),
                         size=(800, 350),
                         # pos_hint = {'center_x': 0.5, 'center_y': 0.9})
                         pos_hint={'x': 0.4, 'y': 0.45})

        bubble3 = Bubble(orientation="horizontal",
                         size_hint=(None, None),
                         size=(800, 350),
                         pos_hint={'center_x': 0.85, 'center_y': 0.1})

        # now add buttons to bubble (cut copy and paste)
        button1 = BubbleButton(text="1) Guilds are a place for like-minded\npeople to come together.", font_size='20sp')
        button2 = BubbleButton(
            text="2) Make posts, send messages, and\nparticipate in guild events!\nAn active guild is a thriving "
                 "guild :)",
            font_size='20sp')
        button3 = BubbleButton(
            text="3) Guild space is limited!\nMaximum size of a guild is 25 members!\nFight for your place in the "
                 "guild!\nNobody likes a spectator!",
            font_size='20sp')

        # button3 = BubbleButton(text = "Paste")

        # now add buttons to bubble
        bubble1.add_widget(button1)
        bubble2.add_widget(button2)
        bubble3.add_widget(button3)
        # bubble.add_widget(button3)

        # finally add bubble to root(float layout)
        self.root.add_widget(bubble1)
        self.root.add_widget(bubble2)
        self.root.add_widget(bubble3)


class HomeScreen(App):
    def build(self):
        self.title = 'Home Screen'
        self.root = FloatLayout()
        Window.clearcolor = (0, 0, 0, 0)
        # Use a Label for the description

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
            # on_press=self.submit
        )

        class imageButtons():
            # Make Sure Image is in directory
            profileButton = Button(
                background_normal='UserProfileButton.png',
                pos_hint={'x': .9, 'y': 0.9},
                size_hint=(None, None)
            )

            BoardgameButton = Button(
                color=(1, 0, .65, 1),
                background_normal='DummyGuild.png',
                size=(800, 200),
                size_hint=(None, None)
            )

            DummyGuild = Button(
                color=(1, 0, .65, 1),
                background_normal='ActualDummyGuild.png',
                size=(800, 200),
                size_hint=(None, None)
            )

            PlankGuild = Button(
                color=(1, 0, .65, 1),
                background_normal='PlankGuild.png',
                size=(800, 200),
                size_hint=(None, None)
            )

        class GuildBannerMenu():
            createGuild = Button(
                text="+ Guild",
                size_hint=(None, None),
                size=(300, 100),
                pos_hint={'x': 0.0, 'y': 0.8},
                # on_press=self.submit
            )

            myGuilds = Button(
                text="My Guild",
                size_hint=(None, None),
                size=(300, 100),
                pos_hint={'x': 0.0, 'y': 0.7},
                # on_press=self.submit
            )
            people = Button(
                text="My People",
                size_hint=(None, None),
                size=(300, 100),
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
                    btn = Button(text=button_text, size=(800, 200), size_hint=(None, None))
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
                # on_press=self.submit
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


class ChatScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class MyApp(App):
    def build(self):
        screen_manager = ScreenManager()
        welcome_screen = WelcomeScreen(name="welcome")
        new_or_returning_window = NewOrReturningWindow(name="new_or_returning_window")
        create_an_acc_window = CreateAnAccWindow(name="create_an_acc_window")
        # blank_screen = BlankScreen(name="blank_screen")

        screen_manager.add_widget(welcome_screen)
        screen_manager.add_widget(new_or_returning_window)
        screen_manager.add_widget(create_an_acc_window)
        # screen_manager.add_widget(blank_screen)

        return screen_manager


if __name__ == '__main__':
    MyApp().run()
