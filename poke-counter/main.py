"""
Poke counter application.
This app shows the number of times the user has poked it.
"""
import time
from kivy.app import App
from kivy.properties import NumericProperty, ObjectProperty
from kivy.uix.widget import Widget


class Counter(Widget):
    """Counter/label that increments when touched. """
    label = ObjectProperty(None)
    count = NumericProperty(0)

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.label.text = str(self.count)

    def on_touch_down(self, touch) -> None:
        """Change color to red when pressed. """
        self.count += 1
        self.label.text = str(self.count)


class MainApp(App):
    """Main application class. """
    def build(self) -> None:
        time.sleep(0.5)  # delay for presplash screen
        return Counter()


if __name__ == '__main__':
    MainApp().run()
