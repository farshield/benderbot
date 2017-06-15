# app
from benderbot import BenderBot
benderbot_app = BenderBot()
import hello  # noqa
import stuff  # noqa


def create_app(post_message):
    benderbot_app.post_message = post_message
    return benderbot_app
