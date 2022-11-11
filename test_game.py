import random
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


from bulls import get_dict_words
dict_words = get_dict_words()



class Bulls(App):
    def build(self):
        self.window = GridLayout()  # Создаем окно
        self.window.cols = 1  # количество столбцов

        self.word_text = Label(
            text="Введите количество букв в слове",   ### Текст
            font_size=48
        )
        self.window.add_widget(self.word_text)

        self.insert_num_letter = TextInput(            # поле ввода
            size_hint=(None, None),
            size=(50, 50),
            multiline=False,                      ###в одну строку
            padding=10                            # отступ курсора
        )

        self.window.add_widget(self.insert_num_letter)

        self.button = Button(
           text="Введите количество букв в слове",            #делаем кнопку
           size_hint = (1, 0.3)
            #background_color = ""
            #background_normal = ""
        )
        self.button.bind(on_press=self.insert_num)             #присваеваем фуекцию для кнопки
        self.window.add_widget(self.button)

        ########################################


        ############################################




        return self.window
    def insert_num(self, instance):       # формируем слово по длине со текстового поля
        num = int(self.insert_num_letter.text)
        word = random.choice(dict_words[num])
        slovo = '* '*len(word)
        self.word_text.text = word




if __name__ == '__main__':
    Bulls().run()


