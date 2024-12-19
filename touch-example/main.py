"""
Example Kivy application.
"""
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget


class Touch(Widget):
    """Label that changes appearance when touched. """
    label = ObjectProperty(None)

    def on_touch_down(self, touch) -> None:
        """Change color to red when pressed. """
        self.label.color = (1, 0, 0, 1)

    def on_touch_up(self, touch):
        """Change color to green when unpressed. """
        self.label.color = (0, 1, 0, 1)


class MainApp(App):
    """Main application class. """
    def build(self) -> None:
        return Touch()


if __name__ == '__main__':
    MainApp().run()
