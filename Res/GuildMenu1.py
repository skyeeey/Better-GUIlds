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


class GuildScreen(App):
    def build(self):
        self.title = 'GuildMenu'
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

            ToggleButton = ToggleButton(
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

            ChatButton = Button(
                background_normal='FakeDiscord.png',
                pos_hint={'x': 0.3, 'y': 0.3},
                size_hint=(0.65, 0.4)
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

        # create a big main button
        ViewGuildMembers = Button(
            background_normal='DropdownMenuButton.png',
            size=(400, 100),
            size_hint=(None, None),
            pos_hint={'x': 0.8, 'y': 0.8}
        )

        dropdown = DropDown()
        for index in range(10):
            # Adding button in drop down list
            btn = Button(text=f"User {index + 1}", size_hint_y=None, height=40)

            # binding the button to show the text when selected
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))

            # then add the button inside the dropdown
            dropdown.add_widget(btn)

        # show the dropdown menu when the main button is released
        # note: all the bind() calls pass the instance of the caller 
        # (here, the mainbutton instance) as the first argument of the callback
        # (here, dropdown.open.).
        ViewGuildMembers.bind(on_release=dropdown.open)

        # one last thing, listen for the selection in the 
        # dropdown list and assign the data to the button text.
        dropdown.bind(on_select=lambda instance, x: setattr(ViewGuildMembers, 'text', x))

        class ScrollableLabel(ScrollView):

            def __init__(self, **kwargs):
                super().__init__(**kwargs)

                # ScrollView does not allow us to add more than one widget, so we need to trick it
                # by creating a layout and placing two widgets inside it
                # Layout is going to have one collumn and and size_hint_y set to None,
                # so height wo't default to any size (we are going to set it on our own)
                self.layout = GridLayout(cols=1, size_hint_y=None)
                self.add_widget(self.layout)

                # Now we need two widgets - Label for chat history and 'artificial' widget below
                # so we can scroll to it every new message and keep new messages visible
                # We want to enable markup, so we can set colors for example
                self.chat_history = Label(size_hint_y=None, markup=True)
                self.scroll_to_point = Label()

                # We add them to our layout
                self.layout.add_widget(self.chat_history)
                self.layout.add_widget(self.scroll_to_point)

            # Method called externally to add new message to the chat history
            def update_chat_history(self, message):
                # First add new line and message itself
                self.chat_history.text += '\n' + message

                # Set layout height to whatever height of chat history text is + 15 pixels
                # (adds a bit of space at teh bottom)
                # Set chat history label to whatever height of chat history text is
                # Set width of chat history text to 98 of the label width (adds small margins)
                self.layout.height = self.chat_history.texture_size[1] + 15
                self.chat_history.height = self.chat_history.texture_size[1]
                self.chat_history.text_size = (self.chat_history.width * 0.98, None)

                # As we are updating above, text height, so also label and layout height are going to be bigger
                # than the area we have for this widget. ScrollView is going to add a scroll, but won't
                # scroll to the botton, nor is there a method that can do that.
                # That's why we want additional, empty widget below whole text - just to be able to scroll to it,
                # so scroll to the bottom of the layout
                self.scroll_to(self.scroll_to_point)

        class ChatPage(GridLayout):
            def __init__(self, **kwargs):
                super().__init__(**kwargs)

                # We are going to use 1 column and 2 rows
                self.cols = 1
                self.rows = 2

                # First row is going to be occupied by our scrollable label
                # We want it be take 90% of app height
                self.history = ScrollableLabel(height=Window.size[1] * 0.5, size_hint_y=None,
                                               width=Window.size[0] * 0.5, size_hint_x=None)
                self.add_widget(self.history)

                # In the second row, we want to have input fields and Send button
                # Input field should take 80% of window width
                # We also want to bind button click to send_message method
                self.new_message = TextInput(width=Window.size[0] * 0.8, size_hint_x=None, height=Window.size[1] * .2,
                                             size_hint_y=None, multiline=False)
                self.send = Button(text="Send")
                self.send.bind(on_press=self.send_message)

                # To be able to add 2 widgets into a layout with just one collumn, we use additional layout,
                # add widgets there, then add this layout to main layout as second row
                bottom_line = GridLayout(cols=2)
                bottom_line.add_widget(self.new_message)
                bottom_line.add_widget(self.send)
                self.add_widget(bottom_line)

            # Gets called when either Send button or Enter key is being pressed
            # (kivy passes button object here as well, but we don;t care about it)
            def send_message(self, _):
                print("send a message!!!")

        ChatScreen = ChatPage(
            pos_hint={'x': 0.3, 'y': -0.1},
        )
        History = ScrollableLabel(
            pos_hint={'x': 0.3, 'y': .5},
        )

        self.root.add_widget(search_input)
        self.root.add_widget(submit)
        self.root.add_widget(imageButtons.profileButton)
        self.root.add_widget(imageButtons.ToggleButton)
        self.root.add_widget(imageButtons.board_dimension_text_label)
        self.root.add_widget(imageButtons.ChatButton)
        self.root.add_widget(GuildBannerMenu.createGuild)
        self.root.add_widget(GuildBannerMenu.myGuilds)
        self.root.add_widget(GuildBannerMenu.people)
        self.root.add_widget(ViewGuildMembers)
        self.root.add_widget(ChatScreen)
        self.root.add_widget(History)

    # def submit(self, instance):
    #     search = self.search_input.text
    #     # Here, you can process the submitted weight and height as needed
    #     # For example, you can print them to the console
    #     print(f"Stuff from search bar: {search}")


if __name__ == '__main__':
    GuildScreen().run()
