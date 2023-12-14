from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.bubble import Bubble, BubbleButton
from kivy.uix.dropdown import DropDown
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.togglebutton import ToggleButton

import SignIn



class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        welcome_label = Label(
            text="Welcome to BetterGUIlds",
            font_size=125,
            pos_hint={'center_x': 0.5, 'center_y': 0.7}
        )

        start_button = Button(
            text="Start",
            font_size=75,
            size_hint=(0.15, 0.12),
            size=(50, 20),
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
            font_size=75,
            pos_hint={'center_x': 0.28, 'center_y': 0.8}
        )

        bubble2_text_label = Label(
            text='Make posts, send messages, and\nparticipate in guild events!\nAn active guild is a thriving.',
            font_size=75,
            pos_hint={'center_x': 0.7, 'center_y': 0.56}
        )

        bubble3_text_label = Label(
            text='Guild space is limited!\nMaximum size of a guild is 25 members!\nFight for your place in the '
                 'guild!\nNobody likes a spectator!',
            font_size=75,
            pos_hint={'center_x': 0.45, 'center_y': 0.3}
        )

        continue_button = Button(
            text="I'm ready to use BetterGUIlds now!",
            font_size=66,
            size_hint=(0.39, 0.10),
            size=(3500, 80),
            pos_hint={'center_x': 0.75, 'y': 0.05},
            on_press=self.on_continue_button_click
        )

        exit_button = Button(
            text="I'm not interested",
            font_size=66,
            size_hint=(0.25, 0.10),
            size=(3500, 80),
            pos_hint={'center_x': 0.20, 'y': 0.05},
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
            font_size=100,
            pos_hint={'center_x': 0.5, 'center_y': 0.7}
        )

        new_button = Button(
            text="I am new",
            font_size=68,
            size_hint=(0.2, 0.10),
            size=(300, 100),
            pos_hint={'center_x': 0.80, 'y': 0.20},
            on_press=self.on_new_button_click
        )

        returning_button = Button(
            text="I am a returning user",
            font_size=68,
            size_hint=(0.25, 0.10),
            size=(420, 100),
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
            font_size=68,
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
            font_size=100,
            pos_hint={'center_x': 0.5, 'center_y': 0.85}
        )

        done_button = Button(
            text="Done and create an account now",
            font_size=68,
            size_hint=(0.35, 0.10),
            size=(600, 80),
            pos_hint={'center_x': 0.80, 'y': 0.1},
            on_press=self.on_done_button_click
        )

        back_button = Button(
            text="Back",
            font_size=68,
            size_hint=(0.20, 0.10),
            size=(480, 80),
            pos_hint={'center_x': 0.20, 'y': 0.1},
            on_press=self.on_back_button_click
        )

        username_text_label = Label(
            text='Create Your Username',
            font_size=68,
            pos_hint={'center_x': 0.3, 'center_y': 0.7}
        )

        # Use a TextInput for entering the description
        self.moreUN_text_input = TextInput(
            hint_text='Type here',
            font_size=60,
            size_hint=(None, None),
            size=(600, 80),
            pos_hint={'center_x': 0.7, 'center_y': 0.7}
        )

        password_text_label = Label(
            text='Create Your Password',
            font_size=68,
            pos_hint={'center_x': 0.3, 'center_y': 0.5}
        )

        # Use a TextInput for entering the description
        self.morePW_text_input = TextInput(
            hint_text='Type here',
            font_size=60,
            size_hint=(None, None),
            size=(600, 80),
            pos_hint={'center_x': 0.7, 'center_y': 0.5}
        )

        reenter_password_text_label = Label(
            text='Re-enter Your Password',
            font_size=68,
            pos_hint={'center_x': 0.3, 'center_y': 0.3}
        )

        # Use a TextInput for entering the description
        self.moreRP_text_input = TextInput(
            hint_text='Type here',
            size_hint=(None, None),
            font_size=60,
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
        self.add_widget(back_button)

    def on_done_button_click(self, instance):
        self.manager.current = "home_screen"

    def on_back_button_click(self, instance):
        self.manager.current = "new_or_returning_window"


class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)

        self.add_widget(FloatLayout())

        search_input = TextInput(
            hint_text='Search for a guild...',
            font_size=68,
            size_hint=(None, None),
            size=(1740, 100),
            pos_hint={'x': 0.3, 'y': 0.95},
        )

        submit = Button(
            text="Search",
            font_size=68,
            size_hint=(None, None),
            size=(300, 100),
            pos_hint={'x': 0.8, 'y': 0.95},
        )

        class imageButtons():
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
            home = Button(
                text="Home",
                font_size=100,
                size_hint=(None, None),
                size=(500, 200),
                pos_hint={'x': 0.001, 'y': 0.91},
                on_press=self.on_home_button_click
            )

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
        self.add_widget(GuildBannerMenu.home)
        self.add_widget(GuildBannerMenu.createGuild)
        self.add_widget(GuildBannerMenu.myGuilds)
        self.add_widget(GuildBannerMenu.people)
        self.add_widget(scrollable_grid)

    def on_home_button_click(self, instance):
        self.manager.current = "home_screen"

    def on_board_button_click(self, instance):
        self.manager.current = "rule_page"

    def on_create_button_click(self, instance):
        self.manager.current = "create_guild"

    def on_guilds_button_click(self, instance):
        self.manager.current = "myGuild"

    def on_people_button_click(self, instance):
        self.manager.current = "my_people_screen"


