#DO NOT LINK THIS PAGE, I PUT IN HERE BY ACCIDENT

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = GridLayout(cols=2, row_force_default=True, row_default_height=60, spacing=10, padding=30)
        # Use a Label for the description

        search_input = TextInput(
            hint_text='Search for a guild...',
            size_hint = (None, None),
            size = (950, 50),
            pos_hint={'center_x': 0.4, 'center_y': 0.975}
        )


        submit = Button(
            text="Search",
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={'center_x': 0.7, 'y': 0.95},
            on_press=self.submit
        )
        class GuildBannerMenu():
            createGuild = Button(
            text="+ Guild",
            size_hint=(None, None),
            size=(300, 100),
            pos_hint={'center_x': 0.1, 'y': 0.8},
            on_press=self.submit
            )
            
            myGuilds = Button(
            text="My Guild",
            size_hint=(None, None),
            size=(300, 100),
            pos_hint={'center_x': 0.1, 'y': 0.7},
            on_press=self.submit
        )
            people = Button(
            text="My People",
            size_hint=(None, None),
            size=(300, 100),
            pos_hint={'center_x': 0.1, 'y': 0.6},
            on_press=self.submit
        )
        
        class GuildScrolling():

            guilds = GridLayout(cols=1, spacing=10, size_hint_y=None)

            for i in range(100):
                btn = Button(text=str(i), size_hint_y=None, height=40)
                guilds.add_widget(btn)

            ScrollingGuilds = ScrollView(
            size_hint=(1, None),
            size=(500, 500),

            do_scroll_x = False)

            ScrollingGuilds.add_widget(guilds)


        


        #image stuff seems not to work anymore?
        #guildHolder = Image(source ="GALAXYBRAINS.png")



        #self.add_widget(guildHolder)

        # guildScroll = ScrollView(
        #     do_scroll_y: True

        # )

        self.add_widget(search_input)
        self.add_widget(submit)
        self.add_widget(GuildBannerMenu.createGuild)
        self.add_widget(GuildBannerMenu.myGuilds)
        self.add_widget(GuildBannerMenu.people)
        self.add_widget(GuildScrolling.ScrollingGuilds)

        # # Use a Label for the description
        # more_text_label = Label(
        #     text='Explain how your day is going:',
        #     font_size=24,
        #     pos_hint={'center_x': 0.5, 'center_y': 0.7}
        # )

        # Use a TextInput for entering the description
        # self.more_text_input = TextInput(
        #     hint_text='Type here',
        #     size_hint=(None, None),
        #     size=(600, 200),
        #     pos_hint={'center_x': 0.5, 'center_y': 0.5}
        # )

        next_button = Button(
            text="Next",
            size_hint=(None, None),
            size=(100, 50),
            pos_hint={'center_x': 0.90, 'y': 0.05},
            on_press=self.on_next_button_click
        )
        back_button = Button(
            text="Back",
            size_hint=(None, None),
            size=(100, 50),
            pos_hint={'center_x': 0.10, 'y': 0.05},
            on_press=self.on_back_button_click
        )


        class ScrollableLabel(ScrollView):
            text = StringProperty('')



        self.add_widget(back_button)
        self.add_widget(next_button)
        # self.add_widget(more_text_label)
        # self.add_widget(self.more_text_input)
        self.add_widget(layout)
    def on_back_button_click(self, instance):
        self.manager.current = "image2"
    def on_next_button_click(self, instance):
        self.manager.current = "exit_window"

    def submit(self, instance):
        search = self.search_input.text
        # Here, you can process the submitted weight and height as needed
        # For example, you can print them to the console
        print(f"Stuff from search bar: {search}")


if __name__ == '__main__':
    SignUpApp().run()

