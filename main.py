import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from chatbot import respond

class ChatInterface(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.history = TextInput(readonly=True, size_hint_y=0.9)
        self.add_widget(self.history)
        self.new_message = TextInput(hint_text="Type your message here...", size_hint_y=0.1)
        self.add_widget(self.new_message)
        self.send_button = Button(text="Send", size_hint_y=0.1)
        self.send_button.bind(on_press=self.send_message)
        self.add_widget(self.send_button)

    def send_message(self, *args):
        message = self.new_message.text
        self.new_message.text = ""
        response = respond(message)
        self.history.text += f"\nYou: {message}\nChatbot: {response}"

class ChatApp(App):
    def build(self):
        return ChatInterface()

if __name__ == "__main__":
    ChatApp().run()
