"""
This is a camera example based on the code in the official documentation:
`https://kivy.org/doc/stable/examples/gen__camera__main__py.html`.
"""
from kivy.app import App
from kivy.graphics.texture import Texture
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout


class CameraPanel(BoxLayout):
    """Camera-based panel for controlling streaming and screenshots. """
    camera = ObjectProperty(None)

    def _capture(self) -> None:
        """Get image from camera. """
        if self.image.texture is None:
            self.image.texture = Texture.create(
                size=self.camera.texture.size,
                colorfmt=self.camera.texture.colorfmt,
            )
        self.image.texture.blit_buffer(
            self.camera.texture.pixels,
            colorfmt=self.camera.texture.colorfmt,
            bufferfmt=self.camera.texture.bufferfmt
        )
        self.image.texture.flip_vertical()
        raw: bytes = self.camera.texture.pixels  # image data here


class MainApp(App):
    """Main application class. """
    def build(self) -> None:
        return CameraPanel()


if __name__ == '__main__':
    MainApp().run()
