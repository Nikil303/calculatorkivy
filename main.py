from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

# for the calculator windoe size
Window.size = (500, 700)

Builder.load_file('main.kv')


class MyLayout(Widget):
    def clear(self):
        self.ids.input1.text = '0'

    #button pressing function
    def button_press(self, button):
        #variable to store value that we entered
        number = self.ids.input1.text

        if number == "0":
            self.ids.input1.text = ''
            self.ids.input1.text = f'{button}'

        else:
            self.ids.input1.text = f'{number}{button}'

    def dot(self):
        number = self.ids.input1.text
        num_list = number.split("+")

        if '+' in number and "." not in num_list[-1]:
            number = f'{number}.'
            self.ids.input1.text = number

        elif '.' in number:
            pass
        else:
            number = f'{number}.'
            self.ids.input1.text = number

    def airthmetic_symbol(self, sign):
        number = self.ids.input1.text
        self.ids.input1.text = f'{number}{sign}'

    def clear(self):
         self.ids.input1.text = '0'

    def remove_last_digit(self):
        number = self.ids.input1.text
        number = number[:-1]
        self.ids.input1.text = number

    def equal(self):
        number = self.ids.input1.text
        answer = eval(number)
        self.ids.input1.text = str(answer)


class calculatorapp(App):
    def build(self):
        self.icon="images.png"
        return MyLayout()

if __name__ == '__main__':
    calculatorapp().run()
