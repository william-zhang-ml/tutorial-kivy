"""
Example Kivy application.
"""
from kivy.app import App
from kivy.uix.label import Label


class MainApp(App):
    """Main application class. """
    def build(self) -> None:
        return Label(text='I am a label.')


if __name__ == '__main__':
    MainApp().run()