class RulePage(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        intro_label = Label(
            text="Introduction of Guild: Board Dimension",
            font_size=100,
            pos_hint={'center_x': 0.5, 'center_y': 0.7}
        )

        rules_label = Label(
            text="Rules:\n1) No Fighting\n2) No swearing\n3) No playing monopoly\n4) No eating chess pieces\n "
                 "**Rules for this application: members of each guild are up to 20. Expect sincere interests in participating in the guild.",
            font_size=50,
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )

        join_button = Button(
            text="Request to join",
            font_size=40,
            size_hint=(0.2, 0.10),
            size=(300, 100),
            pos_hint={'center_x': 0.80, 'y': 0.20},
            on_press=self.on_join_button_click
        )

        cancel_button = Button(
            text="Cancel",
            font_size=40,
            size_hint=(0.25, 0.10),
            size=(420, 100),
            pos_hint={'center_x': 0.20, 'y': 0.20},
            on_press=self.on_cancel_button_click
        )

        self.add_widget(intro_label)
        self.add_widget(rules_label)
        self.add_widget(join_button)
        self.add_widget(cancel_button)

    def on_join_button_click(self, instance):
        self.manager.current = "joined_screen"

    def on_cancel_button_click(self, instance):
        self.manager.current = "home_screen"


class JoinedScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        success_label = Label(
            text="Your request to join BOARD DIMENSION has been approved.",
            font_size=100,
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )

        continue_button = Button(
            text="continue to view this guild",
            font_size=40,
            size_hint=(0.2, 0.10),
            size=(300, 100),
            pos_hint={'center_x': 0.50, 'y': 0.20},
            on_press=self.on_continue_button_click
        )

        self.add_widget(success_label)
        self.add_widget(continue_button)

    def on_continue_button_click(self, instance):
        self.manager.current = "guild_screen"


class GuildScreen(Screen):
    def __init__(self, **kwargs):
        super(GuildScreen, self).__init__(**kwargs)

        self.title = 'GuildMenu'
        layout = FloatLayout()
        Window.clearcolor = (0, 0, 0, 0)

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
                initial_text2 = "Martin: Welcome to the chat!\nHaley: How is everyone doing today?.\nOscar: I'm doing good!"
                initial_text1 = "*You do not have permision to type in this channel*\n\nMartin: Welcome to the Announcments channel\nMartin: We are having a party at Micheals place on Friday"
                self.chat_history1 = ScrollableLabel(initial_text=initial_text1, size_hint=(.5, 0.5),
                                                     pos_hint={'x': 0.01, 'y': 0.3})
                self.chat_history2 = ScrollableLabel(initial_text=initial_text2, size_hint=(.5, 0.5),
                                                     pos_hint={'x': 0.01, 'y': 0.3})
                self.current_chat_history = self.chat_history1

                self.new_message = TextInput(pos_hint={'x': 0.0, 'y': 0.0}, width=Window.size[0] * 0.8,
                                             size_hint_x=None, height=Window.size[1] * 0.1,
                                             size_hint_y=None, multiline=True, hint_text='Type a message here...',
                                             font_size=60)
                self.send = Button(pos_hint={'x': 0.5, 'y': 0.0}, text="Send", font_size=60, size_hint_y=(.06),
                                   size_hint_x=(.1),
                                   height=self.new_message.height)
                self.send.bind(on_release=self.on_send_message)

                # Bind the on_text_validate event to the on_send_message function
                self.new_message.bind(on_text_validate=self.on_send_message)

                self.add_widget(self.chat_history1)
                self.add_widget(self.new_message)
                self.add_widget(self.send)

            def on_send_message(self, instance):
                if self.current_chat_history == self.chat_history2:
                    message = self.new_message.text
                    if message:
                        prefix = "*You*: "
                        self.chat_history2.update_text(f"{prefix}{message}")
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

            toggle_button = ToggleButton(
                color=(1, 0, .65, 1),
                background_normal='ToggleButton2.png',
                background_down='ToggleButton1.png',
                size=(1600, 300),
                pos_hint={'x': .25, 'y': 0.85},
                size_hint=(None, None),
            )

            board_dimension_text_label = Label(
                text='Guild: Board Dimension',
                font_size=80,
                pos_hint={'center_x': 0.50, 'center_y': 0.75}
            )

            view_guild_members = Button(
                background_normal='DropdownMenuButton.png',
                size=(450, 100),
                size_hint=(None, None),
                pos_hint={'x': 0.82, 'y': 0.8},
            )

            @staticmethod
            def on_view_guild_members_press(instance):
                instance.background_color = (0, 1, 0, 1)  # Change the color when pressed

            @staticmethod
            def on_view_guild_members_release(instance):
                instance.background_color = (1, 1, 1, 1)  # Reset to the original color

        class GuildBannerMenu:

            home = Button(
                text="Home",
                font_size=100,
                size_hint=(None, None),
                size=(500, 200),
                pos_hint={'x': 0.001, 'y': 0.91},
                on_press=self.on_home_button_click
            )

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

        dropdown = DropDown(pos_hint={'center_x': 0.9, 'center_y': 0.6})

        kathy = Button(
            text="Kathy",
            size_hint_y=None, height=40, size_hint_x=(0.1),
            on_press=self.on_kathy_button_click
        )

        martin = Button(
            text="Martin",
            size_hint_y=None, height=40, size_hint_x=(0.1),
        )

        oscar = Button(
            text="Oscar",
            size_hint_y=None, height=40, size_hint_x=(0.1),
        )

        kathy.bind(on_release=lambda btn: dropdown.select(btn.text))
        martin.bind(on_release=lambda btn: dropdown.select(btn.text))
        oscar.bind(on_release=lambda btn: dropdown.select(btn.text))
        dropdown.add_widget(kathy)
        dropdown.add_widget(martin)
        dropdown.add_widget(oscar)

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

        image_buttons_instance = ImageButtons()
        image_buttons_instance.view_guild_members.bind(on_press=image_buttons_instance.on_view_guild_members_press)
        image_buttons_instance.view_guild_members.bind(on_release=image_buttons_instance.on_view_guild_members_release)
        dropdown.bind(on_select=lambda instance, x: setattr(image_buttons_instance.view_guild_members, 'text', x))
        view_guild_members_button = image_buttons_instance.view_guild_members
        view_guild_members_button.bind(on_release=dropdown.open)
        layout.add_widget(view_guild_members_button)

        ImageButtons.toggle_button.bind(on_press=chat_screen.toggle_chat_version)

        layout.add_widget(ImageButtons.toggle_button)
        layout.add_widget(ImageButtons.board_dimension_text_label)
        self.add_widget(GuildBannerMenu.createGuild)
        self.add_widget(GuildBannerMenu.myGuilds)
        self.add_widget(GuildBannerMenu.home)
        layout.add_widget(GuildBannerMenu.people)
        layout.add_widget(chat_screen)

        self.add_widget(layout)

    def on_home_button_click(self, instance):
        self.manager.current = "home_screen"

    def on_kathy_button_click(self, instance):
        self.manager.current = "kathy"

    def on_create_button_click(self, instance):
        self.manager.current = "create_guild"

    def on_guilds_button_click(self, instance):
        self.manager.current = "myGuild"

    def on_people_button_click(self, instance):
        self.manager.current = "my_people_screen"


class MyPeopleScreen(Screen):

    def __init__(self, **kwargs):
        super(MyPeopleScreen, self).__init__(**kwargs)

        self.add_widget(FloatLayout())

        class GuildBannerMenu():
            home = Button(
                text="Home",
                font_size=100,
                size_hint=(None, None),
                size=(500, 200),
                pos_hint={'x': 0.001, 'y': 0.91},
                on_press=self.on_home_button_click
            )

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

        class MyPeoplePage():
            mypeople_text_label = Label(
                text='My people',
                font_size=100,
                pos_hint={'center_x': 0.50, 'center_y': 0.80}
            )

            online_text_label = Label(
                text='People ONLINE:',
                font_size=70,
                pos_hint={'center_x': 0.30, 'center_y': 0.65}
            )

            offline_text_label = Label(
                text='People OFFLINE:',
                font_size=70,
                pos_hint={'center_x': 0.30, 'center_y': 0.30}
            )

            kathy_text_label = Label(
                text='Kathy(same guild: board dimension)',
                font_size=50,
                pos_hint={'center_x': 0.42, 'center_y': 0.58}
            )

            chat_button = Button(
                text="Chat with Kathy",
                font_size=58,
                size_hint=(None, None),
                size=(500, 200),
                pos_hint={'x': 0.70, 'y': 0.58},
                on_press=self.on_chat_button_click
            )

        self.add_widget(GuildBannerMenu.home)
        self.add_widget(GuildBannerMenu.createGuild)
        self.add_widget(GuildBannerMenu.myGuilds)
        self.add_widget(GuildBannerMenu.people)
        self.add_widget(MyPeoplePage.chat_button)
        self.add_widget(MyPeoplePage.mypeople_text_label)
        self.add_widget(MyPeoplePage.kathy_text_label)
        self.add_widget(MyPeoplePage.online_text_label)
        self.add_widget(MyPeoplePage.offline_text_label)

    def on_chat_button_click(self, instance):
        self.manager.current = "kathy"

    def on_create_button_click(self, instance):
        self.manager.current = "create_guild"

    def on_guilds_button_click(self, instance):
        self.manager.current = "myGuild"

    def on_home_button_click(self, instance):
        self.manager.current = "home_screen"

    def on_people_button_click(self, instance):
        self.manager.current = "my_people_screen"


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
        initial_text = "*This is the beginning of your chat with Kathy*\n"
        self.chat_history = ScrollableLabel(initial_text=initial_text, font_size=60,
                                            pos_hint={'x': 0.01, 'y': 0.3})
        self.current_chat_history = self.chat_history

        self.new_message = TextInput(pos_hint={'x': 0.0, 'y': 0.1},
                                     multiline=True, hint_text='Type a message here...', font_size=60)
        self.send = Button(pos_hint={'x': 0.4, 'y': 0.1}, text="Send", font_size=60,
                           height=self.new_message.height)
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
        self.chat_history = ScrollableLabel(initial_text=initial_text, size_hint=(.4, 0.6),
                                            pos_hint={'x': 0.01, 'y': 0.3})
        self.current_chat_history = self.chat_history

        self.new_message = TextInput(pos_hint={'x': 0.0, 'y': 0.1},
                                     size_hint_x=(0.4),
                                     size_hint_y=(.06), multiline=True, hint_text='Type a message here...')
        self.send = Button(pos_hint={'x': 0.4, 'y': 0.1}, text="Send", size_hint_y=(.06), size_hint_x=(.1),
                           height=self.new_message.height)
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


class Kathy(Screen):
    def __init__(self, **kwargs):
        super(Kathy, self).__init__(**kwargs)

        self.title = 'GuildMenu'
        layout = FloatLayout()
        Window.clearcolor = (0, 0, 0, 0)

        self.kathy_text_label = Label(
            text='Chat with Kathy',
            font_size=100,
            pos_hint={'center_x': 0.5, 'center_y': 0.83}
        )

        self.guild_banner_menu = GridLayout(cols=1)
        self.home = Button(
            text="Home",
            font_size=100,
            size_hint=(None, None),
            size=(500, 200),
            pos_hint={'x': 0.001, 'y': 0.91},
            on_press=self.on_home_button_click
        )
        self.create_guild = Button(
            text="+ Guild",
            font_size=100,
            size_hint=(None, None),
            size=(500, 200),
            pos_hint={'x': 0.0, 'y': 0.8},
            on_press=self.on_create_button_click
        )
        self.my_guilds = Button(
            text="My Guild",
            font_size=100,
            size_hint=(None, None),
            size=(500, 200),
            pos_hint={'x': 0.0, 'y': 0.7},
            on_press=self.on_guilds_button_click
        )
        self.people = Button(
            text="My People",
            font_size=100,
            size_hint=(None, None),
            size=(500, 200),
            pos_hint={'x': 0.0, 'y': 0.6},
            on_press=self.on_people_button_click
        )
        self.guild_banner_menu.add_widget(self.home)
        self.guild_banner_menu.add_widget(self.create_guild)
        self.guild_banner_menu.add_widget(self.my_guilds)
        self.guild_banner_menu.add_widget(self.people)

        self.chat_screen = ChatPage(
            pos_hint={'x': 0.3, 'y': -0.1},
        )

        self.history = ScrollableLabel(
            pos_hint={'x': 0.3, 'y': .5},
        )

        layout.add_widget(self.kathy_text_label)
        layout.add_widget(self.guild_banner_menu)
        layout.add_widget(self.chat_screen)
        layout.add_widget(self.history)

        self.add_widget(layout)

    def on_home_button_click(self, instance):
        self.manager.current = "home_screen"

    def on_create_button_click(self, instance):
        self.manager.current = "create_guild"

    def on_guilds_button_click(self, instance):
        self.manager.current = "myGuild"

    def on_people_button_click(self, instance):
        self.manager.current = "my_people_screen"


class CreateGuild(Screen):
    def __init__(self, **kwargs):
        super(CreateGuild, self).__init__(**kwargs)

        layout = FloatLayout()

        # Title Label
        title_label = Label(text='Create a new guild!', size_hint=(None, None), size=(300, 50),
                            pos_hint={'center_x': 0.5, 'top': 0.95}, font_size='50sp')
        layout.add_widget(title_label)

        # Guild Title Input
        title1_label = Label(text='Guild Title:', size_hint=(None, None), size=(100, 50),
                             pos_hint={'center_x': 0.30, 'top': 0.84}, font_size='25sp')
        self.name_input = TextInput(hint_text='Type the title of your guild', multiline=False,
                                    size_hint=(None, None), size=(600, 100), pos_hint={'center_x': 0.5, 'top': 0.85},
                                    font_size='20sp')
        layout.add_widget(title1_label)
        layout.add_widget(self.name_input)

        # Guild Description Input
        desc_label = Label(text='Guild Description:', size_hint=(None, None), size=(100, 50),
                           pos_hint={'center_x': 0.30, 'top': 0.74}, font_size='25sp')
        self.desc_input = TextInput(hint_text='Type in a description of your guild', multiline=False,
                                    size_hint=(None, None), size=(600, 100), pos_hint={'center_x': 0.5, 'top': 0.75},
                                    font_size='16sp')
        layout.add_widget(desc_label)
        layout.add_widget(self.desc_input)

        # Guild Rules Input
        rules_label = Label(text='Guild Rules:', size_hint=(None, None), size=(100, 50),
                            pos_hint={'center_x': 0.30, 'top': 0.64}, font_size='25sp')
        self.rules_input = TextInput(hint_text='Type in the rules of your guild', multiline=False,
                                     size_hint=(None, None), size=(600, 100), pos_hint={'center_x': 0.5, 'top': 0.65},
                                     font_size='18sp')
        layout.add_widget(rules_label)
        layout.add_widget(self.rules_input)

        # Logo Dropdown
        logo_label = Label(text='Guild Logo:', size_hint=(None, None), size=(100, 50),
                           pos_hint={'center_x': 0.30, 'top': 0.54}, font_size='25sp')

        self.logo_dropdown = Spinner(
            text='Select a Guild Logo',
            values=('Flower', 'Cook', 'Robot', 'Rollerskates', 'Video Game'),
            size_hint=(None, None),
            size=(600, 100),
            pos_hint={'center_x': 0.5, 'top': 0.55},
            font_size='25sp'
        )
        self.logo_dropdown.bind(text=self.on_spinner_select)
        layout.add_widget(logo_label)
        layout.add_widget(self.logo_dropdown)

        # Image Widget for Guild Logo
        self.guild_logo_image = Image(source='', keep_ratio=True, allow_stretch=True,
                                      size_hint=(None, None), size=(300, 300), pos_hint={'center_x': 0.5, 'top': 0.45})
        layout.add_widget(self.guild_logo_image)

        # Publish Guild Button
        submit_button = Button(text='Confirm Guild Details', size_hint=(None, None), size=(600, 100),
                               pos_hint={'center_x': 0.5, 'y': 0.20}, font_size='25sp', on_press=self.show_popup)
        # submit_button.bind(on_press=self.show_popup)
        layout.add_widget(submit_button)

        # Back Button
        back_button = Button(text='Back', size_hint=(None, None), size=(300, 100),
                             pos_hint={'center_x': 0.1, 'y': 0.8}, font_size='25sp', on_press=self.go_back_click)
        # back_button.bind(on_press=self.go_back_click)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def on_spinner_select(self, spinner, text):
        # Set the source of the Image widget based on the selected value
        if text == 'Flower':
            self.guild_logo_image.source = 'flower.jpg'
        elif text == 'Cook':
            self.guild_logo_image.source = 'cook.jpg'
        elif text == "Robot":
            self.guild_logo_image.source = 'image1.jpg'
        elif text == "Rollerskates":
            self.guild_logo_image.source = 'rollerskates.jpg'
        elif text == "Video Game":
            self.guild_logo_image.source = 'videogame.jpg'

    def go_back_click(self, instance):
        self.manager.current = "home_screen"

    def show_popup(self, instance):
        content = BoxLayout(orientation='vertical')

        popup_label = Label(
            text=f"\n\nName: {self.name_input.text}\n\nDescription: {self.desc_input.text}\n\nRules: {self.rules_input.text}\n\nLogo: {self.logo_dropdown.text}",
            size_hint=(None, None), size=(600, 600))
        content.add_widget(popup_label)

        # Add some spacing
        content.add_widget(Label(size_hint_y=None, height=20))

        # Add 'Close' Button in Popup
        close_button = Button(text="Close", size_hint=(None, None), size=(100, 50),
                              pos_hint={'center_x': 0.12, 'y': 0.90})
        close_button.bind(on_press=self.reset_entries)
        content.add_widget(close_button)

        # Add 'Publish Guild' in Popup
        publish_button = Button(text="Publish Guild", size_hint=(None, None), size=(250, 50),
                                pos_hint={'center_x': 0.82, 'y': 0.10}, on_press=self.on_publish_button_click)
        content.add_widget(publish_button)

        popup = Popup(title="Guild Details", content=content, size_hint=(None, None), size=(900, 700))
        close_button.bind(on_press=popup.dismiss)
        popup.open()

    def reset_entries(self, instance):
        # Reset text inputs and spinner
        self.name_input.text = ''
        self.desc_input.text = ''
        self.rules_input.text = ''
        self.logo_dropdown.text = 'Select Guild Logo'
        self.guild_logo_image.source = ''

    def on_publish_button_click(self, instance):
        self.manager.current = "myGuild"


class MyGuild(Screen):
    def __init__(self, **kwargs):
        super(MyGuild, self).__init__(**kwargs)

        self.add_widget(FloatLayout())

        search_input = TextInput(
            hint_text='Search for a guild...',
            font_size=68,
            size_hint=(None, None),
            size=(1740, 100),
            pos_hint={'x': 0.3, 'y': 0.95},
        )

        submit = Button(
            text="Search",
            font_size=68,
            size_hint=(None, None),
            size=(300, 100),
            pos_hint={'x': 0.8, 'y': 0.95},
        )

        class imageButtons():
            BoardgameButton = Button(
                color=(1, 0, .65, 1),
                background_normal='DummyGuild.png',
                size=(2000, 500),
                size_hint=(None, None),
                on_press=self.on_board_button_click
            )

        class GuildBannerMenu():
            home = Button(
                text="Home",
                font_size=100,
                size_hint=(None, None),
                size=(500, 200),
                pos_hint={'x': 0.001, 'y': 0.91},
                on_press=self.on_home_button_click
            )

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

                self.layout.add_widget(imageButtons.BoardgameButton)

                for i in range(7):
                    button_text = f"Fake guild {i + 1}"
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
        self.add_widget(GuildBannerMenu.home)
        self.add_widget(GuildBannerMenu.createGuild)
        self.add_widget(GuildBannerMenu.myGuilds)
        self.add_widget(GuildBannerMenu.people)
        self.add_widget(scrollable_grid)

    def on_home_button_click(self, instance):
        self.manager.current = "home_screen"

    def on_board_button_click(self, instance):
        self.manager.current = "rule_page"

    def on_create_button_click(self, instance):
        self.manager.current = "create_guild"

    def on_guilds_button_click(self, instance):
        self.manager.current = "myGuild"

    def on_people_button_click(self, instance):
        self.manager.current = "my_people_screen"


class MyApp(App):
    def build(self):
        screen_manager = ScreenManager()
        welcome_screen = WelcomeScreen(name="welcome")
        introduction_of_the_app = BubbleScreen(name="introduction_of_the_app")
        new_or_returning_window = NewOrReturningWindow(name="new_or_returning_window")
        sign_in_window = SignInWindow(name="sign_in_window")
        create_an_acc_window = CreateAnAccWindow(name="create_an_acc_window")
        home_screen = HomeScreen(name="home_screen")
        rule_screen = RulePage(name="rule_page")
        joined_screen = JoinedScreen(name="joined_screen")
        guild_menu = GuildScreen(name="guild_screen")
        my_people_screen = MyPeopleScreen(name="my_people_screen")
        kathy = Kathy(name="kathy")
        createguild = CreateGuild(name="create_guild")
        myGuild = MyGuild(name="myGuild")

        screen_manager.add_widget(welcome_screen)
        screen_manager.add_widget(introduction_of_the_app)
        screen_manager.add_widget(new_or_returning_window)
        screen_manager.add_widget(sign_in_window)
        screen_manager.add_widget(create_an_acc_window)
        screen_manager.add_widget(home_screen)
        screen_manager.add_widget(rule_screen)
        screen_manager.add_widget(joined_screen)
        screen_manager.add_widget(guild_menu)
        screen_manager.add_widget(my_people_screen)
        screen_manager.add_widget(kathy)
        screen_manager.add_widget(createguild)
        screen_manager.add_widget(myGuild)

        return screen_manager


if __name__ == '__main__':
    MyApp().run()
