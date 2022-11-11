import random
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from bulls import get_dict_words
dict_words = get_dict_words()

class ScreenOne():


    def __init__(self,word):
        super().__init__()
        self.word = word
        self.word = ""
        # boxlayout = BoxLayout(orientation="vertical")      #упорядочить по вертикали
        #
        # self.insert_num_letter = TextInput(                     # ТЕКСТОВОе поле
        #
        # size_hint = (1, 0.2),
        # multiline = False
        # )
        #
        # button = Button(                                    # кнопка
        #     text="Введите количество букв в слове",
        #     size_hint=(1, 1),
        #     on_press=self.on_press_button
        #
        # )
        #
        #
        #
        # self.add_widget(boxlayout)
        # boxlayout.add_widget(self.insert_num_letter)
        # boxlayout.add_widget(button)

    def get_word(self, new_word):
        self.word = new_word

    # def on_press_button(self):
    #     num = self.insert_num_letter
    #     print(num)

    #def create_word(self):

        # self.manager.transition.direction = 'left'
        # self.manager.current = 'two'



# class ScreenTwo(Screen):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#
#
#         label_word = Label(
#             text= "Загаданно слово из {} букв!"
#         )
#
#         boxlayout = BoxLayout(orientation="vertical")      #упорядочить по вертикали
#
#         insert_num_letter = TextInput(                     # ТЕКСТОВОе поле
#
#         size_hint = (1, 0.2),
#         multiline = False
#         )
#
#         button = Button(                                    # кнопка
#             text="Отгадайте слово !",
#             size_hint=(1, 1),
#
#         )
#
#         self.add_widget(boxlayout)
#         boxlayout.add_widget(insert_num_letter)
#         boxlayout.add_widget(button)
#         boxlayout.add_widget(label_word)
#
#
#
# class Bulls(App):
#     def build(self):
#         sm = ScreenManager()
#         sm.add_widget(ScreenOne(name='one'))
#         sm.add_widget(ScreenTwo(name='two'))
#
#         return sm
#
if __name__ == "__main__":
    ScreenOne().run()