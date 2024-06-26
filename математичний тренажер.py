from random import randint
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.spinner import Spinner
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup

Window.size = (400, 400)
Window.clearcolor = (78/255, 2/255, 133/255, 1)

class MyApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.k_missed = 0
        self.k_ok = 0
        self.k_error = 0

        self.a = randint(10, 99)
        self.b = randint(10, 99)
        self.sign = "+"

        self.title = "Математичний тренажер"

        self.box = BoxLayout(orientation="vertical")

        self.spinner = Spinner(text="Додавання в межах 100", values=("Додавання в межах 100", "Множення в межах 10"))
        self.example_label = Label(text= str(self.a) + self.sign + str(self.b) + "=")
        self.input_field = TextInput(multiline=False)
        self.check_button = Button(text="Перевірити")
        self.skip_button = Button(text="Пропустити цей приклад")
        self.skipped_examples_label = Label(text="Кількість пропущених прикладів: 0")
        self.solved_examples_label = Label(text="Кількість розв'язаних прикладів: 0")
        self.wrong_examples_label = Label(text="Кількість помилок: 0")

        # Додати в BoxLayout
        self.box.add_widget(self.spinner)
        self.box.add_widget(self.example_label)
        self.box.add_widget(self.input_field)
        self.box.add_widget(self.check_button)
        self.box.add_widget(self.skip_button)
        self.box.add_widget(self.skipped_examples_label)
        self.box.add_widget(self.solved_examples_label)
        self.box.add_widget(self.wrong_examples_label)

        # Команди
        self.spinner.bind(text=self.on_spinner_select)
        self.check_button.bind(on_press=self.check_button_click)
        self.skip_button.bind(on_press=self.skip_button_click)

    def on_spinner_select(self, spinner, text):
        if text == "Додавання в межах 100":
            self.sign = "+"
            self.var = 1
        else:
            self.sign = "*"
            self.var = 10
            
        self.a = int(randint(10, 99)/self.var)
        self.b = int(randint(10, 99)/self.var)
            
        self.example_label.text = str(self.a) + self.sign + str(self.b) + "="

        self.k_missed += 1
        self.skipped_examples_label.text = f"Кількість пропущених прикладів: {self.k_missed}"

    def check_button_click(self, *kwargs):
        if self.input_field.text == str(eval(f"{self.a} {self.sign} {self.b}")):
            popup_ok = Popup(title="Правильно, молодець!", size_hint=(0.8, 0.4))
            popup_ok.content = Button(text="Закрити", on_release=popup_ok.dismiss)
            popup_ok.open()
            self.k_ok = self.k_ok+1
            self.solved_examples_label.text = "Кількість розв'язаних прикладів: " + str(self.k_ok)
            self.next_example()
        else:
            popup_err = Popup(title="Неправильно!", size_hint=(0.8, 0.4))
            popup_err.content = Button(text="Закрити", on_release=popup_err.dismiss)
            popup_err.open()
            self.k_error = self.k_error+1
            self.wrong_examples_label.text = "Кількість помилок: " + str(self.k_error)

    def skip_button_click(self, *args):
        self.k_missed += 1
        self.skipped_examples_label.text = f"Кількість пропущених прикладів: {self.k_missed}"
        self.next_example()

    def next_example(self):
        self.a = int(randint(10, 99)/self.var)
        self.b = int(randint(10, 99)/self.var)
            
        self.example_label.text = str(self.a) + self.sign + str(self.b) + "="
        self.input_field.text = ""

    def build(self):
        return self.box

if __name__ == "__main__":
    MyApp().run()
