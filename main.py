"""
Example Kivy application.
"""
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput


class AppGrid(GridLayout):
    """Main widget grid. """
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.cols = 2

        # name input
        self.add_widget(Label(text='First Name'))
        self.first_name = TextInput(multiline=False)
        self.add_widget(self.first_name)

        # name input
        self.add_widget(Label(text='Last Name'))
        self.last_name = TextInput(multiline=False)
        self.add_widget(self.last_name)

        # email input
        self.add_widget(Label(text='Email'))
        self.email = TextInput(multiline=False)
        self.add_widget(self.email)


class MainApp(App):
    """Main application class. """
    def build(self) -> None:
        return AppGrid()


if __name__ == '__main__':
    MainApp().run()
