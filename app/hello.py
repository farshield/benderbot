# hello.py
from app import benderbot_app


@benderbot_app.register_cmd(r'(hello|hi|hey) bender')
def hello_world(data):
    return 'Hello <@{}>!'.format(data['user'])
