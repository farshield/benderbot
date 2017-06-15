# benderbot.py
import re


class BenderBot:
    """
    Command Dispatcher for BenderBot
    """
    def __init__(self, post_message=None):
        self.post_message = post_message  # callback
        self.command_map = {}

    def talk(self, channel, message):
        self.post_message(channel, message)

    def register_cmd(self, name):
        """
        Decorator for registering a command for the current module
        :param name: RegEx pattern
        :return:
        """
        def func_wrapper(func):
            self.command_map[name] = func
            return func
        return func_wrapper

    def process_command(self, data):
        for command in self.command_map:
            # try to find matching command
            if re.search(command, data['text'], re.IGNORECASE):
                callback = self.command_map[command]
                if callable(callback):
                    self.post_message(data['channel'], callback(data))


def main():
    from app import create_app

    def post_message(channel, message):
        print(u'[{}] {}'.format(channel, message))

    benderbot_app = create_app(post_message)
    while True:
        command = raw_input('> ')
        if not command:
            break
        benderbot_app.process_command({'channel': 'Debug', 'user': None, 'text': command})

if __name__ == "__main__":
    main()
