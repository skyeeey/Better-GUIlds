from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

class SignUpApp(App):
    def build(self):
        self.title = 'Sign In!'
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # Set the window background color to white
        Window.clearcolor = (1,1,1,1)

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
        password_input = TextInput(hint_text='Password', password=True, size_hint_y=400, height=200, multiline=False, font_size='20sp')

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

        # RGB values for CornflowerBlue (#6495ED)
        cornflower_blue_rgb = (100 / 255.0, 149 / 255.0, 237 / 255.0, 1.0)

        # Create sign-up button
        sign_up_button = Button(text='Sign Into Your BetterGUIlds Account', size_hint_y=None, height=40, on_press=sign_up_button_callback, font_size='17sp')
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

if __name__ == '__main__':
    SignUpApp().run()