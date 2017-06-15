# benderbot_plugin.py
from app import create_app

crontable = []
outputs = []


def post_message(channel, message):
    """
    Sends a message to a specified Slack channel
    :param channel: Slack channel
    :param message: Message to be sent
    :return:
    """
    if message:
        outputs.append([channel, message])

benderbot_app = create_app(post_message)


def process_hello(_):
    """
    Event - connected to server
    :param _:
    :return:
    """
    print('[Info] Bender "Bending" Rodriguez connected to server')


def process_message(data):
    """
    Event - message received
    :param data:
    :return:
    """
    benderbot_app.process_command(data)
