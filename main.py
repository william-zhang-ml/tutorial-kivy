"""
Example Kivy application.
"""
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput


class InputGrid(GridLayout):
    """Grid for form inputs. """
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


class AppGrid(GridLayout):
    """Main widget grid. """
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.cols = 1
        self.inputs = InputGrid()
        self.add_widget(self.inputs)
        self.submit = Button(text='Submit', font_size=40)
        self.submit.bind(on_press=self._pressed_button_handler)
        self.add_widget(self.submit)

    def _pressed_button_handler(self, instance: Button) -> None:
        first = self.inputs.first_name
        last = self.inputs.last_name
        email = self.inputs.email
        self.inputs.first_name.text = ''
        self.inputs.last_name.text = ''
        self.inputs.email.text = ''


class MainApp(App):
    """Main application class. """
    def build(self) -> None:
        return AppGrid()


if __name__ == '__main__':
    MainApp().run()
