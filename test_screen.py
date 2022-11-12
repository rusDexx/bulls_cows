


class ScreenOne(Screen):
    pass

class ScreenTwo(Screen):
    pass

class Bulls(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(ScreenOne(name='one'))
        sm.add_widget(ScreenTwo(name='two'))

        return sm

def main():
    if __name__ == "__main__":
        Bulls().run()





main()