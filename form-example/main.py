"""
Example Kivy application.
"""
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout


class InputGrid(GridLayout):
    """Grid for form inputs. """
    first_name = ObjectProperty(None)
    last_name = ObjectProperty(None)
    email = ObjectProperty(None)


class AppGrid(GridLayout):
    """Main widget grid. """
    inputs = ObjectProperty(None)

    def _pressed_button_handler(self) -> None:
        """Print form info and clear form. """
        first = self.inputs.first_name.text
        last = self.inputs.last_name.text
        email = self.inputs.email.text
        self.inputs.first_name.text = ''
        self.inputs.last_name.text = ''
        self.inputs.email.text = ''
        print(first, last, email)


class MainApp(App):
    """Main application class. """
    def build(self) -> None:
        return AppGrid()


if __name__ == '__main__':
    MainApp().run()
