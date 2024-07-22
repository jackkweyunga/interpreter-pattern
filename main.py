"""
Measurement Convertor

This is the main file that runs the application.

It creates a window with a text input field and a button.
The user can enter a question in the text field and click the button to get the answer.

The question should be in the format: "quantity from_conversion to to_conversion"
For example: "1 gallon to pints"

"""
from kivy.app import App

# set window size
from kivy.config import Config
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout

from context import ConversionContext
from expression import Expression

Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '220')


class MeasurementConvertor(BoxLayout):

    def convert(self, question):
        self.ids.response.text = ""
        cc = ConversionContext(question)
        expression_class = getattr(__import__('measurements'), cc.get_from_conversion())
        obj: Expression = expression_class()
        method = getattr(obj, cc.get_to_conversion())
        result = method(cc.get_quantity())
        response = cc.get_response() + " " + result + " " + cc.get_to_conversion()
        self.ids.response.text = response


class MainApp(App):
    title = "Measurement Convertor"

    def build(self):
        return MeasurementConvertor()


if __name__ == "__main__":
    MainApp().run()
