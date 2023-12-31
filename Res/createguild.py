from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image


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
                               pos_hint={'center_x': 0.5, 'y': 0.20}, font_size='25sp')
        submit_button.bind(on_press=self.show_popup)
        layout.add_widget(submit_button)

        # Back Button
        back_button = Button(text='Back', size_hint=(None, None), size=(300, 100),
                               pos_hint={'center_x': 0.1, 'y': 0.8}, font_size='25sp')
        submit_button.bind(on_press=self.go_back)
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

    def go_back(self, instance):
        # put stuff here Skye
        x = 5

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
        # Handle publishing the guild details (currently just prints to console)
        print("Publishing guild details")


class MyApp(App):
    def build(self):
        return CreateGuild()


if __name__ == '__main__':
    MyApp().run()